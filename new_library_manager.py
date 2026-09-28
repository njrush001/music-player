# <============ IMPORTS ===============>
import os
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