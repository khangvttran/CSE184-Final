# Module for getting duration of song from Spotify
# getDuration accepts three strings, the artist, the album, and the song
# returns the duration of the passed song in ms.  Returns 'None' if song is not found
# significant inspiration taken from this article: 	
# https://medium.com/@RareLoot/extracting-spotify-data-on-your-favourite-artist-via-python-d58bc92a4330

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def getDuration(art, albm, sng):
	client_id = "9792c6bb2e6540acaaa115d2136fc9fd"
	client_secret = "81fa55c01dd94bd1b8129c602f8eefb6"
	client_credentials_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
	#spotipy object to get spotify data
	sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 

	#All strings:
	artist = art
	album = albm
	song = sng

	#get artist metadata
	artist_data = sp.search(artist)
	
	##TODO: Error handling if artist is not found
	#uri of artist
	artist_uri = artist_data['tracks']['items'][0]['artists'][0]['uri']
	#list of (simplified) album objects
	sp_albums = sp.artist_albums(artist_uri)
	#the album we're looking for
	the_album = None
	#search for album in list of objects
	for album_Obj in sp_albums['items']:
		if album_Obj['name'] == album:
			the_album = album_Obj
			#print(the_album['name'])
			break
	if the_album == None:
		#return None if albums is not found
		return None
	#get the (full) album object using uri from (simplified) object
	the_album_full = sp.album(the_album['uri'])
	#match string of passed song with name of song inside paging object containing album object
	for track in the_album_full['tracks']['items']:
		if track['name'] == song:
			return track['duration_ms']
	return None


def getDurationWithoutAlbum(art, sng):
	try:
		client_id = "9792c6bb2e6540acaaa115d2136fc9fd"
		client_secret = "81fa55c01dd94bd1b8129c602f8eefb6"
		client_credentials_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
		#spotipy object to get spotify data
		sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 

		#All strings:
		artist = art
		song = sng

		#get artist metadata
		artist_data = sp.search(artist)
		
		##TODO: Error handling if artist is not found
		#uri of artist
		artist_uri = artist_data['tracks']['items'][0]['artists'][0]['uri']
		#list of (simplified) album objects
		sp_albums = sp.artist_albums(artist_uri)
		#the album we're currently iterating through
		the_album = None
		the_track = None
		#search for song in list of (full) album objects
		for album_Obj in sp_albums['items']:
			#grab full album obj to search for list of songs
			the_album = sp.album(album_Obj['uri'])
			#check each song on each album to see if it's a match
			for track in the_album['tracks']['items']:
				if track['name'] == song:
					the_track = track
					break
			if the_track != None:
				break
					#return (dict({"album" : str(the_album['name']), "duration" : track['duration_ms']}))
		#return (dict({"album" : None, "duration" : None}))
		if the_track == None:
			return {'Song' : sng, 'Artist' : art, 'Album' : None, 'Duration(ms)' : None, 'Key' : None, 'Modality' : None, 'Time Signature' : None, 'Acousticness' : None, 'Danceability' : None, 'Energy' : None, 'Instrumentalness' : None, 'Liveness' : None,  'Loudness' : None, 'Speechiness' : None, 'Valence' : None, 'Tempo' : None}
		features = sp.audio_features(the_track['id'])
		feat_dict = {}
		#NEW
		feat_dict.update({"Song" : song})
		feat_dict.update({"Artist" : artist})

		feat_dict.update({"Album" : the_album['name']})
		feat_dict.update({"Duration(ms)" : features[0]['duration_ms']})
		feat_dict.update({"Key" : features[0]['key']})
		feat_dict.update({"Modality" : features[0]['mode']})
		feat_dict.update({"Time Signature" : features[0]['time_signature']})
		feat_dict.update({"Acousticness" : features[0]['acousticness']})
		feat_dict.update({"Danceability" : features[0]['danceability']})
		feat_dict.update({"Energy" : features[0]['energy']})
		feat_dict.update({"Instrumentalness" : features[0]['instrumentalness']})
		feat_dict.update({"Liveness" : features[0]['liveness']})
		feat_dict.update({"Loudness" : features[0]['loudness']})
		feat_dict.update({"Speechiness" : features[0]['speechiness']})
		feat_dict.update({"Valence" : features[0]['valence']})
		feat_dict.update({"Tempo" : features[0]['tempo']})
		
		return feat_dict
	except:
		return {'Song' : sng, 'Artist' : art, 'Album' : None, 'Duration(ms)' : None, 'Key' : None, 'Modality' : None, 'Time Signature' : None, 'Acousticness' : None, 'Danceability' : None, 'Energy' : None, 'Instrumentalness' : None, 'Liveness' : None,  'Loudness' : None, 'Speechiness' : None, 'Valence' : None, 'Tempo' : None}

"""
def audioFeatures (sp , song_id):
	features = sp.audio_features(song_id)
	feat_dict = {}
	feat_dict.update("Duration" : features['duration_ms'])
	feat_dict.update("Key" : features['key'])
	feat_dict.update("Modality" : features['mode'])
	feat_dict.update("Time Signature" : features['time_signature'])
	feat_dict.update("Acousticness" : features['acousticness'])
	feat_dict.update("Danceability" : features['danceability'])
	feat_dict.update("Energy" : features['energy'])
	feat_dict.update("Instrumentalness" : features['instrumentalness'])
	feat_dict.update("Liveness" : features['liveness'])
	feat_dict.update("Loudness" : features['loudness'])
	feat_dict.update("Speechiness" : features['speechiness'])
	feat_dict.update("Valence" : features['valence'])
	feat_dict.update("Tempo" : features['tempo'])
	
	return feat_dict
"""
#	if the_album == None:
#		#return None if albums is not found
#		return None
#	#get the (full) album object using uri from (simplified) object
#	the_album_full = sp.album(the_album['uri'])
#	#match string of passed song with name of song inside paging object containing album object
#	for track in the_album_full['tracks']['items']:
#		if track['name'] == song:
#			return track['duration_ms']
#	return None
