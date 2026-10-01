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

	APP_THEMES = {
		'alma_default': {
			'primary_bg': '#1B1E33',                        # -- Canvas where body lines are drawn
			'secondary_bg': '#0F111D',                      # -- Background colour of items built on the main canvas
			'border': '#353A4F',                            # -- Colour of the dividers

			'primary_text_colour': '#FFFFFF',               # --
			'secondary_text_colour': '#4DD4AC',
			'third_text_colour': '#AFABAB',

			'navigator_default_bg': '#1B1E33',
			'navigator_default_fg': '#FFFFFF',

			'navigator_hover_bg': '#3E3F5E',
			'navigator_hover_fg': '#FFFFFF',

			'frame_highlight_bg': '#4DD4AC',
			'frame_highlight_fg': '#0F111D',

			'controls_fg': '#FFFFFF',
			
			'progress_canvas_default': '#2E2E2E',
			'progress_canvas_highlight': '#4DD4AC',

			'volume_canvas_default': '#2E2E2E',
			'volume_canvas_highlight': '#4DD4AC',
			'waveform_colour': '#4DD4AC',
		},

		'theme_1': {
			'primary_bg': '#032a1f',                        # -- Canvas where body lines are drawn
			'secondary_bg': '#021712',                      # -- Background colour of items built on the main canvas
			'border': '#0a7d5f',                            # -- Colour of the dividers

			'primary_text_colour': '#F8E7C9',               # --
			'secondary_text_colour': '#4e3b06',
			'third_text_colour': '#010705',

			'navigator_default_bg': '#032a1f',
			'navigator_default_fg': '#F8E7C9',

			'navigator_hover_bg': '#0b9571',
			'navigator_hover_fg': '#23312d',

			'frame_highlight_bg': '#F8E7C9',
			'frame_highlight_fg': '#2a2a2a',

			'controls_fg': '#F8E7C9',

			'progress_canvas_default': '#564b49',
			'progress_canvas_highlight': '#F8E7C9',

			'volume_canvas_default': '#564b49',
			'volume_canvas_highlight': '#F8E7C9',
			'waveform_colour': '#F8E7C9',
		},

		'theme_2': {
			'primary_bg': '#181a20',                        # -- Canvas where body lines are drawn
			'secondary_bg': '#0d0e12',                      # -- Background colour of items built on the main canvas
			'border': '#9ca2b5',                            # -- Colour of the dividers

			'primary_text_colour': '#666f89',               # --
			'secondary_text_colour': '#064e3b',
			'third_text_colour': '#07184b',

			'navigator_default_bg': '#181a20',
			'navigator_default_fg': '#ebebeb',

			'navigator_hover_bg': '#393e4c',
			'navigator_hover_fg': '#ffd6a5',

			'frame_highlight_bg': '#ffd6a5',
			'frame_highlight_fg': '#020303',

			'controls_fg': '#666f89',

			'progress_canvas_default': '#343845',
			'progress_canvas_highlight': '#ffd6a5',

			'volume_canvas_default': '#343845',
			'volume_canvas_highlight': '#ffd6a5',
			'waveform_colour': '#666f89',
		},

	}

	DEFAULT_PROGRAM_DATA = {
		# -- theme
		'active_theme': 'alma_default',

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
		],

		'tracks_data': {}
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