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


