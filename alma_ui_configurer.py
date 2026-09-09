# <============ IMPORTS ===============>
from tkinterdnd2 import DND_FILES
import new_player_engine
# <====================================>

thread_worker = None

# ========================================================================================================================
# ============================================ ALL DEPENDENCIES

def _on_click(func, obj) -> None:
    ''' Function to run whenever object is clicked '''
    # --
    obj.bind('<Button-1>', lambda e: func(e.x, obj))

    #<_end of the function_>

def _on_drag(func, obj) -> None:
    ''' Function to run whenever object is clicked '''
    # --
    obj.bind('<B1-Motion>', lambda e: func(e.x, obj))

    #<_end of the function_>

def _on_release(func, obj) -> None:
    ''' Function to run whenever object is clicked '''
    # --
    obj.bind('<ButtonRelease-1>', lambda e: func(e.x, obj))

    #<_end of the function_>

def on_seek(data: dict) -> None:
    ''' Seeking event '''
    # --
    for canvas_id in data:
        # -- Bind on click
        obj = data[canvas_id][0]
        func_on_click = data[canvas_id][1]['command']['on_click']
        func_on_drag = data[canvas_id][1]['command']['on_drag']
        func_on_release = data[canvas_id][1]['command']['on_release']

        _on_click(func_on_click, obj)
        _on_drag(func_on_drag, obj)

        # --
        if func_on_release is not None:
            # --
            _on_release(func_on_release, obj)

            #<_>
        
    #<_end of the function_>


# ========================================================================================================================
# ========================================================================================================================

