
import os, json
from config import AlmaDataPaths

class PlaylistManager:
    def __init__(self, app):
        self.app = app
        self.playlists = {}
        self.playlist_dir = AlmaDataPaths.PLAYLIST_DIR

    def load_playlist_manager(self) -> None:
        '''
        Calls the UI builder and configurer and shows
        user's created Playlist
        '''
        playlists_data: dict = self.load_users_playlist()

        self.app.ui.build_playlist_manager_ui()


        self.app.root.after(
            self.app.ui.build_time + 500,
            self.app.ui.playlist_name_ui,
            playlists_data
        )

        self.app.root.after(
            self.app.ui.build_time + 1000,
            self.app.pgc.configure_playlist_UI,
            self.app.pgc.playlist_manager_ui_data
        )

        #<_end of the method_>
    
    def load_users_playlist(self) -> dict:
        '''
        Opens the folder where playlists are saved and extracts
        important info.
        '''
        data = {}
        for r, _, files in os.walk(self.playlist_dir):
            for f in files:
                if f.lower().endswith('.json'):
                    with open(os.path.join(r, f), 'r') as file:
                        db_data = json.load(file)
                    
                    ID: str = db_data[0]
                    name: str = f.replace('.json', '').title()

                    total: int = len(db_data[1])
                    if total < 2:
                        total = '1 Song' if total == 1 else '-'
                    else:
                        total = f'{total} Songs'

                    data[ID] = {
                        'name': name,
                        'total': total
                    }

                    self.playlists[ID] = db_data[1]

                else:
                    os.remove(os.path.join(r, f))

        return data

        #<_end of the method_>
    
    def open_playlist(self, playlist_id: str) -> None:
        ''' Open the selected playlist '''
        # -- Supply paths
        paths = [p for p in self.playlists[playlist_id].values()]

        self.app.root.after(
            50,
            self.app.ui.playlist_items_ui,
            paths
        )

        #<_end of the method_>
    
    def close_playlist_manager(self) -> None:
        '''  Close the playlist UI then delete all data '''
        # -- Close the playlist UI
        self.app.ui.destroy_playlist_manager_ui()

        #<_end of the method_>