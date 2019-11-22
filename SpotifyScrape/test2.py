import spotScrape
import numpy as np
import pandas as pd
import csv
import sys

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
# list object to hold duration values in ms, to be added to dataframe
duration = []
# call spotScrape module to getDuration of songs, append to list
for row in numArr:
	duration.append(spotScrape.getDuration(row[0], row[1], row[2]))
# add song duration column to dataframe
df.insert(3, "Duration(ms)", duration)
print()
print("New dataFrame:")
print()
print(df)