class ProgramUIConfigurer():
    ''' Configures Elements In Main UI. Used to access configurers in the parent classes '''
    
    def __init__(self, app) -> None:
        global thread_worker
        # --
        self.app = app

        self.playlist_manager_ui_data = {}
        self.main_ui_data = {}
        self.track_frames_data = {}

        # --
        from alma_music_player import thread_worker as tw
        thread_worker = tw

        #<_end of the method_>

    def configure_frame_and_labels(self, data: dict) -> None:
        '''
        Defines what happens to created UI objects.
        '''
        for obj_id in data:
            # ----------------------------------------------------------
            # ----------------------------------------------------------

            try:
                self.bind_object_on_enter(
                    object=data[obj_id][0],                 # -- object where this event should occur
                    fg=data[obj_id][1]['on_enter']['fg'],  # -- text colour on the object on this event
                    bg=data[obj_id][1]['on_enter']['bg'],         # -- background colour of the object when the event occurs
                    item_type=data[obj_id][1]['item_type']  # -- indicates if the object contains some objects inside it
                )
            except KeyError:
                pass

            # -- On leave
            try:
                self.bind_object_on_leave(
                    object=data[obj_id][0],                 # -- object where this event should occur
                    fg=data[obj_id][1]['on_leave']['fg'],   # -- text colour on the object on this event
                    bg=data[obj_id][1]['on_leave']['bg'],   # -- background colour of the object when the event occurs
                    item_type=data[obj_id][1]['item_type']  # -- indicates if the object contains some objects inside it
                )
            except KeyError:
                pass

            # -- On click
            self.bind_object_on_click(

                object=data[obj_id][0],                  # -- object where this event should occur
                fg=data[obj_id][1]['on_click']['fg'],    # -- text colour on the object on this event
                bg=data[obj_id][1]['on_click']['bg'],    # -- background colour of the object when the event occurs
                item_type=data[obj_id][1]['item_type'],  # -- indicates if the object contains some objects inside it
                command=data[obj_id][1]['on_click']['command'],  # -- what should happen on clicking this object
                args=data[obj_id][1]['args']             # -- arguments passed to the command
            )
            # ----------------------------------------------------------
            # ----------------------------------------------------------


            if data[obj_id][1]['item_type'] == 'frame':
                #include objects in the frame
                for obj in data[obj_id][0].winfo_children():
                    # -- On hover
                    try:
                        self.bind_object_on_enter(
                            object=obj,                            # -- object where this event should occur
                            fg=data[obj_id][1]['on_enter']['fg'],  # -- text colour on the object on this event
                            bg=data[obj_id][1]['on_enter']['bg'],  # -- background colour of the object when the event occurs
                            item_type='',                    # -- indicates if the object contains some objects inside it
                            parent=data[obj_id][0]           # -- background colour of the object when the event occurs
                        )
                    except KeyError:
                        pass

                    # -- On leave
                    try:
                        self.bind_object_on_leave(
                            object=obj,                      # -- object where this event should occur
                            fg=data[obj_id][1]['on_leave']['fg'],  # -- text colour on the object on this event
                            bg=data[obj_id][1]['on_leave']['bg'],  # -- background colour of the object when the event occurs
                            item_type='',                    # -- indicates if the object contains some objects inside it
                            parent=data[obj_id][0]           # -- helps to configure other objects that are insiide the same parent
                        )
                    except KeyError:
                        pass

                    # -- On click
                    self.bind_object_on_click(
                        object=obj,                              # -- object where this event should occur
                        fg=data[obj_id][1]['on_click']['fg'],    # -- text colour on the object on this event
                        bg=data[obj_id][1]['on_click']['bg'],       # -- background colour of the object when the event occurs
                        item_type='',                            # -- indicates if the object contains some objects inside it
                        parent=data[obj_id][0],                  # -- helps to configure other objects that are insiide the same parent
                        command=data[obj_id][1]['on_click']['command'],  # -- what should happen on clicking this object
                        args=data[obj_id][1]['args']             # -- arguments passed to the command
                    )

        #<_end of the function_>

    def bind_object_on_enter(self, object, fg: str, bg: str, item_type: str, parent=None, command=None, args=None) -> None:
        ''' Defines what happens to the object on enter '''
        object.bind(
            '<Enter>',
            lambda e: self.on_enter(
                event=e,                 # --
                object=object,           # -- object where this event should occur
                fg=fg,                   # -- text colour on the object on this event
                bg=bg,                   # -- background colour of the object when the event occurs
                item_type=item_type,     # -- indicates if the object contains some objects inside it
                parent=parent,           # -- helps to configure other objects that are insiide the same parent
                command=command,         # -- what should happen on clicking this object
                args=args                # -- arguments passed to the command
            )
        )

        #<_end of the function_>

    def bind_object_on_leave(self, object, fg: str, bg: str, item_type: str, parent=None, command=None, args=None) -> None:
        ''' Defines what happens to the object on leave '''
        # --
        object.bind(
            '<Leave>',
            lambda e: self.on_leave(
                event=e,                 # --
                object=object,           # -- object where this event should occur
                fg=fg,                   # -- text colour on the object on this event
                bg=bg,                   # -- background colour of the object when the event occurs
                item_type=item_type,     # -- indicates if the object contains some objects inside it
                parent=parent,           # -- helps to configure other objects that are insiide the same parent
                command=command,         # -- what should happen on clicking this object
                args=args                # -- arguments passed to the command
            )
        )

        #<_end of the function_>

    def bind_object_on_click(self, object, fg: str, bg: str, item_type: str, parent=None, command=None, args=None) -> None:
        ''' Defines what happens to the object on leave '''
        object.bind(
            '<Button-1>',
            lambda e: self.on_click(
                event=e,                 # --
                object=object,           # -- object where this event should occur
                fg=fg,                   # -- text colour on the object on this event
                bg=bg,                   # -- background colour of the object when the event occurs
                item_type=item_type,     # -- indicates if the object contains some objects inside it
                parent=parent,           # -- helps to configure other objects that are insiide the same parent
                command=command,         # -- what should happen on clicking this object
                args=args                # -- arguments passed to the command
            )
        )

        #<_end of the function_>

    def on_enter(self, event, fg: str, object, bg: str, item_type: str, parent=None, command=None, args=None) -> None:
        '''
        Defines what happens when the user hovers on an object
        object     ->
        bg         -> represents the background colour of the object on_leave
        item_type  -> frame or label, tells us when to configure items within the frame too
        parent     -> if item_type is label and lives within a frame..the frame is passsed
                    It helps us apply effects to other frame's components
        '''
        # --
        object.config(bg=bg)

        if item_type == 'frame':
            for obj in object.winfo_children():
                obj.config(bg=bg)
                obj.config(fg=fg)

        if parent is not None:
            for obj in parent.winfo_children():
                obj.config(bg=bg)
                obj.config(fg=fg)
            parent.config(bg=bg)

        #<_end of the function_>

    def on_leave(self, event, fg: str, object, bg: str, item_type: str, parent=None, command=None, args=None) -> None:
        '''
        On hover then leave, this function define what happens to the object
        object     ->
        bg         -> represents the background colour of the object on_leave
        item_type  -> frame or label, tells us when to configure items within the frame too
        parent     -> if item_type is label and lives within a frame..the frame is passsed
                    It helps us apply effects to other frame's components
        '''
        # --
        object.config(bg=bg)

        if item_type == 'frame':
            for obj in object.winfo_children():
                obj.config(bg=bg)
                obj.config(fg=fg)

        if parent is not None:
            for obj in parent.winfo_children():
                obj.config(bg=bg)
                obj.config(fg=fg)
            parent.config(bg=bg)

        #<_end of the function_>

    def on_click(self, event, object, fg: str, bg: str, item_type: str, parent=None, command=None, args=None) -> None:
        '''
        Called when an object is clicked.
        object     ->
        bg         -> represents the background colour of the object on_leave
        item_type  -> frame or label, tells us when to configure items within the frame too
        parent     -> if item_type is label and lives within a frame..the frame is passsed
                    It helps us apply effects to other frame's components
        '''
        # --
        # --
        object.config(bg=bg)

        if item_type == 'frame':
            for obj in object.winfo_children():
                obj.config(bg=bg)
                obj.config(fg=fg)

        if parent is not None:
            for obj in parent.winfo_children():
                obj.config(bg=bg)
                obj.config(fg=fg)
            parent.config(bg=bg)

        if command is not None:
            try:
                command(args)
            except Exception:
                command()

        #<_end of the function_>

    def unhighlight_inactive_frame(self, frame) -> None:
        ''' Unhighlight '''
        # -- Unhighlight the previous active frame
        try:
            # -- Unhighlight
            frame.config(bg='#0F111D')

            # -- Unhighlight its object too
            for obj in frame.winfo_children():
                # --
                obj.config(bg='#0F111D')
                obj.config(fg='#FFFFFF')

        except AttributeError:
            # -- Application just started
            pass

        #<_end of the method_>

    def on_home_press(self) -> None:
        print('I will show you home UI')

        #<_end of the method_>

    def on_playlist_press(self) -> None:
        print('I will show you playlist ui')

        #<_end of the method_>

    def on_settings_press(self) -> None:
        print('I will show you settings ui')

        #<_end of the method_>

    def on_load_folder_press(self) -> None:
        '''
        Allow User to select folder with his music
        '''
        # --
        thread_worker(
            target=self.app.lib.get_music_from_folder,
            arguments=(None,),
            daemon=True
        )
        #<_end of the method_>

    def on_yt_music_press(self, win) -> None:
        ''' Downloader UI should be built '''
        # --
        self.app.pub.build_downloader_ui(win)

        #<_end of the method_>

    def on_recommendations_press(self) -> None:
        print('I will play your recommendations')

        #<_end of the method_>

    def on_track_frame_click(self, args) -> None:
        '''
        What happens when you click a frame that should
        trigger playback.
        '''
        # -- Unhighlight
        try:
            # --
            self.unhighlight_inactive_frame(
                frame=self.track_frames_data[self.track_frames_data['active_frame']]
            )
        except KeyError:
            # --
            pass

        self.track_frames_data['active_frame'] = str(id(args[1]))
        
        # --
        self.app.pub.root.after(
            0,
            lambda: self.app.pyr.initialise(
                build_mini_queue=False,
                track_index=args[0],
                build_data=[[], 0]
            )
        )

        #<_end of the method_>

    def on_next_btn_press(self, hint: int) -> None:
        ''' Play next song '''
        # --
        thread_worker(
            target=self.app.pyr.next_playable,
            arguments=(hint,),
            daemon=True
        )

        #<_end of the method_>

    def on_prev_btn_press(self, hint: int) -> None:
        ''' Play next song '''
        # --
        thread_worker(
            target=self.app.pyr.next_playable,
            arguments=(hint,),
            daemon=True
        )

    def on_pause_btn_press(self, btn) -> None:
        ''' Trigger pausing or unpausing of a track'''
        #  -- Check state
        if self.app.pyr.track_paused:
            # -- Indicate target
            func = self.app.pyr.resume_track

        else:
            func = self.app.pyr.pause_track

        # -- Work in a thread
        thread_worker(
            target=func,
            arguments=(btn,),
            daemon=True
        )

        #<_end of the method_>

    def on_loop_btn_press(self, loop_btn) -> None:
        ''' Toggle between loop all and one '''
        # -- Thread worker
        thread_worker(
            target=self.app.toggle_loop,
            arguments=(loop_btn,),
            daemon=True
        )

        #<_end of the method_>

    def on_shuffle_btn_press(self, shuffle_btn) -> None:
        ''' Toggle shuffle mode off or on '''
        # -- Thread worker
        thread_worker(
            target=self.app.toggle_shuffle,
            arguments=(shuffle_btn,),
            daemon=True
        )

        #<_end of the method_>

    def on_url_tab_press(self, search_tab) -> None:
        ''' Switch Between tabs and unhighlight the passed tab if necessary'''
        # -- Build the URL tab contents
        self.app.pub.url_tab_contents(search_tab, first_build=False)

        #<_end of the method_>

    def on_search_tab_press(self, url_tab) -> None:
        ''' Switch Between tabs and unhighlight the passed tab if necessary'''
        # -- Build the search tab contents
        self.app.pub.search_tab_contents(url_tab)

        #<_end of the method_>

    def on_execute_query_press(self) -> None:
        ''' Search or download song at given URL '''
        print("I'll search or Download the query you pass")

        #<_end of the method_>

    def on_last_play_press(self) -> None:
        ''' Continue ewith last playback '''
        print('Last played song shall bee played!')

        #<_end of the method_>


    def on_volume_canvas_click(self, set_point, volume_canvas) -> None:
        ''' Search or download song at given URL '''
        # -- Draw
        vol: float = self.app.pub.show_volume_progress(
            x_0=0, x_1=set_point,
            y_0=0, y_1=volume_canvas.winfo_height()
        )

        # --
        if vol is None:
            return

            #<_>

        self.app.pyr.set_volume(vol)

        #<_end of the method_>

    def on_progress_canvas_click(self, set_point, progress_canvas) -> None:
        ''' Search or download song at given URL '''
        # -- Draw
        self.app.pub.show_song_progress(
            x_0=0, x_1=set_point,
            y_0=0, y_1=progress_canvas.winfo_height()
        )

        #<_end of the method_>

    def on_progress_canvas_drag(self, set_point, progress_canvas) -> None:
        ''' Search or download song at given URL '''
        # -- Draw
        self.app.pub.show_song_progress(
            x_0=0, x_1=set_point,
            y_0=0, y_1=progress_canvas.winfo_height()
        )
        # -- user dragging
        self.pyr.user_seeking = True

        #<_end of the method_>

    def on_progress_canvas_release(self, set_point, progress_canvas) -> None:
        ''' Trigger playback from position '''
        # -- not dragging
        self.pyr.user_seeking = False

        # -- ratio seeked
        ratio: float = (set_point / progress_canvas.winfo_width())

        # -- trigger playback
        new_player_engine.play_song(start=(ratio * self.app.pyr.track_duration))

        #<_end of the method_>