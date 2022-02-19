"""

Creates a spotify OAuth cllient to fetch data from a users spotify account. Returns a csv file of user's complete playlist data.

Milo Barkow, Feburary 19th, 2022

"""

import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth, SpotifyPKCE
import pandas as pd

CLIENTID = os.environ['CLIENTID']                 # insert app client ID from spotify dashboard
redirect_uri = 'http://localhost:8888/callback'   # redurect uri - same as spotify dashboard
scope = 'playlist-read-private user-library-read' # scope of auththorization, can be changed

auth_PKCE = SpotifyPKCE(client_id=CLIENTID,
                        redirect_uri=redirect_uri,
                        scope=scope,
                        open_browser=True)

sp = spotipy.Spotify(requests_timeout=50, auth_manager=auth_PKCE)

data_dict = sp.current_user_playlists(offset=0, limit=50)

final = {}
playlist_list = []
song_dict = {}
max = 0
offset = 0

while offset < 200:
    data_dict = sp.current_user_playlists(offset=offset, limit=50)
    for playlist in data_dict['items']:
        song_list = []
        pid = playlist['id']
        body = sp.playlist(pid)
        name = body['name']
        print(name)
        track_count = body['tracks']['total']
        song_list.append(track_count)
        of = 0
        while of < 1000:
            playlist = sp.playlist_items(pid, offset=of)
            for song in playlist['items']:
                song_data = str(f"{song['track']['name']}\n")
                for artist in song['track']['artists']:
                    song_data = song_data + artist['name'] + ' '
                song_list.append(song_data)
            of += 100
        final[f'{name}'] = song_list
        if track_count > max:
            max = track_count
            of += 100
    offset += 50

print(max)
for key in final:
    while len(final[key]) < 912:
        final[key].append(' ')
final_csv = pd.DataFrame(final).to_csv('final.csv', index=False)

try:
    os.remove('.cache')
except OSError as e:
    print("Error: %s : %s" % ('.cache', e.strerror))
