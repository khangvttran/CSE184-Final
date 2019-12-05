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
columns = ['Artist', 'Album', 'Year', 'album_duration(ms)','number_of_tracks']
df = pd.DataFrame(columns=columns)
album_data = pd.read_csv('scraper/2005-2018top200albums.csv')
number = 0
for index, row in album_data.iterrows():
	# time.sleep(random.randint(1,10))
	album = row['Album']
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

	
	#if '(' in song:
	#	songspl = song.split('(')
	#	song = songspl[0]
	#if '\'' in song:
	#	song = song.replace('\'', '')
	
	try:
		results = sp.search(q='album:' + album + ' artist:' + artist, type='album')
		#print(results)
		album_id = results['albums']['items'][0]['id']
		#print(album + " by " + artist+ ", id: " + str(album_id))
		#number_of_tracks = len(results['tracks']['items'])
		songs = sp.album_tracks(album_id)
		song_count = 0
		album_duration = 0
		for song in songs['items']:
			song_count += 1
			album_duration += song['duration_ms']

		# data = {'Rank': [rank], 'Album': [album], 'Artist': [artist], 'Year': [year]}
		data = {'Artist': [artist], 'Album': [song], 'Year' : [year], 'album_duration(ms)': [album_duration], 'number_of_tracks' : [song_count] }
		dfRow = pd.DataFrame(data, columns=columns)
		df = pd.concat([df, dfRow], ignore_index=True)
		print(album + ' by ' + artist + ' added!')
	except:
		print(album + ' by ' + artist + 'Not found!')
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
df.to_csv('albumDataTop200ByYear.csv')