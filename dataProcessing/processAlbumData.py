import spotipy
import json
import pandas as pd
import time
import random
from spotipy.oauth2 import SpotifyClientCredentials

client_id = ""
client_secret = ""
client_credentials_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
#spotipy object to get spotify data
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 
columns = ['Artist', 'Album', 'Year', 'album_duration(ms)','number_of_tracks']
df = pd.DataFrame(columns=columns)
album_data = pd.read_csv('../data/2005-2018top200albums.csv')
number = 0
#For every song:
for index, row in album_data.iterrows():
	# time.sleep(random.randint(1,10))
	album = row['Album']
	artist = row['Artist']
	year = row['Year']
	# parse artist string to fit with search API
	if 'Featuring' in artist:
		artistSpl = artist.split('Featuring')
		artist = artistSpl[0]
	if '&' in artist:
		artistSpl = artist.split('&')
		artist = artistSpl[0]
	if '$' in artist:
		artist = artist.replace('$', 's')
	if '\'' in artist:
		artist = artist.replace('\'', '')
	# Search for each album
	try:
		# get the album
		results = sp.search(q='album:' + album + ' artist:' + artist, type='album')
		# get album 'id' from metadata
		album_id = results['albums']['items'][0]['id']
		# get array of tracks (wrapped in 'paging object')
		songs = sp.album_tracks(album_id)
		song_count = 0
		album_duration = 0
		# every 'simplified' track object in 'paging object'
		for song in songs['items']:
			song_count += 1
			album_duration += song['duration_ms']
		# record all data in dictionary
		data = {'Artist': [artist], 'Album': [album], 'Year' : [year], 'album_duration(ms)': [album_duration], 'number_of_tracks' : [song_count] }
		# concatenate data in df
		dfRow = pd.DataFrame(data, columns=columns)
		df = pd.concat([df, dfRow], ignore_index=True)
		print(album + ' by ' + artist + ' added!')
	except:
		# if album not found
		print(album + ' by ' + artist + ' Not found!')
		continue

print(df)
df.to_csv('albumDataTop200ByYear.csv')