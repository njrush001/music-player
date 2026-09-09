# <============ IMPORTS ===============>
import os
import tkinter as tk
from typing import Callable
from PIL import Image, ImageTk
from config import AlmaDataPaths
from new_ui_updater import set_image
from alma_ui_configurer import on_seek
from new_ui_updater import clean_title
# <====================================>

# ========================================================================================================================
# ============================================ ALL DEPENDENCIES

def build_frame(parent, **kwargs) -> tk.Frame:
    '''
    Build a frame with the given properties.
    '''
    return tk.Frame(parent, **kwargs)

    #<_end of the function_>

def build_label(parent, **kwargs) -> tk.Label:
    '''
    Build a label with the given properties.
    '''
    return tk.Label(parent, **kwargs)

    #<_end of the function_>

def build_canvas(parent, **kwargs) -> tk.Canvas:
    '''
    Build a canvas with the given properties.
    '''
    return tk.Canvas(parent, **kwargs)

    #<_end of the function_>

def build_entry(parent, **kwargs) -> tk.Entry:
    '''
    Build a entry with the given properties.
    '''
    return tk.Entry(parent, **kwargs)

    #<_end of the function_>

# ========================================================================================================================
# ========================================================================================================================


class PlaylistManagerUI:
    ''' Builds The Playlist UI '''

    def build_playlist_manager_ui(self) -> None:
        ''' Build the UI when needed '''
        # -- Manager UI: Holds all the elements
        self.playlist_ui = build_frame(
            parent=self.root,
            bg='#1B1E33',
            width=1020, height=540
        )

        prompt = build_label(
            parent=self.playlist_ui,
            text='Loading ...',
            font=('Franklin Gothic Heavy', 20),
            fg='#FFFFFF', bg='#1B1E33'
        )
        prompt.pack(padx=50, pady=200)

        self.root.after(
            600,
            lambda: self.playlist_ui.place(
                x=0, y=0,
                width=1020,
                height=540
            )
        )

        # -- Create elements (1 sec delay)
        self.root.after(
            1000,
            self._playlist_manager_elements,
            self.playlist_ui
        )

        #<_end of the method_>
    
    def _playlist_manager_elements(self, win) -> None:
        ''' Build elements in the playlist manager ui '''
        # -- Canvas
        # -- Create Canvas (All UI elements will be shown here)
        self.main_canvas = build_canvas(
            parent=win, bg='#1B1E33',
            highlightthickness=0, bd=0
        )

        self.root.after(
            0,
            lambda: self.main_canvas.place(
                x=0, y=0,
                width=1020,
                height=540
            )
        )

        # -------------------------------------------------------------------------------------
        # ------------------------------      PARTION        ----------------------------------
        self.root.after(
            1000,
            lambda: self.main_canvas.create_line(
                0, 35, 1020, 35,
                fill='#353A4F'
            )
        )

        self.root.after(
            1500,
            lambda: self.main_canvas.create_line(
                270, 35, 270, 540,
                fill='#353A4F'
            )
        )

        self.root.after(
            2000,
            lambda: self.main_canvas.create_line(
                270, 55, 1020, 55,
                fill='#353A4F'
            )
        )

        self.root.after(
            2500,
            lambda: self.main_canvas.create_line(
                0, 480, 1020, 480,
                fill='#353A4F'
            )
        )

        self.root.after(
            3000,
            lambda: self.main_canvas.create_rectangle(
                12, 70, 257, 100,
                fill='#1B1E33',
                outline='#353A4F'
            )
        )

        self.root.after(
            3500,
            lambda: self.main_canvas.create_rectangle(
                300, 70, 995, 463,
                fill='#1B1E33',
                outline='#353A4F',
                dash=(4, 6)
            )
        )
        # -------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------

        # -- QUIT (helps to exit the playlist manager)
        quit_label = build_label(
            parent=self.main_canvas,
            text='CLOSE',
            font=('Franklin Gothic Heavy', 11),
            fg='#FFFFFF', bg='#1B1E33'
        )

        self.root.after(
            4000,
            lambda: quit_label.place(
                x=960, y=6
            )
        )

        # -- UI_ICON (image)
        ui_icon = build_label(
            parent=self.main_canvas,
            highlightthickness=0, bd=0
        )
        # -- Insert image
        set_image(
            label=ui_icon,                                 # -- where the icon will be displayed
            img=AlmaDataPaths.BG_DIR / 'player_icon.png',  # -- location of the icon
            size=(26, 26)                                  # -- the size to be displayed
        )

        self.root.after(
            4500,
            lambda: ui_icon.place(
                x=8,  y=6
            )
        )

        ui_title = build_label(
            parent=self.main_canvas,
            text='ALMA PLAYLIST MANAGER',
            font=('Franklin Gothic Heavy', 13),
            fg='#FFFFFF', bg='#1B1E33'
        )

        self.root.after(
            5000,
            lambda: ui_title.place(
                x=39, y=7
            )
        )

        section_title = build_label(
            parent=self.main_canvas,
            text='PLAYLIST', bg='#1B1E33',
            fg='#FFFFFF', font=('Franklin Gothic Heavy', 11)
        )

        self.root.after(
            5500,
            lambda: section_title.place(
                x=8,  y=40
            )
        )

        self.pst_search = build_entry(
            parent=self.main_canvas,
            width=32, bg='#1B1E33',
            fg='#FFFFFF', insertbackground='#FFFFFF',
            relief='flat', font=('Segoe UI', 10)
        )
    
        self.root.after(
            6000,
            lambda: self.pst_search.place(
                x=20,  y=76
            )
        )
        self.root.after(
            6500,
            lambda: self.pst_search.insert(
                0, '🔍 Search Playlists ...'
            )
        )

        # -------------------------------------------------------------------------------------
        # -----------------------------      ESSENTIALS      ----------------------------------

        # -- Base frame (hold the essentials in one place)
        base_frame = build_frame(
            parent=self.main_canvas,
            bg='#1B1E33'
        )

        self.root.after(
            7000,
            lambda: base_frame.place(
                x=12, y=490,
                width=245, height=40
            )
        )

        self.new_pst = build_label(
            parent=base_frame,
            text='➕', width=3,
            font=('Franklin Gothic Heavy', 18),
            fg='#FFFFFF', bg='#2A2B3D'
        )

        self.refresh = build_label(
            parent=base_frame,
            text='🔃', width=3,
            font=('Franklin Gothic Heavy', 18),
            fg='#FFFFFF', bg='#2A2B3D'
        )

        self.delete = build_label(
            parent=base_frame,
            text='🚮', width=3,
            font=('Franklin Gothic Heavy', 18),
            fg='#FFFFFF', bg='#2A2B3D'
        )

        self.edit = build_label(
            parent=base_frame,
            text='📝', width=3,
            font=('Franklin Gothic Heavy', 18),
            fg='#FFFFFF', bg='#2A2B3D'
        )


        self.pgc.playlist_manager_ui_data.update(
            {
                str(id(quit_label)): [
                    quit_label, {
                        'args': None,
                        'item_type': 'label',
                        'on_enter': 'red',
                        'on_leave': '#1B1E33',
                        'on_click': ('red', self.destroy_playlist_manager_ui)
                    }
                ],

                str(id(self.new_pst)): [
                    self.new_pst, {
                        'args': None,
                        'item_type': 'label',
                        'on_enter': 'green',
                        'on_leave': '#2A2B3D',
                        'on_click': ('#B973F4', None)
                    }
                ],

                str(id(self.refresh)): [
                    self.refresh, {
                        'args': None,
                        'item_type': 'label',
                        'on_enter': 'green',
                        'on_leave': '#2A2B3D',
                        'on_click': ('#B973F4', None)
                    }
                ],

                str(id(self.edit)): [
                    self.edit, {
                        'args': None,
                        'item_type': 'label',
                        'on_enter': 'green',
                        'on_leave': '#2A2B3D',
                        'on_click': ('#B973F4', None)
                    }
                ]
            }
        )

        # -- display the objects
        self.root.after(
            7500,
            lambda: self.new_pst.pack(
                side='left',
                padx=(15, 0)
            )
        )

        self.root.after(
            8000,
            lambda: self.refresh.pack(
                side='left',
                padx=(7, 0)
            )
        )

        self.root.after(
            8500,
            lambda: self.delete.pack(
                side='left',
                padx=(7, 0)
            )
        )

        self.root.after(
            9000,
            lambda: self.edit.pack(
                side='left',
                padx=(7, 0)
            )
        )

        # -------------------------------------------------------------------------------------
        # ----------------------------      DEFAULT VIEW     ----------------------------------
        default_view_frame = build_frame(
            parent=self.main_canvas,
            bg='#1B1E33'
        )

        self.root.after(
            9500,
            lambda: default_view_frame.place(
                x=480, y=178, width=340, height=182
            )
        )

        empty_icon = build_label(
            parent=default_view_frame,
            highlightthickness=0, bd=0,
            bg='#1E1E2E'
        )

        self.root.after(
            10000,
            lambda: empty_icon.place(
                x=110, y=2
            )
        )

        self.root.after(
            10500,
            lambda: set_image(
                label=empty_icon,                                 # -- where the icon will be displayed
                img=AlmaDataPaths.BG_DIR / 'empty_display.png',   # -- location of the icon
                size=(120, 114)                                   # -- the size to be displayed
            )
        )

        prompt_1 = build_label(
            parent=default_view_frame,
            text='Select Playlist',
            font=('Franklin Gothic Heavy', 11),
            fg='#B973F4', bg='#1B1E33'
        )
        
        self.root.after(
            11000,
            lambda: prompt_1.place(
                x=117, y=115
            )
        )

        text: str = 'Choose a playlist from the list or create a new one.'
        prompt_2 = build_label(
            parent=default_view_frame,
            text=text, font=('Franklin Gothic Heavy', 10),
            fg='#FFFFFF', bg='#1B1E33', wraplength=190,
            justify='center', anchor='n'
        )
        
        self.root.after(
            11500,
            lambda: prompt_2.place(
                x=45, y=140,
                width=250,
                height=40
            )
        )

        #<_end of the method_>
    
    def playlist_name_ui(self, playlist_data: dict) -> None:
        '''
        Create labels that will act as buttons.
        count: int -> represents the no. of labels to build.
        playlist_data: dict -> Gives the information to display
         about the playlist
            - data = {
                'name': name,
                'total': total
            }
        max_count: int -> Gives the max number of playlists that can
         be displayed on the window
        '''
        self.visible_frame = build_frame(
            parent=self.main_canvas,
            bg='#1B1E33'
        )
        
        self.visible_frame.place(
                x=12, y=110,
                width=247,
                height=362
            )

        # --
        count: int = len(playlist_data)
        max_count: int = 7

        def _build() -> None:
            ''' Create the actual labels '''
            nonlocal count
            # -- visible frame can hold max of 7 pst names
            if count > max_count:
                # --  Build the first seven
                count = 7

            for i, ID in enumerate(playlist_data, start=1):
                # -- Stop building when seven items are built
                if i <= count:
                    # -- Playlist buttons

                    frame = build_frame(
                        parent=self.visible_frame,
                        bg='#2A2B3D', width=240,
                        height=47
                    )

                    frame.pack(padx=(4, 0), pady=(4, 0), anchor='w')
                    frame.pack_propagate(False)

                    #colours = ['#4DD4AC', '#FF689D', '#7B61FF']

                    icon_label = build_label(
                        parent=frame,
                        text='🎵', width=2,
                        font=('Franklin Gothic Heavy', 18),
                        fg='#FFFFFF', bg='#2A2B3D', bd=0
                    )

                    icon_label.pack(padx=(7, 0), pady=2, side='left')

                    pst_name = build_label(
                        parent=frame,
                        text=playlist_data[ID]['name'],
                        font=('Franklin Gothic Heavy', 10),
                        fg='#FFFFFF', bg='#2A2B3D', bd=0
                    )

                    pst_name.pack(padx=(5, 0), pady=6, side='left', anchor='n')

                    total_songs = build_label(
                        parent=frame,
                        text=playlist_data[ID]['total'],
                        font=('Franklin Gothic Heavy', 6),
                        fg='#FFFFFF', bg='#2A2B3D', bd=0
                    )

                    total_songs.place(x=42, y=30)

                    self.pgc.playlist_manager_ui_data.update(
                        {
                            str(id(frame)): [
                                frame, {
                                    'args': ID,
                                    'item_type': 'frame',
                                    'on_enter': 'green',
                                    'on_leave': '#2A2B3D',
                                    'on_click': ('#B973F4', self.pmr.open_playlist)
                                }
                            ]
                        }
                    )

            #<_end of the function_>
        
        # --
        _build()

        #<_end of the method_>
    
    def playlist_items_ui(self, playlist_items: list, max_items=10) -> None:
        ''' UI for songs in playlist '''
        # -- Destroy frame if active
        try:
            # --
            self.playlist_items_frame.destroy()
        except Exception:
            # -- Frame not created
            pass

        # -- Create frame
        self.playlist_items_frame = build_frame(
            parent=self.main_canvas,
            bg='#1B1E33', highlightthickness=0,
            bd=0
        )

        self.playlist_items_frame.place(x=300, y=70, width=696, height=394)

        count: int = len(playlist_items)
        if count > 10:
            count = 10

        items = playlist_items[:count]

        for path in items:
            song_frame = build_frame(
                parent=self.playlist_items_frame,
                bg='#1B1E33', width=690, height=35
            )

            song_frame.pack(padx=(3, 0), pady=(4, 0), side='top', anchor='w')
            song_frame.pack_propagate(False)

            artwork_label = build_label(
                parent=song_frame,
                highlightthickness=0, bd=0
            )

            artwork_label.pack(side='left', padx=(5, 0))

            set_image(artwork_label, AlmaDataPaths.BG_DIR / 'alma_bgd.png', (30, 30))

            text: str = os.path.basename(path)
            song_name = build_label(
                parent=song_frame,
                text=text, font=('Calibri', 10),
                fg='#FFFFFF', bg='#1B1E33'
            )

            song_name.pack(padx=(5, 0), pady=(0, 0), side='top', anchor='w')

            text: str = 'Alan Walker'
            song_artist = build_label(
                parent=song_frame,
                text=text, font=('Calibri', 8),
                fg='#FFFFFF', bg='#1B1E33'
            )

            song_artist.place(x=40, y=18)

            length_label = build_label(
                parent=song_frame,
                text='00:03:45',
                font=('Calibri', 10),
                fg='#FFFFFF', bg='#1B1E33'
            )

            length_label = tk.Label()
            length_label.place(x=620, y=1)

        #<_end of the method_>
    
    def destroy_playlist_manager_ui(self) -> None:
        ''' Destroy playlist manager ui '''
        # -- Clear states
        self.pgc.playlist_manager_ui_data = {}

        # -- Destroy
        self.playlist_ui.destroy()

        #<_end of the method_>

