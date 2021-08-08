import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

CLIENTID = '7a9404710e8b4fcea7f0e5634f000c96'
CLIENTSECRET = '9b35c0b6042147e898aec07ff46a2e0b'
redirect_uri = 'http://localhost:8888/callback'
scope = 'playlist-read-private user-library-read'

sp = spotipy.Spotify(requests_timeout=50, auth_manager=SpotifyOAuth(client_id=CLIENTID,
                                                                    client_secret=CLIENTSECRET,
                                                                    redirect_uri=redirect_uri,
                                                                    scope=scope))

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

# scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
#          "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
#
# credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
# client = gspread.authorize(credentials)
#
# spreadsheet = client.open('CSV-to-Google-Sheet')
#
# with open('final.csv', 'r') as file:
#     content = file.read()
#     client.import_csv(spreadsheet.id, data=content)
