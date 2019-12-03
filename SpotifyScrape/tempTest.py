import spotScrape
import numpy as np
import pandas as pd
import csv
import sys

import time
sleep_min = 2
sleep_max = 5
start_time = time.time()
request_count = 0

#Test module for spotScrape.py, using dataFrame read from command line
arg_list = sys.argv
try:
	raw_df = pd.read_csv(arg_list[1])
	print('Reading csv ' + str(arg_list[1]) + " , its first 5(or less) elements:")
	print(raw_df.head())
except:
	print("csv not found... quitting")
	exit()
#
#raw_df['features'] = [spotScrape.getDurationWithoutAlbum(artist, song) for (artist, song) in zip(raw_df['Artist'], raw_df['Song'])]
#print(raw_df)
cols = ['Song', 'Artist', 'Album', 'Duration(ms)', 'Key', 'Modality', 'Time Signature' , 'Acousticness', 'Danceability', 'Energy', 'Instrumentalness', 'Liveness', 'Loudness', 'Speechiness', 'Valence', 'Tempo' ]
scraped_df = pd.DataFrame(columns = cols) 
print("\nScraped DataFrame intitalized: \n")
print(scraped_df)
print()

frames = [spotScrape.getDurationWithoutAlbum(artist, song) for artist, song in zip(raw_df['Artist'], raw_df['Song'])]
new_df = pd.DataFrame(frames)
print(new_df)

print("--- %s seconds ---" % (time.time() - start_time))


#scraped_df.append(frames)
#print(scraped_df)

#rows_list = []
#for row in raw_df:
#	print(row)



# Goteen by own investigation:
"""df['Album'] = None

# My titles: Duration(ms), Key, Modality, Time Signature, Acousticness, Danceability, Energy, Instrumentalness, Liveness, 
# Loudness, Speechiness, Valence, Tempo
# Spotify Track fields: duration(ms), key, mode, time_signature (all int's), acousticness, danceability, energy, instrumentalness,
# liveness, loudness, speechiness, valence, tempo (all float's) 
df['Duration(ms)'] = None
df['Key'] = None
df['Modality'] = None
df['Time Signature'] = None
df['Acousticness'] = None
df['Danceability'] = None
df['Energy'] = None
df['Instrumentalness'] = None
df['Liveness'] = None
df['Loudness'] = None
df['Speechiness'] = None
df['Valence'] = None
df['Tempo'] = None

print(df)

df.append(spotScrape.getDurationWithoutAlbum(artist, song))


for row in numArr:
	duration.append(spotScrape.getDurationWithoutAlbum(row[0], row[2])['duration'])
	request_count += 1
	#random delay
	if request_count % 5 == 0:
		print(str(request_count) + " durations grabbed")
		time.sleep(np.random.uniform(sleep_min, sleep_max))
		print('Loop #: {}'.format(request_count))
		print('Elapsed Time: {} seconds'.format(time.time() - start_time))
# add song duration column to dataframe
print(duration)

new_df = pd.DataFrame(numArr)
new_df.insert(3, "Duration(ms)", duration)
print()
print("New dataFrame:")
print()
print(new_df)

"""