class LastPlayedUI:
    ''' Create UI showing the last played song '''

    def build_last_played_ui(self, win: tk.Frame) -> None:
        '''Build the ui when needed '''
        # --
        self.lastp_frame: tk.Frame = build_frame(
            parent=win,
            bg='#0F111D',
            highlightthickness=0, bd=0
        )

        last_played_thumbnail: tk.Label = build_label(
            parent=self.lastp_frame,
            highlightthickness=0,
            bd=0
        )

        prompt: tk.Label = build_label(
            parent=self.lastp_frame,
            highlightthickness=0,
            bd=0, text='Continue?',
            font=('Franklin Gothic Heavy', 13),
            fg='#FFFFFF', bg='#0F111D'
        )

        s_n = 'Alan Walker Style x AVA - Not Alone (Official Music Video)'

        song_name: tk.Label = build_label(
            parent=self.lastp_frame,
            text=clean_title(path=s_n, max_lmt=35, max_show=33),
            font=('Tahoma', 9), highlightthickness=0,
            bd=0, fg='#4DD4AC', bg='#0F111D'
        )

        confirmation: tk.Label = build_label(
            parent=self.lastp_frame,
            text='▶', bg='#0F111D', bd=0,
            fg='#FFFFFF', highlightthickness=0,
            font=('Franklin Gothic Heavy', 27)
        )

        # -------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------
        # -- Placements

        self.root.after(
            10,
            lambda: set_image(
                label=last_played_thumbnail,
                img=AlmaDataPaths.BG_DIR / 'alma_bgd.png',
                size=(100, 100)
            )
        )

        self.root.after(
            20,
            lambda: last_played_thumbnail.pack(
                pady=(5, 0),
                side='top'
            )
        )

        self.root.after(
            30,
            lambda: prompt.pack(
                pady=(5, 0),
                side='top'
            )
        )

        self.root.after(
            40,
            lambda: song_name.place(
                x=2, y=135
            )
        )

        self.root.after(
            50,
            lambda: confirmation.place(
                x=90, y=155
            )
        )

        self.root.after(
            0,
            lambda: self.lastp_frame.place(
                x=2, y=200,
                width=211,
                height=214
            )
        )
        # -------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------

        # -- Data for configuration
        data = {
            str(id(confirmation)): [
                confirmation, {
                    'args': None,
                    'item_type': 'label',

                    'on_click': {
                        'fg': '#FFFFFF',
                        'bg': '#0F111D',
                        'command': self.app.puc.on_last_play_press
                    }
                }
            ]
        }

        # -- Configure
        self.root.after(
            70,
            self.app.puc.configure_frame_and_labels,
            data
        )

        #<_end of the method_>

