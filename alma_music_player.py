# <============ IMPORTS ===============>
import threading, random, os
from new_ui_updater import UIUpdates
from alma_ui_builder import ProgramUI
from new_player_engine import PlayerEngine
from alma_player_settings import PlayerData
from new_library_manager import LibraryManager
from alma_ui_configurer import ProgramUIConfigurer
from alma_database_manager import AlmaDatabaseManager
# <====================================>

# ========================================================================================================================
# ============================================ ALL DEPENDENCIES
def thread_worker(target, arguments, daemon: bool) -> None:
	''' Spawn the passed function in a background thread '''
	# --
	_worker = threading.Thread(
		target=target,
		args=arguments,
		daemon=daemon
	)

	_worker.start()

	#<_end of the function_>

# ========================================================================================================================
# ========================================================================================================================

class ProgramPlaylists:
	def __init__(self, root, pub) -> None:
		# --
		self.root = root
		self.pub = pub
		# ---
		self.main_playlist = []      # -- Main playlist with track paths
		self.main_basenames = []
		self.shuffled_playlist = []
		self.users_favourites = []   # -- Users favourite songs
		# ---

		#<_end of the method_>

	def select_tracks_to_add(self, paths: dict) -> None:
		''' Avoid adding Duplicates to UI '''
		# --
		added = []   # -- used to display added tracks
		for track, track_path in paths.items():
			# -- Ignore duplicates
			if track in self.main_basenames:
				# -- ignore
				continue

			# -- Add this track to playlist
			added.append(track)
			self.main_basenames.append(track)
			self.main_playlist.append(track_path)

			try:
				# -- Clamp btn 0 and max length
				self.shuffled_playlist.insert(
					random.randint(
						0,
						(len(self.shuffled_playlist) - 1)
					),
					track_path
				)

			except ValueError:
				# -- Insert at pos 0
				self.shuffled_playlist.insert(
					0,
					track_path
				)

		if added:
			# -- Display added songs
			self.root.after(
				0,
				self.pub.mini_queue,
				added
			)

		#<_end of the method_>

	def repeat_all_mode_idx(self, hint: int) -> None:
		''' Sets the next track index. Also runs few algorithms to ensure UI updates '''
		# --
		m_p = self.main_playlist
		m_b = self.main_basenames

		# -- Update current index (wrap-around incase we at the end)
		prev_index: int = self.pyr.track_index
		self.pyr.track_index = (self.pyr.track_index + hint) % len(m_p)

		if ((self.pyr.track_index % 5) == 0) and (hint == 1):
			# -- Build Mini queue

			tracks: list[str] = m_b[self.pyr.track_index:]
			start_point: int = m_b.index(tracks[0])

			build_mini_queue: bool = True

		elif (hint == -1) and ((prev_index % 5) == 0):
			# -- Build Mini queue

			# -- Check positions of indices
			if self.pyr.track_index > prev_index:
				# -- prev index is at 0, while track index may be at 15: find starting point
				if ((self.pyr.track_index % 5) == 0):
					# -- Should display only one item
					tracks: list[str] = [m_b[self.pyr.track_index]]

				else:
					# -- find previous int divisible by 5
					pos: int = self.pyr.track_index

					while ((pos % 5) != 0):
						# -- Decrease number
						pos -= 1

					# -- Collect items from pos to end
					tracks: list[str] = m_b[pos:]

			else:
				# -- Normal queue

				tracks: list[str] = m_b[(prev_index - 5):]

			start_point: int = m_b.index(tracks[0])
			build_mini_queue: bool = True

		else:
			# -- Don't Build
			tracks: list = []
			start_point: int = 0
			build_mini_queue: bool = False

		return tracks, start_point, build_mini_queue

		#<_end of the method_>

	def shuffle_mode_idx(self, hint: int) -> None:
		''' Sets the next track index. Also runs few algorithms to ensure UI updates '''
		# --
		m_p = self.main_playlist
		m_b = self.main_basenames
		s_p = self.shuffled_playlist

		# --
		prev_index: int = self.pyr.track_index
		shuff_idx: int = s_p.index(m_p[self.pyr.track_index])
		self.pyr.track_index = m_p.index(s_p[((shuff_idx + hint) % len(s_p))])

		# -- Build?
		if (self.pyr.track_index % 5 == 0):
			# -- Build mini queue
			tracks: str = m_b[self.pyr.track_index:]
			start_point: int = m_b.index(tracks[0])
			build_mini_queue: bool = True

		elif (int(str(self.pyr.track_index - prev_index).replace('-', ''))) > 4:
			# -- Find start point
			pos: int = self.pyr.track_index

			# --
			while (pos % 5 != 0):
				# -- reduce pos
				pos -= 1

			# --
			tracks: list[str] = m_b[pos:]
			start_point: int = m_b.index(tracks[0])
			build_mini_queue: bool = True

		else:
			# -- Next song in the same mini queue as the previous song
			tracks: list = []
			start_point: int = 0
			build_mini_queue: bool = False

		return tracks, start_point, build_mini_queue

		#<_end of the method_>

	def clear_playlist_bags(self) -> None:
		'''
		Clear Playlist bags. Necessary while loading a folder
		or a playlist.
		'''
		# --
		self.main_playlist.clear()
		self.main_basenames.clear()

		#<_end of the method_>

class MusicApp(ProgramPlaylists):
	def __init__(self) -> None:
		# ======================================================================================
		# ============================================ ALL DEPENDENCIES
		self.dbm = AlmaDatabaseManager(self)
		self.pda = PlayerData(self)
		self.lib = LibraryManager(self)
		self.pyr = PlayerEngine(self)
		self.uiu = UIUpdates(self)
		self.puc = ProgramUIConfigurer(self)
		self.pub = ProgramUI(self)

		super().__init__(self.pub.root, self.pub)

		self.pub.root.protocol('WM_DELETE_WINDOW', self.on_app_close)
		self.pub.root.mainloop()
		# ======================================================================================
		# ======================================================================================

		#<_end of the method_>

	def toggle_shuffle(self, shuffle_btn) -> None:
		''' Update the current playback mode '''
		# --
		if self.pda.player_data['shuffle_on']:
			# -- Toggle shuffle off
			text: str = '🔁'
			self.pda.player_data['shuffle_on'] = False

		else:
			# -- Toggle shuffle on
			text: str = '🔃'
			self.pda.player_data['shuffle_on'] = True

		# -- Update text on button
		self.uiu.update_text_on(
			object=shuffle_btn,
			text=text
		)

		#<_end of the method_>

	def toggle_loop(self, loop_btn) -> None:
		''' Update the current playback mode '''
		# --
		if self.pda.player_data['loop_on']:
			# -- Repeat one
			text: str = '🔂'
			self.pda.player_data['loop_on'] = False

		else:
			# -- Loop all
			text: str = '🔁'
			self.pda.player_data['loop_on'] = True

		# -- Update text on button
		self.uiu.update_text_on(
			object=loop_btn,
			text=text
		)

		#<_end of the method_>

	def on_app_close(self) -> None:
		''' Save Player Data '''
		# --
		self.pda.save_player_data()

		# -- Close window
		self.pub.root.destroy()

		#<_end of the method_>

if __name__ == '__main__':
	MusicApp()