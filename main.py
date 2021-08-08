import spotipy
from spotipy.oauth2 import SpotifyOAuth
from emailsender import send_email
import os

CLIENTID = '7a9404710e8b4fcea7f0e5634f000c96'
CLIENTSECRET = '9b35c0b6042147e898aec07ff46a2e0b'
redirect_uri = 'http://localhost:8888/callback'
scope = 'playlist-read-private user-library-read'

sp = spotipy.Spotify(requests_timeout=50, auth_manager=SpotifyOAuth(client_id=CLIENTID,
                                               client_secret=CLIENTSECRET,
                                               redirect_uri=redirect_uri,
                                               scope=scope))
master_list = []


def liked():
    global master_list
    offset = 0
    while offset < 10000:
        songs_dict = sp.current_user_saved_tracks(offset=offset, limit=50)
        song_list = songs_dict['items']

        for item in song_list:
            data = f"{item['track']['name']} ------- "
            for artist in item['track']['artists']:
                data = data + artist['name'] + ' '
            master_list.append(data)
        offset += 50


liked()

message = str(len(master_list)) + '\n'.join(master_list).encode('utf-8')

with open('list.txt', mode='a', encoding="utf-8") as file:
    for i in master_list:
        file.write(f'{i}\n')

send_email(my_email='milohbarkow@gmail.com', to_email='milohbarkow@gmail.com', password=os.getenv('PASSW'),
           message=message)