class SettingsUI:
    ''' Build settings ui '''

    def build_settings_ui(self, configure_ui: Callable) -> None:
        ''' Build settings ui when needed '''
        # -- Configure UI
        configure_ui()

        #<_end of the method_>

    def destroy_settings_ui(self) -> None:
        ''' Destroy playlist manager ui '''
        pass

        #<_end of the method_>

class AudioDownloaderUI:
    ''' Build the YouTube Downloader UI '''
    def __init__(self) -> None:
        # --
        self.url_tab_active: bool = False
        self.search_tab_active: bool = False

        #<_end of the method_>

    def build_downloader_ui(self, win) -> None:
        ''' Build the downloader UI when called '''
        print("SERVICE POSTPONED!!")
        return
        
        # --
        self.yt_canvas = build_canvas(
            parent=win,
            bg='#0F111D',
            highlightthickness=0, bd=0
        )

        # --
        downloader_title = build_label(
            parent=self.yt_canvas,
            text='Download Music',
            font=('Franklin Gothic Heavy', 10),
            fg='#FFFFFF', bg='#0F111D'
        )

        url_tab = build_frame(
            parent=self.yt_canvas,
            bg='#4DD4AC', cursor='hand2'
        )

        url_label = build_label(
            parent=url_tab,
            cursor='hand2',
            text='🔗 From URL',
            fg='#0F111D', bg='#4DD4AC',
            font=('Tahoma', 8)
        )

        search_tab = build_frame(
            parent=self.yt_canvas,
            bg='#0F111D', cursor='hand2'
        )

        search_label = build_label(
            parent=search_tab,
            text='🔍 Search',
            cursor='hand2',
            fg='#FFFFFF', bg='#0F111D',
            font=('Tahoma', 8)
        )

        # -------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------
        # --- placements
        self.root.after(
            50,
            lambda: downloader_title.place(
                x=5, y=2
            )
        )

        self.root.after(
            100,
            lambda: self.yt_canvas.create_rectangle(
                5, 28, 788, 57,
                fill='#0F111D',
                outline='#353A4F'
            )
        )

        self.root.after(
            100,
            lambda: self.yt_canvas.create_rectangle(
                15, 32, 355, 52,
                fill='#0F111D',
                outline=''
            )
        )

        self.root.after(
            100,
            lambda: self.yt_canvas.create_rectangle(
                361, 32, 778, 52,
                fill='#0F111D',
                outline=''
            )
        )

        self.root.after(
            105,
            lambda: url_tab.place(
                x=17, y=34,
                width=336, height=17
            )
        )

        self.root.after(
            105,
            lambda: search_tab.place(
                x=363, y=34,
                width=413, height=17
            )
        )

        self.root.after(
            110,
            lambda: url_label.pack()
        )

        self.root.after(
            110,
            lambda: search_label.pack()
        )

        self.root.after(
            0,
            lambda: self.yt_canvas.place(
                x=0, y=0,
                width=793,
                height=223
            )
        )

        self.root.after(
            120,
            self.url_tab_contents,
            search_tab
        )

        # -------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------

        # -- Data Collection
        data = {}

        data.update(
            {
                str(id(url_tab)): [
                    url_tab, {
                        'args': search_tab,
                        'item_type': 'frame',

                        'on_click': {
                            'fg': '#0F111D',
                            'bg': '#4DD4AC',
                            'command': self.app.puc.on_url_tab_press
                        }
                    }
                ],
                str(id(search_tab)): [
                    search_tab, {
                        'args': url_tab,
                        'item_type': 'frame',

                        'on_click': {
                            'fg': '#0F111D',
                            'bg': '#4DD4AC',
                            'command': self.app.puc.on_search_tab_press
                        }
                    }
                ]
            }
        )

        # -- Configure
        self.app.puc.configure_frame_and_labels(data=data)

        #<_end of the method_>

    def url_tab_contents(self, search_tab , first_build: bool = True) -> None:
        '''
        Builds the contents that should appear under URL tab.
        It switches from search tab if startup is false.
        '''

        if self.url_tab_active:
            # -- user clicked url tab while it was active.
            return # --Nothing should happen
        # -- 
        elif first_build:
            # -- Implies hte UI was created for the first time
            pass
        else:
            # -- Switch from search tab

            # -- Change search tab item colours
            search_tab.config(bg='#0F111D')
            for obj in search_tab.winfo_children():
                obj.config(fg='#FFFFFF')
                obj.config(bg='#0F111D')

            self.search_tab_active = False
        # --
        try:
            # -- Assume this is not the first time build
            self.hint_a.config(text='Download From URL')

        except AttributeError:
            # -- Fist time build
            self.hint_a = build_label(
                parent=self.yt_canvas,
                text='Download From URL',
                font=('Franklin Gothic Heavy', 9),
                fg='#FFFFFF', bg='#0F111D'
            )

        try:
            # -- Assume this is not the first time build
            self.hint_b.config(text='Paste a Music URL from YouTube')

        except AttributeError:
            # -- Fist time build
            self.hint_b = build_label(
                parent=self.yt_canvas,
                text='Paste a Music URL from YouTube',
                font=('Tahoma', 8),
                fg='#FFFFFF', bg='#0F111D'
            )
        try:
            # --
            self.query_input.delete(0, 'end')
            self.query_input.insert('end', 'Paste URL Here ...')

        except AttributeError:
            # --
            self.query_input = build_entry(
                parent=self.yt_canvas,
                bg='#0F111D', fg='#FFFFFF',
                insertbackground='#FFFFFF',
                relief='flat', font=('Segoe UI', 11)
            )
            self.query_input.insert('end', 'Paste URL Here ...')

        try:
            # --
            self.execute_query.config(text='📥 Download')

        except AttributeError:
            # --
            self.execute_query = build_label(
                parent=self.yt_canvas,
                text='📥 Download',
                font=('Segoe UI', 10),
                width=14, cursor='hand2',
                fg='#0F111D', bg='#4DD4AC'
            )

        else:
            # -- Nice return point
            self.url_tab_active = True

            return # -- No need for placements

        recent = build_label(
            parent=self.yt_canvas,
            text='💱 Recent Downloads',
            font=('Franklin Gothic Heavy', 9),
            fg='#FFFFFF', bg='#0F111D'
        )

        # -- url tab active
        self.url_tab_active = True

        # -------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------
        # --- placements

        self.root.after(
            0,
            lambda: self.hint_a.place(
                x=5, y=62
            )
        )

        self.root.after(
            10,
            lambda: self.hint_b.place(
                x=5, y=83
            )
        )

        self.root.after(
            20,
            lambda: self.yt_canvas.create_rectangle(
                5, 105, 675, 134,
                fill='#0F111D',
                outline='#353A4F'
            )
        )

        self.root.after(
            30,
            lambda: self.query_input.place(
                x=7, y=109, width=666
            )
        )

        self.root.after(
            40,
            lambda: self.execute_query.place(
                x=682, y=105, height=29
            )
        )

        self.root.after(
            50,
            lambda: self.yt_canvas.create_line(
                268, 200, 524, 200,
                fill='#353A4F'
            )
        )

        self.root.after(
            40,
            lambda: recent.place(
                x=5, y=200
            )
        )

        # -------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------

        # -- Data collection for binding
        data = {
            str(id(self.execute_query)): [
                self.execute_query, {
                    'args': None,
                    'item_type': 'label',

                    'on_click': {
                        'fg': '#0F111D',
                        'bg': '#4DD4AC',
                        'command': self.app.puc.on_execute_query_press
                    }
                }
            ]
        }

        # -- Configure
        self.app.puc.configure_frame_and_labels(data=data)

        #<_end of the method_>

    def search_tab_contents(self, url_tab) -> None:
        '''
        Builds the contents that should appear under search tab.
        It switches from URL tab.
        '''
        if self.search_tab_active:
            # -- user clicked url tab while it was active.
            return # --Nothing should happen

        else:
            # -- Switch from URL tab

            # -- Change search tab item colours
            url_tab.config(bg='#0F111D')
            for obj in url_tab.winfo_children():
                obj.config(fg='#FFFFFF')
                obj.config(bg='#0F111D')

            self.url_tab_active = False

        # --
        self.hint_a.config(text='Search Your Song')
        self.hint_b.config(text='Enter Your Search Query Below')

        # --
        self.query_input.delete(0, 'end')
        self.query_input.insert('end', 'Input Search Query')

        # --
        self.execute_query.config(text='🔍 Search')

        # --
        self.search_tab_active =  True

        data = {
            str(id(self.execute_query)): [
                self.execute_query, {
                    'args': None,
                    'item_type': 'label',

                    'on_click': {
                        'fg': '#0F111D',
                        'bg': '#4DD4AC',
                        'command': self.app.puc.on_execute_query_press
                    }
                }
            ]
        }

        #<_end of the method_>

