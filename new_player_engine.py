# <============ IMPORTS ===============>
import pygame
from typing import Optional
from mutagen.mp3 import MP3
from new_ui_updater import extract_metadata_for_track, extract_track_artwork
# <====================================>

# -- Engine used to play music
pygame.mixer.init()

# ========================================================================================================================
# ============================================ ALL DEPENDENCIES

def fade_out_song(fade_out_time: int) -> None:
	''' Fade out the currently playing track '''
	# -- Fade out currently playing song
	pygame.mixer.music.fadeout(fade_out_time)

	#<_end of the method_>

def get_track_duration(path) -> int:
	''' Get the track duration of the given track path '''
	# --
	try:
		# --
		audio = MP3(path)

		# -- return the audio duration
		return int(audio.info.length)

	except FileNotFoundError:
		# -- return 0
		return 0

	#<_end of the function_>

def play_song(start: float = 0.0, fade_ms: int = 600) -> None:
	''' Play the passed song '''
	pygame.mixer.music.play(start=start, fade_ms=fade_ms)

	#<_end of the method_>

def load_song(path) -> None:
	''' Load the passed track '''
	try:
		# --
		pygame.mixer.music.load(path)
	except Exception as e:
		print(e)

	#<_end of the method_>

# ========================================================================================================================
# ========================================================================================================================


