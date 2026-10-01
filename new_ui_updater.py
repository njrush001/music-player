# <============ IMPORTS ===============>
import os, io
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from PIL import Image, ImageTk
from config import AlmaDataPaths
from mutagen.easyid3 import EasyID3
# <====================================>

# ========================================================================================================================
# ============================================ ALL DEPENDENCIES

def open_image_path(img_path):
	''' Open image at the given path '''
	return Image.open(img_path)

	#<_end of the function_>

def set_image(label, img, size: tuple[int, int], blended_img=None) -> None:
	''' Set Image '''
	if blended_img is None:
	# -- Open img and resize
		try:
			_img = img.resize(size)

		except AttributeError:
			# -- Use default artwork
			_img = open_image_path(
				img_path=AlmaDataPaths.BG_DIR / 'alma_bgd.png'
			).resize(size)

		finally:
			_photo = ImageTk.PhotoImage(_img)

	else:
		# -- cross fading in action
		_photo = ImageTk.PhotoImage(blended_img)

	# -- Display image
	label.config(image=_photo)
	label.image = _photo

#<_end of the function_>

def extract_track_artwork(path):
	''' Extract the thumbnail of the current playing '''
	try:
		audio = ID3(path)
		for tag in audio.values():
			if tag.FrameID == 'APIC':
				img = Image.open(io.BytesIO(tag.data))

				# -- Return the img
				return img

	except Exception:
		# --- Such songs do not start with an ID3 Tag
		return None

	#<__ end of the function __>

def clean_title(path, max_lmt: int = 20, max_show: int = 17) -> str:
	''' Return a song name to be displayed in the UI '''
	base: str = os.path.basename(path)
	clean_base: str = base.replace('.mp3', '').title()

	# --- Characters should not exceed max_lmt
	if len(clean_base) > max_lmt:
		# -- Return max_show of specified characters
		return clean_base[:max_show] + ' ...'
	
	return clean_base

	#<_end of the function_>

def extract_metadata_for_track(path) -> tuple[str]:
	'''
	Extract the following info from a track
	 - Song's Title
	 - Song's Artist
	'''
	audio = MP3(path, ID3=EasyID3)

	# -- Get title and artist (if available)
	title: str = audio.get('title', 'Unknown Title')
	artist: str = audio.get('artist', 'Unknown Artist')
	# --

	# --
	if title == 'Unknown Title':
		# -- Use Basename
		title: str = os.path.basename(path)
	else:
		title: str = title[0]
	
	if artist == 'Unknown Artist':
		# -- Use App owner name
		artist: str = 'Alma'
	else:
		# -- Artist Name Found
		artist: str = artist[0]
	# ==========================
	# ==========================
	
	# -- Clean Title
	c_t: str = clean_title(title, max_lmt=35, max_show=33)

	return c_t, artist

	#<_end of function_>

# ========================================================================================================================
# ========================================================================================================================

