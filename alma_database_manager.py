import json, os
from config import AlmaDataPaths

class AlmaDatabaseManager:

	# -- file_names
	REQUIRED_FILES = {
		'playback_data.json': {'loop_on': True, 'shuffle_on': False, 'volume_level': 0.2},
		'last_played.json': {},
		'live_updates_hints.json': {},
		'music_folders.json': [AlmaDataPaths.MUSIC_DIR],
		'theme.json': {'active_theme': 'alma_default'},
		'tracks_data.json': {},
		'wave_data.json': {}
	}

	def __init__(self) -> None:
		# -------------
		# -------------
		self.PLAYBACK_DATA = AlmaDataPaths.DATA_DIR / 'playback_data.json'
		self.LAST_PLAYED_FILE = AlmaDataPaths.DATA_DIR / 'last_played.json'
		self.LIVE_UPDATES_FILE = AlmaDataPaths.DATA_DIR / 'live_updates_hints.json'
		self.MUSIC_FOLDERS_FILE = AlmaDataPaths.DATA_DIR / 'music_folders.json'
		self.THEME_FILE = AlmaDataPaths.DATA_DIR / 'theme.json'
		self.TRACKS_DATA_FILE = AlmaDataPaths.DATA_DIR / 'tracks_data.json'
		self.WAVE_DATA_FILE = AlmaDataPaths.DATA_DIR / 'wave_data.json'
		# --------------
		# --------------

		def _check(check_type: str) -> None:
			paths = {}
			for r, _, files in os.walk(AlmaDataPaths.DATA_DIR):
				for f in files:
					# --
					full_path = os.path.join(r, f)
					paths[f] = full_path

			if check_type == 'delete_unknown':
				for f in paths:
					if f not in AlmaDatabaseManager.REQUIRED_FILES:
						os.remove(paths[f])    # -- Delete unknown file

			elif check_type == 'create_unavailable':
				for p in AlmaDatabaseManager.REQUIRED_FILES:
					if p not in paths:
						# --
						self.save_data(AlmaDatabaseManager.REQUIRED_FILES[p], AlmaDataPaths.DATA_DIR / f'{p}.json')

			#<_end of inner function_>

		# -- Twice check: one for deletion, the other for creation
		_check(check_type='delete_unknown')
		_check(check_type='create_unavailable')

		#<_end of the method_>

	def read_data(self, path, return_value) -> dict:
		'''
		Return Data saved in a certain database:
		 - path -> represents the full path of the database to be read
		'''

		try:
			with open(path, 'r') as database:
				return json.load(database)

		except FileNotFoundError:
			return return_value

		#<__ end of the method __>

	def save_data(self, data, path) -> None:
		''' Save data to a file '''
		try:
			with open(path, 'w') as database:
				json.dump(data, database, indent=4)

		except Exception as e:
			raise e

		#<__ end of the method __>


#<_ END OF DATABASEMANAGER_>