class PlayerEngine:
	def __init__(self, app) -> None:
		# --
		self.app = app

		self.playing = ''            # -- Currently playing song
		self.track_index = 0         # -- Position of the playing song
		self.track_duration = 0      # -- Track duration of the currently playing
		self.track_paused = False    # -- Indicates when a track is paused or not
		self.user_seeking = False    # -- User dragging
		self.progress_update = None  # --

		#<_end of the method_>

	def set_volume(self, vol: float) -> None:
		''' Set volume level '''
		# --
		pygame.mixer.music.set_volume(vol)

		self.app.pda.player_data['volume_level'] = vol

		#<_end of the function_>

	def update_progress(self) -> None:
		'''
		Displays progress ratio, time elapsed and remaining time.
		'''
		# --
		if not pygame.mixer.music.get_busy() and not self.track_paused:
			# -- Song ended naturally
			self.app.pub.root.after_cancel(self.progress_update)
			self.next_playable(hint=1)

			#<_>

		elif self.track_paused:
			# -- Track is paused -> stop scheduling until unpaused
			self.app.pub.root.after_cancel(self.progress_update)

		elif self.user_seeking:
			# -- Do not update UI
			self.progress_update = self.root.after(50, self.update_progress)
		else:
			# -- Update UI
			p_c = self.app.pub.progress_canvas
			x_1: int = int(pygame.mixer.music.get_pos() / self.track_duration) * p_c.winfo_width()

			self.app.puc.on_progress_canvas_click(
				set_point=x_1,
				progress_canvas=p_c
			)

			# --
			self.progress_update = self.app.pub.root.after(50, self.update_progress)

		#<_end of the method_>


	# -------------------------------------------------------------------------------------
	# -------------------------------------------------------------------------------------
	# ------------------------------- PLAYBACK CONTROLS -----------------------------------

	def initialise(self, build_mini_queue: bool, track_index: Optional[int], build_data=None) -> None:
		''' Load and play track. And initiate UI updates '''

		# -- Update track index
		self.track_index = track_index if track_index is not None else self.track_index
		path = self.app.main_playlist[self.track_index]

		# -- Load and play
		load_song(path)
		play_song()

		# -- Get artist, song_name and artwork
		track_name, artist = extract_metadata_for_track(path)
		artwork = extract_track_artwork(path)
		self.track_duration = get_track_duration(path)

		# -- Update track name and artist
		self.app.uiu.update_text_on(
			object=self.app.pub.song_title,
			text=track_name,
		)

		self.app.uiu.update_text_on(
			object=self.app.pub.artist,
			text=artist,
		)

		# -- Cross_fade images

		self.app.uiu.crossfade_images(
			label=self.app.pub.audio_thumbnail,
			new_img=artwork
		)

		self.app.uiu.crossfade_images(
			label=self.app.pub.sub_audio_thumbnail,
			new_img=artwork,
			size=(55, 55)
		)

		if build_mini_queue:

			# -- Update queue
			self.app.pub.mini_queue(
				# -- tracks from the current playing to end
				tracks=build_data[0],
				start_point=build_data[1]
			)

		# -- Highlight
		try:
			# --
			self.app.puc.unhighlight_inactive_frame(
				frame=self.app.puc.track_frames_data[self.app.puc.track_frames_data['active_frame']]
			)
		except KeyError:
			# --
			pass

		# -- Get frames
		frames = list(self.app.puc.track_frames_data.keys())
		frames.remove('active_frame')

		# -- Consider index range
		try:
			# -- Get object id
			idx: int = self.track_index
			obj_id: str = frames[idx]
		except IndexError:
			# curr idx not in [0,1,2,3,4]. Translate self.track_index to one of them
			if (self.track_index % 5) == 0:
				# -- Implies we are at the starting point
				idx: int = 0
				obj_id: str = frames[idx]
			else:
				# -- Determine idx in a while loop
				idx: int = 0
				check_pos: int = self.track_index

				while ((check_pos % 5) != 0):
					# --
					check_pos -= 1
					idx += 1        # -- Gets near target

				obj_id: str = frames[idx]

		frame_to_highlight = self.app.puc.track_frames_data[obj_id]

		# -- Highlight
		self.app.puc.on_click(
			event=None, object=frame_to_highlight,
			fg='#0F111D', bg='#4DD4AC', item_type='frame'
		)

		# --
		self.app.puc.track_frames_data['active_frame'] = obj_id


		#<_end of the method_>

	def pause_track(self, pause_btn) -> None:
		''' Pause the currently playing song '''
		# --
		pygame.mixer.music.pause()

		# -- Configure button text
		self.app.uiu.update_text_on(
			object=pause_btn,
			text='▶'
		)

		# -- Paused state
		self.track_paused = True

		#<_end of the method_>

	def resume_track(self, unpause_btn) -> None:
		''' Unpause the song '''
		# --
		pygame.mixer.music.unpause()

		# -- Configure button text
		self.app.uiu.update_text_on(
			object=unpause_btn,
			text='⏸'
		)

		# -- Unpaused state
		self.track_paused = False

		#<_end of the method_>

	def _delayed_song(self, hint: int) -> None:
		'''
		Delay playback of the previous or next song.
		Hint is a value, either +1, or -1. and both
		correspond to next and previous song. When 
		passed, this method will decide which song to
		play next.
		'''
		# -- Get play mode
		loop_on: bool = self.app.pda.player_data['loop_on']
		shuffle_on: bool = self.app.pda.player_data['shuffle_on']

		if not loop_on:
			# -- Repeat one mode
			tracks: list = []
			start_point: int = 0
			build_mini_queue: bool = False
			# --

		elif loop_on and not shuffle_on:
			# -- loop all and shuffle mode not on
			data: tuple[list, int, bool] = self.app.repeat_all_mode_idx(hint=hint)
			# --
			tracks: list = data[0]
			start_point: int = data[1]
			build_mini_queue: bool = data[2]
			# --

		else:
			# -- Shuffle On
			data: tuple[list, int, bool] = self.app.shuffle_mode_idx(hint=hint)
			# --
			tracks: list = data[0]
			start_point: int = data[1]
			build_mini_queue: bool = data[2]
			# --

		# -- Initiate playback; also build mini_queue
		self.initialise(
			track_index=None,
			build_data=[tracks, start_point],
			build_mini_queue=build_mini_queue
		)

		#<_end of the method_>

	def next_playable(self, hint: int) -> None:
		''' Play the next or previous track in queue '''
		# --
		if not self.app.main_playlist and not pygame.mixer.music.get_busy():
			# -- No music playing
			return

		# -- fade out currently playing
		fade_out_song(fade_out_time=620) # -- 620ms to fade out the previous song

		# -- Delay a lil bit
		self.app.pub.root.after(
			100,
			self._delayed_song,
			hint
		)

		#<_end of the method_>

	# -------------------------------------------------------------------------------------
	# -------------------------------------------------------------------------------------
	# -------------------------------------------------------------------------------------

	# -------------------------------------------------------------------------------------
	# -------------------------------------------------------------------------------------
	# ---------------------------------- LAST PLAYED --------------------------------------

	def last_played_track(self) -> None:
		pass

		#<_end of the method_>

	def play_last_played_track(self) -> None:
		pass

		#<_end of the method_>

	# -------------------------------------------------------------------------------------
	# -------------------------------------------------------------------------------------
	# -------------------------------------------------------------------------------------