class MainUI:
    ''' Build Main UI (The interface user will interact with most) '''

    def build_main_ui(self) -> None:
        ''' Build Main UI On Startup '''
        # -- Main UI: Holds all the elements
        main_ui = build_frame(
            parent=self.root, bg='#1B1E33',
            width=1020, height=540
        )

        prompt = build_label(
            parent=main_ui,
            text='Hello, Lurk! Welcome Back.',
            font=('Franklin Gothic Heavy', 20),
            fg='#FFFFFF', bg='#1B1E33'
        )

        prompt.pack(padx=50, pady=230)

        self.root.after(
            0,
            lambda: main_ui.place(
                x=0, y=0,
                width=1020,
                height=540
            )
        )

        # -- Create elements (1 sec delay for welcome message)
        self.root.after(
            1000,
            self._main_elements,
            main_ui
        )

        #<_end of the method_>

    def _main_elements(self, win: tk.Frame) -> None:
        ''' Build elements in the main ui '''
        # -- Canvas
        # -- Create Canvas (All UI elements will be shown here)
        self.main_canvas = build_canvas(
            parent=win,
            bg='#1B1E33',
            highlightthickness=0, bd=0
        )

        live_feedback = build_frame(
            parent=self.main_canvas,
            bg='#0F111D'
        )

        app_info = build_frame(
            parent=self.main_canvas,
            bg='#0F111D'
        )

        ui_icon = build_label(
            parent=self.main_canvas,
            highlightthickness=0, bd=0
        )

        ui_title = build_label(
            parent=self.main_canvas,
            text='Lurk Alma',
            font=('Franklin Gothic Heavy', 9),
            fg='#4DD4AC', bg='#0F111D'
        )

        ui_title_b = build_label(
            parent=self.main_canvas,
            text='Music Player',
            font=('Bahnschrift SemiBold Condensed', 7),
            fg='#FFFFFF', bg='#0F111D'
        )

        navigation = build_frame(
            parent=self.main_canvas,
            bg='#0F111D'
        )

        home = build_frame(
            parent=self.main_canvas,
            bg='#1B1E33',
            cursor='hand2'
        )

        home_label = build_label(
            parent=home,
            text='🏠 Home', cursor='hand2',
            font=('Franklin Gothic Heavy', 8),
            fg='#FFFFFF', bg='#1B1E33'
        )

        playlist = build_frame(
            parent=self.main_canvas,
            bg='#1B1E33',
            cursor='hand2'
        )

        playlist_label = build_label(
            parent=playlist,
            text='📃 Playlist',
            font=('Franklin Gothic Heavy', 8),
            fg='#FFFFFF', bg='#1B1E33',
            cursor='hand2'
        )

        settings = build_frame(
            parent=self.main_canvas,
            bg='#1B1E33', cursor='hand2'
        )

        settings_label = build_label(
            parent=settings,
            text='⚙ Settings', cursor='hand2',
            font=('Franklin Gothic Heavy', 8),
            fg='#FFFFFF', bg='#1B1E33'
        )

        load_folder = build_frame(
            parent=self.main_canvas,
            bg='#1B1E33', cursor='hand2'
        )

        load_folder_label = build_label(
            parent=load_folder,
            text='📂 Load Music Folder',
            font=('Franklin Gothic Heavy', 8),
            fg='#FFFFFF', bg='#1B1E33',
            cursor='hand2'
        )

        yt_music = build_frame(
            parent=self.main_canvas,
            bg='#1B1E33', cursor='hand2'
        )

        yt_music_label = build_label(
            parent=yt_music,
            text='📥 Download Music',
            font=('Franklin Gothic Heavy', 8),
            fg='#FFFFFF', bg='#1B1E33',
            cursor='hand2'
        )

        recommendations = build_frame(
            parent=self.main_canvas,
            bg='#1B1E33', cursor='hand2'
        )

        recommendations_label = build_label(
            parent=recommendations,
            text='🗯 Suggested Music',
            font=('Franklin Gothic Heavy', 8),
            fg='#FFFFFF', bg='#1B1E33',
            cursor='hand2'
        )

        # --
        self.audio_info = build_frame(
            parent=self.main_canvas,
            bg='#0F111D'
        )

        self.audio_thumbnail = build_label(
            parent=self.audio_info,
            highlightthickness=0,
            bd=0,
            relief='raised'
        )

        song_name: str = 'Wake Me Up'
        artist_name: str = 'Alan Walker'
        file_type: str = 'MP3'

        self.song_title = build_label(
            parent=self.audio_info,
            text=song_name, highlightthickness=0,
            bd=0, bg='#0F111D', fg='#FFFFFF',
            font=('Tahoma', 18, 'bold')
        )

        self.artist = build_label(
            parent=self.audio_info,
            text=artist_name, highlightthickness=0,
            bd=0, bg='#0F111D', fg='#4DD4AC',
            font=('Tahoma', 12)
        )

        self.file_label = build_label(
            parent=self.audio_info,
            text=file_type, highlightthickness=0,
            bd=0, bg='#0F111D', fg='#AFABAB',
            font=('Tahoma', 10, 'bold')
        )

        self.queue_canvas = build_canvas(
            parent=self.main_canvas,
            bg='#0F111D', bd=0,
            highlightthickness=0
        )


        num_tab = build_label(
            parent=self.queue_canvas,
            text='#',
            font=('Tahoma', 7, 'bold'),
            bg='#0F111D', fg='#FFFFFF'
        )

        title_tab = build_label(
            parent=self.queue_canvas,
            text='TITLE',
            font=('Tahoma', 7, 'bold'),
            bg='#0F111D', fg='#FFFFFF'
        )

        artist_tab = build_label(
            parent=self.queue_canvas,
            text='ARTIST',
            font=('Tahoma', 7, 'bold'),
            bg='#0F111D', fg='#FFFFFF'
        )

        duration_tab = build_label(
            parent=self.queue_canvas,
            text='⌚',
            font=('Tahoma', 7, 'bold'),
            bg='#0F111D', fg='#FFFFFF'
        )

        # -- No Songs Added
        no_fd = build_label(
            parent=self.queue_canvas,
            text='-- No Folder Selected --',
            bg='#0F111D', fg='#FFFFFF',
            font=('Tahoma', 14, 'bold'),
            highlightthickness=0, bd=0
        )

        # -- Song Progress
        progress_frame = build_frame(
            parent=self.main_canvas,
            bg='#0F111D', bd=0,
            highlightthickness=0
        )

        self.sub_audio_thumbnail = build_label(
            parent=progress_frame,
            highlightthickness=0,
            bd=0
        )

        self.progress_canvas = build_canvas(
            parent=progress_frame,
            highlightthickness=0,
            bd=0, bg='#2E2E2E',
            cursor='hand2'
        )

        prev_btn = build_label(
            parent=progress_frame,
            font=('Franklin Gothic Heavy', 17),
            text='⏮', bg='#0F111D',
            fg='#FFFFFF', cursor='hand2',
            highlightthickness=0, bd=0
        )

        pause_btn = build_label(
            parent=progress_frame,
            font=('Franklin Gothic Heavy', 17),
            text='⏸', bg='#0F111D',
            fg='#FFFFFF', cursor='hand2',
            highlightthickness=0, bd=0
        )

        next_btn = build_label(
            parent=progress_frame,
            font=('Franklin Gothic Heavy', 17),
            text='⏭', bg='#0F111D',
            fg='#FFFFFF', cursor='hand2',
            highlightthickness=0, bd=0
        )

        # -- Get saved states for consistency
        shuffle_text: str = '🔀'
        if self.app.pda.player_data['shuffle_on']:
            # -- Shuffle mode was active
            shuffle_text = '🔃'

        shuffle_btn = build_label(
            parent=progress_frame,
            font=('Franklin Gothic Heavy', 10),
            text=shuffle_text, bg='#0F111D',
            fg='#FFFFFF', cursor='hand2',
            highlightthickness=0, bd=0
        )

        # -- Get saved states for consistency
        loop_text: str = '🔂'
        if self.app.pda.player_data['loop_on']:
            # -- Shuffle mode was active
            loop_text = '🔁'

        loop_btn = build_label(
            parent=progress_frame,
            font=('Franklin Gothic Heavy', 10),
            text=loop_text, bg='#0F111D',
            fg='#FFFFFF', cursor='hand2',
            highlightthickness=0, bd=0
        )

        time_elapsed = build_label(
            parent=progress_frame,
            font=('Franklin Gothic Heavy', 12),
            text='00:00:00', bg='#0F111D',
            fg='#FFFFFF',
            highlightthickness=0, bd=0
        )

        remaining_time = build_label(
            parent=progress_frame,
            font=('Franklin Gothic Heavy', 12),
            text='00:00:00', bg='#0F111D',
            fg='#FFFFFF',
            highlightthickness=0, bd=0
        )

        full_view_btn = build_label(
            parent=progress_frame,
            font=('Franklin Gothic Heavy', 11),
            text='🔱', bg='#0F111D',
            fg='#FFFFFF', cursor='hand2',
            highlightthickness=0, bd=0
        )

        self.volume_canvas = build_canvas(
            parent=progress_frame,
            highlightthickness=0,
            bd=0, bg='#2E2E2E',
            cursor='hand2'
        )

        # -- Get saved volume level
        vol: float = self.app.pda.player_data['volume_level']

        self.volume_level = build_label(
            parent=progress_frame,
            font=('Franklin Gothic Heavy', 11),
            text='Volume: ', bg='#0F111D',
            fg='#FFFFFF',
            highlightthickness=0, bd=0
        )

        # -------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------
        # --------------------------------------- PLACEMENTS ----------------------------------

        # -------------------------------------------------------------------------------------
        # -- Main canvas (all ui elements live on this parent)
        self.root.after(
            0,
            lambda: self.main_canvas.place(
                x=0, y=0,
                width=1020,
                height=540
            )
        )
        # -------------------------------------------------------------------------------------

        # -------------------------------------------------------------------------------------
        # -- Partition (divides main canvas into different sections)
        self.root.after(
            500,
            lambda: self.main_canvas.create_line(
                220, 0, 220, 472,
                fill='#353A4F'
            )
        )


        self.root.after(
            700,
            lambda: self.main_canvas.create_line(
                0, 472, 1020, 472,
                fill='#353A4F'
            )
        )

        self.root.after(
            900,
            lambda: self.main_canvas.create_line(
                0, 50, 220, 50,
                fill='#353A4F'
            )
        )

        self.root.after(
            1100,
            lambda: self.main_canvas.create_line(
                220, 20, 1020, 20,
                fill='#353A4F'
            )
        )

        self.root.after(
            1300,
            lambda: self.main_canvas.create_line(
                220, 250, 1020, 250,
                fill='#353A4F'
            )
        )
        # -------------------------------------------------------------------------------------

        # -------------------------------------------------------------------------------------
        # -- live feedback (where feedbaack to user will be displayed)
        self.root.after(
            1500,
            lambda: live_feedback.place(
                x=224, y=2,
                width=793, height=16
            )
        )
        # -------------------------------------------------------------------------------------

        # -------------------------------------------------------------------------------------
        # -- shows the app name + icon
        self.root.after(
            2000,
            lambda: app_info.place(
                x=2, y=3, width=215,
                height=45
            )
        )

        self.root.after(
            2750,
            lambda: set_image(
                label=ui_icon,                                 # -- where the icon will be displayed
                img=AlmaDataPaths.BG_DIR / 'player_icon.png',  # -- location of the icon
                size=(35, 35) 
            )
        )

        self.root.after(
            3000,
            lambda: ui_icon.place(
                x=8, y=6
            )
        )

        self.root.after(
            3000,
            lambda: ui_title.place(
                x=50, y=6
            )
        )

        self.root.after(
            3000,
            lambda: ui_title_b.place(
                x=50, y=25
            )
        )
        # -------------------------------------------------------------------------------------

        # -------------------------------------------------------------------------------------
        # -- navigation (where controls helping wiith navigation are shown)
        self.root.after(
            3250,
            lambda: navigation.place(
                x=2, y=53, width=215,
                height=416
            )
        )

        self.root.after(
            3300,
            lambda: home_label.pack(
                side='left', anchor='w',
                padx=5, pady=0)
        )

        self.root.after(
            3300,
            lambda: playlist_label.pack(
                side='left', anchor='w',
                padx=5, pady=0)
        )

        self.root.after(
            3300,
            lambda: settings_label.pack(
                side='left', anchor='w',
                padx=5, pady=0)
        )

        self.root.after(
            3300,
            lambda: load_folder_label.pack(
                side='left', anchor='w',
                padx=5, pady=0)
        )

        self.root.after(
            3300,
            lambda: yt_music_label.pack(
                side='left', anchor='w',
                padx=5, pady=0)
        )

        self.root.after(
            3300,
            lambda: recommendations_label.pack(
                side='left', anchor='w',
                padx=5, pady=0)
        )

        self.root.after(
            3500,
            lambda: home.place(
                x=5, y=60,
                width=210, height=25
            )
        )

        self.root.after(
            3500,
            lambda: playlist.place(
                x=5, y=90,
                width=210, height=25
            )
        )

        self.root.after(
            3500,
            lambda: settings.place(
                x=5, y=120,
                width=210, height=25
            )
        )

        self.root.after(
            3500,
            lambda: load_folder.place(
                x=5, y=150,
                width=210, height=25
            )
        )

        self.root.after(
            3500,
            lambda: yt_music.place(
                x=5, y=180,
                width=210, height=25
            )
        )

        self.root.after(
            3500,
            lambda: recommendations.place(
                x=5, y=210,
                width=210, height=25
            )
        )
        # -------------------------------------------------------------------------------------

        # -------------------------------------------------------------------------------------
        # -- current playing display (song name + artist + file type)
        self.root.after(
            3700,
            lambda: set_image(
                label=self.audio_thumbnail,
                img=AlmaDataPaths.BG_DIR / 'alma_bgd.png',
                size=(210, 210)
            )
        )

        self.root.after(
            3750,
            lambda: self.audio_thumbnail.place(
                x=10, y=5
            )
        )

        self.root.after(
            3750,
            lambda: self.song_title.place(
                x=230, y=40
            )
        )

        self.root.after(
            3750,
            lambda: self.artist.place(
                x=230, y=75
            )
        )

        self.root.after(
            3750,
            lambda: self.file_label.place(
                x=230, y=100
            )
        )

        self.root.after(
            4000,
            lambda: self.audio_info.place(
                x=224, y=24,
                width=793, height=223
            )
        )
        # -------------------------------------------------------------------------------------

        # -------------------------------------------------------------------------------------
        # -- queue (where queue of songs will be shown)
        self.root.after(
            4500,
            lambda: self.queue_canvas.place(
                x=224, y=254,
                width=793, height=216
            )
        )

        self.root.after(
            5000,
            lambda: self.queue_canvas.create_line(
                0, 25, 790, 25,
                fill='#353A4F'
            )
        )

        self.root.after(
            5150,
            lambda: num_tab.place(
                x=30, y=3
            )
        )

        self.root.after(
            5200,
            lambda: title_tab.place(
                x=90, y=3
            )
        )

        self.root.after(
            5250,
            lambda: artist_tab.place(
                x=470, y=3
            )
        )

        self.root.after(
            5350,
            lambda: duration_tab.place(
                x=650, y=3
            )
        )

        self.root.after(
            5500,
            lambda: no_fd.place(
                x=300, y=90
            )
        )
        # -------------------------------------------------------------------------------------

        # -------------------------------------------------------------------------------------
        # -- progress frame (song progress + volume and other playback conntrols)
        self.root.after(
            5650,
            lambda: set_image(
                label=self.sub_audio_thumbnail,
                img=AlmaDataPaths.BG_DIR / 'alma_bgd.png',
                size=(55, 55)
            )
        )

        self.root.after(
            5700,
            lambda: self.sub_audio_thumbnail.place(
                x=3, y=2
            )
        )

        self.root.after(
            5710,
            lambda: self.progress_canvas.place(
                x=170, y=15, width=700, height=5
            )
        )

        self.root.after(
            5750,
            lambda: prev_btn.place(
                x=445, y=27
            )
        )

        self.root.after(
            5800,
            lambda: pause_btn.place(
                x=495, y=27
            )
        )

        self.root.after(
            5830,
            lambda: next_btn.place(
                x=545, y=27
            )
        )

        self.root.after(
            5860,
            lambda: shuffle_btn.place(
                x=410, y=33
            )
        )

        self.root.after(
            5900,
            lambda: loop_btn.place(
                x=595, y=33
            )
        )

        self.root.after(
            5930,
            lambda: time_elapsed.place(
                x=195, y=33
            )
        )

        self.root.after(
            5960,
            lambda: remaining_time.place(
                x=780, y=33
            )
        )

        self.root.after(
            5990,
            lambda: full_view_btn.place(
                x=850, y=33
            )
        )

        self.root.after(
            6120,
            lambda: self.volume_canvas.place(
                x=885, y=23,
                width=120, height=5
            )
        )

        self.root.after(
            6135,
            lambda: self.show_volume_progress(
                x_0=0, x_1=(vol * self.volume_canvas.winfo_width()),
                y_0=0, y_1=self.volume_canvas.winfo_height()
            )
        )

        self.root.after(
            6150,
            lambda: self.volume_level.place(
                x=895, y=35
            )
        )

        self.root.after(
            6500,
            lambda: progress_frame.place(
                x=3, y=475,
                width=1015, height=60
            )
        )

        # -------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------


        # -------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------
        # ------------------------------------ DATA COLLECTION --------------------------------
        self.app.puc.main_ui_data.update(
            {
                str(id(home)): [
                    home, {
                        'args': None,
                        'item_type': 'frame',
                        'item_active': False,
                        'obj_id': str(id(home)),
                        'has_children': True,
                        
                        'on_enter': {
                            'fg': '#FFFFFF',
                            'bg': '#3E3F5E'
                        },
                        'on_leave': {
                            'fg': '#FFFFFF',
                            'bg': '#1B1E33'
                        },

                        'on_click': {
                            'fg': '#0F111D',
                            'bg': '#4DD4AC',
                            'command': self.app.puc.on_home_press
                        }
                    }
                ],
                str(id(playlist)): [
                    playlist, {
                        'args': None,
                        'item_type': 'frame',
                        'item_active': False,
                        'obj_id': str(id(playlist)),
                        'has_children': True,
                        
                        'on_enter': {
                            'fg': '#FFFFFF',
                            'bg': '#3E3F5E'
                        },
                        'on_leave': {
                            'fg': '#FFFFFF',
                            'bg': '#1B1E33'
                        },

                        'on_click': {
                            'fg': '#0F111D',
                            'bg': '#4DD4AC',
                            'command': self.app.puc.on_playlist_press
                        }
                    }
                ],
                str(id(settings)): [
                    settings, {
                        'args': None,
                        'item_type': 'frame',
                        'item_active': False,
                        'obj_id': str(id(settings)),
                        'has_children': True,
                        
                        'on_enter': {
                            'fg': '#FFFFFF',
                            'bg': '#3E3F5E'
                        },
                        'on_leave': {
                            'fg': '#FFFFFF',
                            'bg': '#1B1E33'
                        },

                        'on_click': {
                            'fg': '#0F111D',
                            'bg': '#4DD4AC',
                            'command': self.app.puc.on_settings_press
                        }
                    }
                ],
                str(id(load_folder)): [
                    load_folder, {
                        'args': None,
                        'item_type': 'frame',
                        'item_active': False,
                        'obj_id': str(id(load_folder)),
                        'has_children': True,
                        
                        'on_enter': {
                            'fg': '#FFFFFF',
                            'bg': '#3E3F5E'
                        },
                        'on_leave': {
                            'fg': '#FFFFFF',
                            'bg': '#1B1E33'
                        },

                        'on_click': {
                            'fg': '#0F111D',
                            'bg': '#4DD4AC',
                            'command': self.app.puc.on_load_folder_press
                        }
                    }
                ],
                str(id(yt_music)): [
                    yt_music, {
                        'args': self.audio_info,
                        'item_type': 'frame',
                        'item_active': False,
                        'obj_id': str(id(yt_music)),
                        'has_children': True,
                        
                        'on_enter': {
                            'fg': '#FFFFFF',
                            'bg': '#3E3F5E'
                        },
                        'on_leave': {
                            'fg': '#FFFFFF',
                            'bg': '#1B1E33'
                        },

                        'on_click': {
                            'fg': '#0F111D',
                            'bg': '#4DD4AC',
                            'command': self.app.puc.on_yt_music_press
                        }
                    }
                ],
                str(id(recommendations)): [
                    recommendations, {
                        'args': None,
                        'item_type': 'frame',
                        'item_active': False,
                        'obj_id': str(id(recommendations)),
                        'has_children': True,
                        
                        'on_enter': {
                            'fg': '#FFFFFF',
                            'bg': '#3E3F5E'
                        },
                        'on_leave': {
                            'fg': '#FFFFFF',
                            'bg': '#1B1E33'
                        },

                        'on_click': {
                            'fg': '#0F111D',
                            'bg': '#4DD4AC',
                            'command': self.app.puc.on_recommendations_press
                        }
                    }
                ],
                str(id(prev_btn)): [
                    prev_btn, {
                        'args': -1,
                        'item_type': 'label',

                        'on_click': {
                            'fg': '#FFFFFF',
                            'bg': '#0F111D',
                            'command': self.app.puc.on_prev_btn_press
                        }
                    }
                ],
                str(id(pause_btn)): [
                    pause_btn, {
                        'args': pause_btn,
                        'item_type': 'label',

                        'on_click': {
                            'fg': '#FFFFFF',
                            'bg': '#0F111D',
                            'command': self.app.puc.on_pause_btn_press
                        }
                    }
                ],
                str(id(next_btn)): [
                    next_btn, {
                        'args': 1,
                        'item_type': 'label',

                        'on_click': {
                            'fg': '#FFFFFF',
                            'bg': '#0F111D',
                            'command': self.app.puc.on_next_btn_press
                        }
                    }
                ],
                str(id(shuffle_btn)): [
                    shuffle_btn, {
                        'args': shuffle_btn,
                        'item_type': 'label',

                        'on_click': {
                            'fg': '#FFFFFF',
                            'bg': '#0F111D',
                            'command': self.app.puc.on_shuffle_btn_press
                        }
                    }
                ],
                str(id(loop_btn)): [
                    loop_btn, {
                        'args': loop_btn,
                        'item_type': 'label',

                        'on_click': {
                            'fg': '#FFFFFF',
                            'bg': '#0F111D',
                            'command': self.app.puc.on_loop_btn_press
                        }
                    }
                ],
                str(id(full_view_btn)): [
                    full_view_btn, {
                        'args': None,
                        'item_type': 'label',

                        'on_click': {
                            'fg': '#FFFFFF',
                            'bg': '#0F111D',
                            'command': lambda: print("I'll let you see full view!")
                        }
                    }
                ]
            }
        )
        
        canvas_data = {}
        canvas_data.update(
            {
                str(id(self.progress_canvas)): [
                    self.progress_canvas, {
                        'command': {
                            'on_click': self.app.puc.on_progress_canvas_click,
                            'on_drag': self.app.puc.on_progress_canvas_drag,
                            'on_release': self.app.puc.on_progress_canvas_release
                        }
                    }
                ],
                str(id(self.volume_canvas)): [
                    self.volume_canvas, {
                        'command': {
                            'on_click': self.app.puc.on_volume_canvas_click,
                            'on_drag': self.app.puc.on_volume_canvas_click,
                            'on_release': None
                        }
                    }
                ]
            }
        )
        # -------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------


        # -- CONFIGURE
        self.root.after(
            7000,
            on_seek,
            canvas_data
        )

        self.root.after(
            7500,
            self.app.puc.configure_frame_and_labels,
            self.app.puc.main_ui_data
        )

        # -- Show last played UI
        self.root.after(
            10000,
            self.build_last_played_ui,
            navigation
        )

        #<_end of the method_>

    def current_playing_display(self, song_artist: tuple[str, str], artwork) -> None:
        '''
        Shows the currently playing artwork,
        song name, artist and file type.
        '''

        # -- Destroy items in self.audio info
        for obj in self.audio_info.winfo_children():
            # --
            obj.destroy()

        # -- The artwork
        audio_thumbnail = build_label(
            parent=self.audio_info,
            highlightthickness=0,
            bd=0,
            relief='raised'
        )

        # -- file type (currently only mp3 files are allowed)
        file_type: str = 'MP3'

        # -- Song title
        song_title = build_label(
            parent=self.audio_info,
            text=song_artist[0], highlightthickness=0,
            bd=0, bg='#0F111D', fg='#FFFFFF',
            font=('Tahoma', 18, 'bold')
        )

        # -- artist name
        artist = build_label(
            parent=self.audio_info,
            text=song_artist[1], highlightthickness=0,
            bd=0, bg='#0F111D', fg='#4DD4AC',
            font=('Tahoma', 12)
        )

        # -- file type
        file_label = build_label(
            parent=self.audio_info,
            text=file_type, highlightthickness=0,
            bd=0, bg='#0F111D', fg='#AFABAB',
            font=('Tahoma', 10, 'bold')
        )

        # -------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------

        # -- Placements

        # -- current playing display (song name + artist + file type)
        self.root.after(
            100,
            lambda: set_image(
                label=audio_thumbnail,
                img=artwork,
                size=(210, 210)
            )
        )

        self.root.after(
            150,
            lambda: audio_thumbnail.place(
                x=10, y=5
            )
        )

        self.root.after(
            200,
            lambda: song_title.place(
                x=230, y=40
            )
        )

        self.root.after(
            250,
            lambda: artist.place(
                x=230, y=75
            )
        )

        self.root.after(
            300,
            lambda: file_label.place(
                x=230, y=100
            )
        )

        #<_end of the method_>

    def mini_queue(self, tracks: list, start_point: int = 0, max_show=72, max_lmt=72) -> None:
        '''
        Build the ui where tracks are displayed.
        '''
        # -- Destroy previous frame iif available
        try:
            # -- Destroy
            self.song_frame.destroy()
        except AttributeError:
            # -- First time build
            pass

        self.song_frame = build_frame(
            parent=self.queue_canvas,
            bg='#0F111D'
        )

        # ------------------------------------------------------------
        # ------------------------------------------------------------
        self.root.after(
            0,
            lambda: self.song_frame.place(
                x=10, y=30,
                width=770, height=179
            )
        )
        # ------------------------------------------------------------
        # ------------------------------------------------------------


        tracks = tracks[:5]

        # -- Clear everytime a new one is built
        data = {}
        self.app.puc.track_frames_data = {}

        for i, track in enumerate(tracks, start=start_point + 1):
            frame = build_frame(
                parent=self.song_frame,
                bg='#0F111D', width=765,
                height=32, cursor='hand2'
            )

            # -- Song Info
            artist: str = 'Arvy Natcht'
            time: str = '00:03:45'


            num_of_song = build_label(
                parent=frame,
                text=i, cursor='hand2',
                font=('Franklin Gothic Heavy', 6),
                fg='#FFFFFF', bg='#0F111D'
            ).place(x=28, y=8)

            song_name_label = build_label(
                parent=frame,
                text=track[:72], cursor='hand2',
                font=('Franklin Gothic Heavy', 6),
                fg='#FFFFFF', bg='#0F111D'
            ).place(x=85, y=8)

            artist_name_label = build_label(
                parent=frame,
                text=artist, cursor='hand2',
                font=('Franklin Gothic Heavy', 6),
                fg='#FFFFFF', bg='#0F111D'
            ).place(x=465, y=8)

            time_label = build_label(
                parent=frame,
                text=time, cursor='hand2',
                font=('Franklin Gothic Heavy', 6),
                fg='#FFFFFF', bg='#0F111D'
            ).place(x=645, y=8)

            frame.pack(padx=0, pady=(3, 0))

            # -- Collect This Frame Data
            obj_id: str = str(id(frame))

            data[obj_id] = [
                frame, {
                    'args': [i-1, frame],          # -- Should play track at this position
                    'item_type': 'frame',

                    'on_click': {
                        'fg': '#0F111D',
                        'bg': '#4DD4AC',
                        'command': self.app.puc.on_track_frame_click
                    }
                }
            ]

            self.app.puc.track_frames_data[obj_id] = frame

        # -- No active item
        self.app.puc.track_frames_data['active_frame'] = None

        # -- Configure data
        self.app.puc.configure_frame_and_labels(data)

        #<_end of the method_>

    def show_volume_progress(self, x_0: int, y_0: int, x_1: int, y_1: int) -> float:
        ''' Delete previous progress and create new one '''
        # --
        if x_1 < 0 or x_1 > self.volume_canvas.winfo_width():
            return
        
        # -- Draw
        try:
            # --
            self.volume_canvas.delete('volume_bar')
        except KeyError:
            # -- Previously not created
            pass

        # -- Create new bar
        self.volume_canvas.create_rectangle(
            x_0, y_0, x_1, y_1,
            fill='green', outline='',
            tags='volume_bar'
        )

        vol: float = x_1 / self.volume_canvas.winfo_width()
        vol_percent = str(round((vol * 100), 0)).split('.')[0]
        self.volume_level.config(text=f'Volume: {vol_percent}%')

        return vol

        #<_end of the method_>

    def show_song_progress(self, x_0: int, y_0: int, x_1: int, y_1: int) -> None:
        ''' Delete previous progress and create new one '''
        # --
        if x_1 < 0 or x_1 > self.progress_canvas.winfo_width():
            return
        # -- Draw
        try:
            # --
            self.progress_canvas.delete('progress_bar')
        except KeyError:
            # -- Previously not created
            pass

        # -- Create new bar
        self.progress_canvas.create_rectangle(
            x_0, y_0, x_1, y_1,
            fill='green', outline='',
            tags='progress_bar'
        )
        
        #<_end of the method_>

    def canvas_for_waveform(self) -> tk.Canvas:
        '''
        Return the canvas where waveform for current playing song
        will be drawn.
        '''
        self.waveform_canvas: tk.Canvas =  build_canvas(
            parent=self.audio_info,
            bg='green', highlightthickness=0,
            bd=0
        ).place(x=230, y=140, width=620, height=60)

        #<_end of the method_>

class ProgramUI(PlaylistManagerUI, LastPlayedUI, SettingsUI, AudioDownloaderUI, MainUI):
    def __init__(self, app) -> None:
        # ======================================================================================
        # ======================================================================================
        self.app = app
        self.root = tk.Tk()
        self.root.title('Lurk')                            # Window Name
        self.root.geometry('1020x540')                     # Width(1020 pixels) x height(540 pixels)
        self.root.resizable(False, False)                  # The window size should not be resizable
        self.root.configure(bg='black')                    # Background colour will be black
        # ======================================================================================
        # ======================================================================================

        super().__init__()
        #print(ProgramUI.__mro__)
        #print(self.__dict__)
        #return

        self.build_main_ui()

        #<_end of the method_>