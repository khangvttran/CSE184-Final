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
	df = pd.read_csv(arg_list[1])
	print('Reading csv ' + str(arg_list[1]) + " , its first 5(or less) elements:")
except:
	print("csv not found... quitting")
	exit()
print(df.head())
# put dataFrame into numpy array, might not be necessarry, used for conveinience
numArr = df.values
#numArr = numArr[:9, :]
# list object to hold duration values in ms, to be added to dataframe
duration = []
# call spotScrape module to getDuration of songs, append to list
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
