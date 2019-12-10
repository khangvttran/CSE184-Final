from bs4 import BeautifulSoup
from requests import get
import json
import pandas as pd
import time
import random

columns = ['Rank', 'Song', 'Artist', 'Year', 'Genre']
genres = ['pop', 'adult-pop', 'hot-country', 'hot-rock', 'hot-r-and-and-b-hip-hop', 'hot-r-and-and-b-', 'hot-rap', 'rhythmic', 'hot-latin', 'hot-dance-electronic-', 'hot-christian', 'hot-gospel', 'smooth-jazz', ]
years = ['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
df = pd.DataFrame(columns=columns)
for genre in genres: 
    for year in years: #get each year per genre
        time.sleep(random.randint(1,10)) #delay so i dont get banned
        url = 'https://www.billboard.com/charts/year-end/' + year + '/' + genre + '-songs' #get url and genre
        response = get(url)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        type(html_soup)
        rows = html_soup.findAll('div', {'class': 'ye-chart-item__primary-row'}) #get all rows from webpage
        for row in rows:
            rank = row.find('div', {'class': 'ye-chart-item__rank'}).text.strip() #find rank text
            song = row.find('div', {'class': 'ye-chart-item__title'}).text.strip() #find song text
            artist = row.find('div', {'class': 'ye-chart-item__artist'}).text.strip() #find artist text
            data = {'Rank': [rank], 'Song': [song], 'Artist': [artist], 'Year': [year], 'Genre': [genre]}
            dfRow = pd.DataFrame(data, columns=columns) #create df with above data
            df = pd.concat([df, dfRow], ignore_index=True) #append to df
            print('Adding ' + song + ', ranked ' + rank + ' to data.')
print(df)
df.to_csv('topGenres.csv') #export df to csv

