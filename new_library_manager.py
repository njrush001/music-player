# <============ IMPORTS ===============>
import os, threading
from typing import Optional
from tkinter import filedialog
from new_player_engine import music_playing
# <====================================>

class LibraryManager:
	def __init__(self, app) -> None:
		# --
		self.app = app

		#<_end of the method_>

	def select_folder(self) -> Optional[str]:
		''' Allow User To Select a folder with his Music '''
		FOLDER: str = filedialog.askdirectory(
				title='Select The Folder With Your Music'
			)

		# --
		return FOLDER if FOLDER else None

		#<_end of the method_>

	def get_music_from_folder(self, *args) -> None:
		''' Return list of paths from the directory user will choose'''
		user_folder: str = self.select_folder()

		if user_folder is not None:
			# -- song list
			paths = {}

			# -- Open folder and append tracks
			for r, _, files in os.walk(user_folder):
				for f in files:
					if f.lower().endswith('.mp3'):
						paths[f.replace('.mp3', '')] = os.path.join(r, f)

			if paths:
				# --
				track = None
				if music_playing():
					# --
					track = self.app.main_playlist[self.app.pyr.track_index]

					#<_>

				# -- Clear Playlist bags
				self.app.clear_playlist_bags()
				
				# -- Show these paths in UI(if applicable)
				if track is not None:
					# -- Don't build mini queue
					self.app.select_tracks_to_add(
						paths=paths,
						initiate_build=False
					)

					# -- Track playing(will trigger build of mini queue once it gets the right idx)
					self.app.track_playing(track=track)

					return

					#<_>

				# -- track is unavailable (build mini queue - probably the program has just started)
				self.app.select_tracks_to_add(paths)

		#<_end of the method_>

	def _search_file(self, track) -> None:
		''' Find the location of the given song '''
		# -- Folders To Search
		FOLDERS: list = self.app.pda.player_data['music_folders'].copy()

		# -- Attempt search
		for _dir in FOLDERS:
			for r, _, files in os.walk(_dir):
				# -- Attempt search in this folder's files
				if track in files:
					# -- Return file path
					return os.path.join(r, track)
		
		# -- Song not available
		return None

		#<_end of the method_>

	def _get_paths(self, tracks: list, last_play=False) -> None:
		''' Find paths in Know Folders '''
		# -- Will Hold All Paths That Are Found
		found = {}

		# -- For Every Track, Attempt Finding its location
		for track in tracks:
			# -- Attempt Search
			path = self._search_file(track)

			# -- Add Found paths to found
			if path is not None:
				# -- Add
				found[track.replace('.mp3', '')] = path
		# --
		if len(found) > 0:
			# -- Clear playlists & Add
			self.app.clear_playlist_bags()
			self.app.select_tracks_to_add(paths=found)

		#<_end of the method_>

	def thread_worker_for_search(self, tracks, last_play=False) -> None:
		''' Initiate thread worker for search '''
		# -- Create task
		_task = threading.Thread(
			target=self._get_paths,
			args=(tracks,), kwargs={'last_play': last_play},
			daemon=True)

		# -- Start the task
		_task.start()

		#<_end of the method_>