class UIUpdates:
	def __init__(self, app) -> None:
		self.app = app
		self.root = None
		self.generating_data = False

		#<__ end of the method __>

	def update_text_on(self, object, text: str) -> None:
		''' Update text on the passed object '''
		try:
			# --
			self.root.after(
				0,
				lambda: object.config(text=text)
			)

		except Exception:
			pass

		#<_end of the method_>

	def place_object(self, object, delta: int, **kwargs) -> None:
		'''
		Place an object after some time delta using the properties
		specified under kwargs
		'''
		# --
		self.root.after(
			delta,
			lambda: object.place(
				**kwargs
			)
		)

		#<_end of the function_>

	def pack_object(self, object, delta: int, **kwargs) -> None:
		'''
		Pack an object after some time delta using the properties
		specified under kwargs
		'''
		# --
		self.root.after(
			delta,
			lambda: object.pack(
				**kwargs
			)
		)

		#<_end of the function_>

	def remove_highlight(self, frame) -> None:
		''' Remove highlight from a frame which is not representing the actively playing song '''
		# --
		a_p = self.app.pub.app_theme

		try:
			# -- Unhighlight
			frame.config(bg=a_p['secondary_bg'])

			# -- Consider its children too
			for obj in frame.winfo_children():
				# --
				obj.config(bg=a_p['secondary_bg'])
				obj.config(fg=a_p['primary_text_colour'])

		except AttributeError:
			# -- Application may have just started (Nothing to remove highlight from)
			pass

		#<_end of the method_>

	def highlight_playing(self) -> None:
		''' Highlights the currently playing track on mini queue '''
		# -- Get frames
		frames = list(self.app.puc.track_frames_data.keys())
		frames.remove('active_frame')
		a_p = self.app.pub.app_theme

		# -- Consider index range
		try:
			# -- Get frame ID
			idx = self.app.pyr.track_index
			frame_id = frames[idx]
		except IndexError:
			# -- idx not in [0, 1, 2, 3, 4]. TRANSLATE track_index to one of 'em
			if (self.app.pyr.track_index % 5) == 0:
				# -- We are at the starting point of a group of 5
				idx = 0
				frame_id = frames[idx]
			else:
				# idx in a group of 5
				idx = 0
				check_pos = self.app.pyr.track_index

				while ((check_pos % 5) != 0):
					check_pos -=  1
					idx += 1

				frame_id  = frames[idx]

		frame_to_highlight = self.app.puc.track_frames_data[frame_id]

		# -- Highlight
		self.app.puc.on_click(
			event=None, object=frame_to_highlight,
			fg=a_p['frame_highlight_fg'], bg=a_p['frame_highlight_bg'],
			item_type='frame'
		)

		# -- mark as active
		self.app.puc.track_frames_data['active_frame'] = frame_id

		#<_end of the method_>

	def draw_wave_for_track(self, path, center: int = 30) -> None:
		''' Draw wave for song given the norm '''
		# --
		base = os.path.basename(path).replace('.mp3', '')

		# -- Get waveform data
		try:
			# --
			waveform_data = self.app.pda.player_data['tracks_data'][base]['waveform_data']
		except KeyError:
			# -- If generation in progress, skip
			if self.generating_data:
				return
				
			self.generating_data = True
			# -- Generate waveform data (Don't draw)
			from alma_music_player import thread_worker as t_w

			t_w(
				target=self.app.pyr.generate_waveform_data,
				arguments=(path,),
				daemon=False
			)

			return

		else:
			# -- Draw wave
			a_p = self.app.pub.app_theme

			def _draw(x_pos, norm) -> None:
				# --
				self.app.pub.waveform_canvas.create_line(
					x_pos, center - norm,
					x_pos, center + norm,
					fill=a_p['waveform_colour']
				)

				#<_end of inner function_>

			for x, norm in enumerate(waveform_data):
				# --
				_draw(x, norm)

		# --

		#<_end of the method_>

	def crossfade_images(self, label, new_img, steps: int = 5, delay: int = 13, size: tuple[int, int] = (210, 210)) -> None:
		''' morph-like behaviour between images '''
		# --
		old_img = ImageTk.getimage(label.image).convert('RGBA')

		# --
		try:
			# -- Incase current song has no artwork
			new_img = new_img.resize(size).convert('RGBA')
		except AttributeError:
			# -- Song has no artwork
			new_img = open_image_path(
				img_path=AlmaDataPaths.BG_DIR / 'alma_bgd.png'
			).resize(size).convert('RGBA')

		def _step(i: int) -> None:
			''' Blend old image with new '''
			if i > steps:
				# -- Crossfade complete
				return

			alpha = i / steps # -- alpha ranges between 0 ~ 1

			# -- blend old img with new
			blended_img = Image.blend(old_img, new_img, alpha)

			# -- set blended image as the current artwork
			set_image(
				label=label,
				img=None,
				size=None,
				blended_img=blended_img
			)

			# -- Repeat till crossfade is complete
			self.root.after(
				delay,
				lambda: _step(i + 1)
			)

			#<_end of inner function_>

		_step(0)

		#<_end of the method_>


#<_ END OF UIUPDATES>