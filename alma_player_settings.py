# <============ IMPORTS ===============>
import os
from typing import Optional
from config import AlmaDataPaths
from new_ui_updater import clean_title
# <====================================>

class PlayerData:
	def __init__(self, app) -> None:
		self.app = app

		# -- Load user data
		self.load_user_data()

	def load_user_data(self) -> None:
		''' Load Crucial User Data '''
		# --- Load User Data
		self.last_played_data = self.app.dbm.read_data(self.app.dbm.LAST_PLAYED_FILE, {})
		self.music_folders = self.app.dbm.read_data(self.app.dbm.MUSIC_FOLDERS_FILE, [AlmaDataPaths.MUSIC_DIR])
		self.playback_data = self.app.dbm.read_data(self.app.dbm.PLAYBACK_DATA, {'loop_on': True, 'shuffle_on': False, 'volume_level': 0.2})
		self.active_theme = self.app.dbm.read_data(self.app.dbm.THEME_FILE, {'active_theme': 'alma_default'})
		self.tracks_data = self.app.dbm.read_data(self.app.dbm.TRACKS_DATA_FILE, {})
		self.wave_data = self.app.dbm.read_data(self.app.dbm.WAVE_DATA_FILE, {})
		# ---
		# ---

		#<__ end of the method __>

	def get_last_played_data(self) -> str:
		''' Get the last played song from loaded data '''
		track_path = self.last_played_data.get('song', None)

		# --
		if track_path is not None:
			# -- Get progress ratio
			progress_ratio = self.last_played_data.get('progress_ratio', 0)
			track_duration = self.last_played_data.get('track_duration', 0)

			return track_path, progress_ratio, track_duration

			#<_>

		return '', 0, 0

		#<_end of the method_>

#<_ END OF SETTINGSMANAGER>