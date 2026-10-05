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
			'display_name': 'Alma Classic',
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
			'display_name': 'Emerald Ivory',
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
			'display_name': 'Slate & Peach',
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

		'theme_3': {
			'display_name': 'Violet Ember',
		    'primary_bg': '#171522',
		    'secondary_bg': '#0D0B12',
		    'border': '#383247',

		    'primary_text_colour': '#F1EDF7',
		    'secondary_text_colour': '#ff7f50',
		    'third_text_colour': '#777181',

		    'navigator_default_bg': '#171522',
		    'navigator_default_fg': '#F1EDF7',

		    'navigator_hover_bg': '#29223A',
		    'navigator_hover_fg': '#D8B4FE',

		    'frame_highlight_bg': '#B06CFF',
		    'frame_highlight_fg': '#0D0B12',

		    'controls_fg': '#D8D0E2',

		    'progress_canvas_default': '#302A38',
		    'progress_canvas_highlight': '#B06CFF',

		    'volume_canvas_default': '#302A38',
		    'volume_canvas_highlight': '#B06CFF',

		    'waveform_colour': '#B06CFF',
		},

		'midnight_forest': {
			'display_name': 'Gilded Forest',
		    'primary_bg': '#151A18',
		    'secondary_bg': '#0A0F0D',
		    'border': '#35403A',

		    'primary_text_colour': '#F1F0E8',
		    'secondary_text_colour': '#C7A85A',
		    'third_text_colour': '#718078',

		    'navigator_default_bg': '#151A18',
		    'navigator_default_fg': '#F1F0E8',

		    'navigator_hover_bg': '#202B25',
		    'navigator_hover_fg': '#E0C878',

		    'frame_highlight_bg': '#C7A85A',
		    'frame_highlight_fg': '#0A0F0D',

		    'controls_fg': '#AEBBB4',

		    'progress_canvas_default': '#303A34',
		    'progress_canvas_highlight': '#C7A85A',

		    'volume_canvas_default': '#303A34',
		    'volume_canvas_highlight': '#C7A85A',

		    'waveform_colour': '#8FAFA0',
		},

		'crimson_moon': {
			'display_name': 'Crimson Moon',
		    'primary_bg': '#181319',
		    'secondary_bg': '#0C090D',
		    'border': '#3A3039',

		    'primary_text_colour': '#F2EDF0',
		    'secondary_text_colour': '#C65F70',
		    'third_text_colour': '#77808D',

		    'navigator_default_bg': '#181319',
		    'navigator_default_fg': '#F2EDF0',

		    'navigator_hover_bg': '#2A1C24',
		    'navigator_hover_fg': '#E38A98',

		    'frame_highlight_bg': '#C65F70',
		    'frame_highlight_fg': '#0C090D',

		    'controls_fg': '#B9B4BB',

		    'progress_canvas_default': '#33272E',
		    'progress_canvas_highlight': '#C65F70',

		    'volume_canvas_default': '#33272E',
		    'volume_canvas_highlight': '#C65F70',

		    'waveform_colour': '#8794A6',
		},

		'deep_atlas': {
			'display_name': 'Midnight Atlas',
		    'primary_bg': '#111923',
		    'secondary_bg': '#080E15',
		    'border': '#303D4C',

		    'primary_text_colour': '#F1EEE6',
		    'secondary_text_colour': '#D27A68',
		    'third_text_colour': '#718194',

		    'navigator_default_bg': '#111923',
		    'navigator_default_fg': '#F1EEE6',

		    'navigator_hover_bg': '#1C2A38',
		    'navigator_hover_fg': '#E59A89',

		    'frame_highlight_bg': '#D27A68',
		    'frame_highlight_fg': '#080E15',

		    'controls_fg': '#B9C4CE',

		    'progress_canvas_default': '#293542',
		    'progress_canvas_highlight': '#D27A68',

		    'volume_canvas_default': '#293542',
		    'volume_canvas_highlight': '#D27A68',

		    'waveform_colour': '#8DA5B8',
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