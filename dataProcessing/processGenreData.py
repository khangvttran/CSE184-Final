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
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)  #authenticate token
columns = ['Artist', 'Song', 'Duration(ms)', 'Year', 'Genre', 'danceability', 'energy', 'key', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'explicit', 'uri']
df = pd.DataFrame(columns=columns)
top100 = pd.read_csv('../data/topGenres.csv') #import csv
for index, row in top100.iterrows():
	# time.sleep(random.randint(1,10)) not needed bc spotify apparently doesnt care for requests of 10,000
	#get song, artist, year
	song = row['Song']
	artist = row['Artist']
	year = row['Year']
	genre = row['Genre']
	#parse strings to make searchable
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
	if '(' in song:
		songspl = song.split('(')
		song = songspl[0]
	if '\'' in song:
		song = song.replace('\'', '')
	#try catch for searching songs
	try:
		#songs are found
		results = sp.search(q='artist:' + artist + ' track:' + song, type='track') #spotify api to search
		id = results['tracks']['items'][0]['id'] #song is first result
		#get song data
		explicit = results['tracks']['items'][0]['explicit']
		audiofeat = sp.audio_features(id)
		duration = audiofeat[0]['duration_ms']
		danceability = audiofeat[0]['danceability']
		energy = audiofeat[0]['energy']
		loudness = audiofeat[0]['loudness']
		speechiness = audiofeat[0]['speechiness']
		acousticness = audiofeat[0]['acousticness']
		instrumentalness = audiofeat[0]['instrumentalness']
		liveness = audiofeat[0]['liveness']
		valence = audiofeat[0]['valence']
		tempo = audiofeat[0]['tempo']
		key = audiofeat[0]['key']
		uri = audiofeat[0]['uri']
		data = {'Artist': [artist], 'Song': [song], 'Duration(ms)' : [duration], 'Year': [year], 'Genre': [genre], 'danceability' : [danceability], 'energy' : [energy], 'key': [key], 'loudness': [loudness], 'speechiness': [speechiness], 'acousticness': [acousticness], 'instrumentalness': [instrumentalness], 'liveness': [liveness], 'valence': [valence], 'tempo': [tempo], 'explicit': [explicit], 'uri': [uri] }
		#append to dfrow
		dfRow = pd.DataFrame(data, columns=columns)
		df = pd.concat([df, dfRow], ignore_index=True) #append to dataframe
		print(song + ' by ' + artist + ' added!')
	except:
		print(song + ' by ' + artist + 'Not found!')
		continue
print(df)
df.to_csv('genreData.csv') #export as csv
