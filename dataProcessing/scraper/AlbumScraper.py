from bs4 import BeautifulSoup
from requests import get
import json
import pandas as pd

columns = ['Rank', 'Album', 'Artist', 'Year']
years = ['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
df = pd.DataFrame(columns=columns)
for year in years:
    url = 'https://www.billboard.com/charts/year-end/' + year + '/top-billboard-200-albums' #get URL with year
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)
    rows = html_soup.findAll('div', {'class': 'ye-chart-item__primary-row decade-end-chart-item__no-expand'})
    for row in rows:
        rank = row.find('div', {'class': 'ye-chart-item__rank'}).text.strip() #find rank and strip text
        album = row.find('div', {'class': 'ye-chart-item__title'}).text.strip() #find album and strip text
        artist = row.find('div', {'class': 'ye-chart-item__artist'}).text.strip() #find artist and strip text
        data = {'Rank': [rank], 'Album': [album], 'Artist': [artist], 'Year': [year]} #add to data
        dfRow = pd.DataFrame(data, columns=columns) #put data in DFrow
        df = pd.concat([df, dfRow], ignore_index=True) #append to df
        print('Adding ' + album + ', ranked ' + rank + ' to data.')
print(df)
df.to_csv('2005-2018top200albums.csv') #export to csv

