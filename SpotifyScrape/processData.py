import spotipy
import json
import pandas as pd
import time
import random
from spotipy.oauth2 import SpotifyClientCredentials

client_id = "9792c6bb2e6540acaaa115d2136fc9fd"
client_secret = "81fa55c01dd94bd1b8129c602f8eefb6"
client_credentials_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
#spotipy object to get spotify data
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 
columns = ['Artist', 'Song', 'Duration(ms)', 'Year', 'danceability', 'energy', 'key', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'uri']
df = pd.DataFrame(columns=columns)
top100 = pd.read_csv('2005-2018top100.csv')
number = 0
for index, row in top100.iterrows():
	# time.sleep(random.randint(1,10))
	song = row['Song']
	artist = row['Artist']
	year = row['Year']
	if 'Featuring' in artist:
		artistSpl = artist.split('Featuring')
		artist = artistSpl[0]
	# if '(' in artist:
	# 	artistSpl = artist.split('(')
	# 	artist = artistSpl[0]
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

	try:
		results = sp.search(q='artist:' + artist + ' track:' + song, type='track')
		id = results['tracks']['items'][0]['id']
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
		# data = {'Rank': [rank], 'Album': [album], 'Artist': [artist], 'Year': [year]}
		data = {'Artist': [artist], 'Song': [song], 'Duration(ms)' : [duration], 'Year': [year], 'danceability' : [danceability], 'energy' : [energy], 'key': [key], 'loudness': [loudness], 'speechiness': [speechiness], 'acousticness': [acousticness], 'instrumentalness': [instrumentalness], 'liveness': [liveness], 'valence': [valence], 'tempo': [tempo], 'uri': [uri] }
		dfRow = pd.DataFrame(data, columns=columns)
		df = pd.concat([df, dfRow], ignore_index=True)
		print(song + ' by ' + artist + ' added!')
	except:
		print(song + ' by ' + artist + 'Not found!')
		continue

	# try:
	# 	results = sp.search(q='artist:' + artist + 'track:' + song, type='track')
	# 	id = results['tracks']['items'][0]['id']
	# 	audiofeat = sp.audio_features(id)
	# 	duration = audiofeat[0]['duration_ms']
	# 	danceability = audiofeat[0]['danceability']
	# 	energy = audiofeat[0]['energy']
	# 	loudness = audiofeat[0]['loudness']
	# 	speechiness = audiofeat[0]['speechiness']
	# 	acousticness = audiofeat[0]['acousticness']
	# 	instrumentalness = audiofeat[0]['instrumentalness']
	# 	liveness = audiofeat[0]['liveness']
	# 	valence = audiofeat[0]['valence']
	# 	temp = audiofeat[0]['tempo']
	# 	# data = {'Rank': [rank], 'Album': [album], 'Artist': [artist], 'Year': [year]}
	# 	data = {'Artist': [artist], 'Song': [song], 'Duration(ms)' : [duration], 'Year': [year], 'danceability' : [danceability], 'energy' : [energy], 'key': [key], 'loudness': [loudness], 'speechiness': [speechiness], 'acousticness': [acousticness], 'instrumentalness': [instrumentalness], 'liveness': [liveness], 'valence': [valence], 'tempo': [tempo] }
	# 	dfRow = pd.DataFrame(data, columns=columns)
	# 	print(dfRow)
	# 	df = pd.concat([df, dfRow], ignore_index=True)
	# except:
	# 	print(results)
	# 	print(song)
	# 	print(artist)
	# 	continue
	# number += 1
	# if number == 25:
	# 	break
print(df)
df.to_csv('songDataTop100ByYearfixtest.csv')
