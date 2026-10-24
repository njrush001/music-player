import os, json
from config import AlmaDataPaths

class PlaylistManager:
    def __init__(self, app):
        self.app = app
        self.playlists = {}
        self.playlist_dir = AlmaDataPaths.PLAYLIST_DIR

    def get_artist_music(self, args) -> None:
        ''' Get songs from the passed artist '''
        # --
        data_file = self.playlist_dir / 'artists_music.json'
        data = self.app.dbm.read_data(data_file)
        tracks = data.get(args[0], None)

        if not isinstance(tracks, list):
            raise KeyError('Tracks Unavailable: Could Not Fnd Tracks By That Artist')
        data = {}
        for p in tracks:
            base = os.path.basename(p)
            data[base.replace('.mp3', '')] = p
        self.app.clear_playlist_bags()
        self.app.pyr.track_index = 0
        self.app.select_tracks_to_add(data)
        args[1].destroy()

        #<_end of the method_>
    
    def load_users_playlist(self) -> dict:
        '''
        Opens the folder where playlists are saved and extracts
        important info.
        '''
        visualisation_data = {}
        for r, _, files in os.walk(self.playlist_dir):
            for f in files:
                data = self.app.dbm.read_data(self.playlist_dir / f)
                for name in data:
                    if len(data[name]) == 0:
                        # -- Empty playlist
                        continue

                    visualisation_data[name] = data[name]['total']

        return visualisation_data

        #<_end of the method_>
    
    def open_playlist(self, playlist_id: str) -> None:
        ''' Open the selected playlist '''
        pass

        #<_end of the method_>