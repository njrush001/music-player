# <============ IMPORTS =========================>
from pathlib import Path
# <==============================================>

class AlmaDataPaths:
	''' Create Directories For Various Data Files '''

	# -- Get Base Directory
	BASE_DIR = Path(__file__).resolve().parent
	# -- Default Music Folder
	MUSIC_DIR = BASE_DIR / 'music'
	# -- Recommendations and Playlists Data Files Live Here
	DATA_DIR = BASE_DIR / 'data'
	# -- Exceptions Files
	ERROR_DIR = BASE_DIR / 'errors'
	# -- Background Dir
	BG_DIR = BASE_DIR / 'background'
	# -- Created Playlists Stay Here
	PLAYLIST_DIR = BASE_DIR / 'playlists'
	# -- Player Settings File Stays Here
	SETTINGS_DIR = BASE_DIR / 'settings_data'

	DEFAULT_PROGRAM_DATA = {
		# -- repeat all is the default
		'loop_on': True,

		# -- Shuffle mode not active
		'shuffle_on': False,
		
		# -- Startup volume 20%
		'volume_level': 0.2,

		# -- Song that played last before the app was closed
		'last_played_data': {},

		# -- Folders to scan
		'music_folders': [
			str(MUSIC_DIR)
		],

		# -- Download history
		'downloads': [],

		# -- Search Hints
		'search_hints': [
            'Search by song title...',
            'Try an artist name...',
            'Looking for a track?',
            'Search by album name...',
            'Find a song for your mood...',
            'Type a lyric you remember...',
            'Play an old favorite...',
            'Dig up a hidden gem...',
            'Music just feels right...',
            "Type if you can't find it...",
            "Drag & Drop Functional😍",
            "Add Files Using The Button Below👇",
            "Add Songs To Favoutites👇"
		],

		'live_messages': [
            "Tip: Save Your Favourite Tracks",
            "Tip: Use Artwork To Tell The Next Song",
            "Tip: Beautiful Design, Isn't it?",
            "Tip: Use The Playlist Function To Customise Your Playlists",
            "Tip: The App Tracks Your Playstyle.",
            "Tip: The App Can Get Exciting. Take A Break Sometimes",
            "Tip: Protect Your Ears From Outside Noise",
            "Tip: Alma Music Player, One You Need While Studying",
            "Tip: Forget About The Logic Behind & Enjoy",
            "Tip: Recommend The Upgrades You Desire To See",
            "Tip: Jump And Listen Where It Strucks You The Most",
            "Tip: Seeking Communicates A Lot",
            "Tip: Your Feedback Is Always Appreciated",
            "Tip: Alma Music Player ! The Best Personal Music Player ❤"
		]
	}

#<_ END OF ALMADATAPATHS_>

# --- This part runs once
_bag = [
	AlmaDataPaths.MUSIC_DIR,     # -- Music stored in this folder
	AlmaDataPaths.BG_DIR,        # -- Has the default background artwork for the app
	AlmaDataPaths.DATA_DIR,      # -- Has 'saved_data.json' & 'recommendations.json'
	AlmaDataPaths.ERROR_DIR,     # -- Has 'exceptions.txt'
	AlmaDataPaths.PLAYLIST_DIR,  # -- This is where the program store created playlists
	AlmaDataPaths.SETTINGS_DIR   # -- This is where users' preferences are saved
]

for _dir in _bag:
	# -- Create the directory if not available
	_dir.mkdir(parents=True, exist_ok=True)