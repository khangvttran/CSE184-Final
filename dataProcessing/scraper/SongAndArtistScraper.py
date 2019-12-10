from bs4 import BeautifulSoup
from requests import get
import json
import pandas as pd

columns = ['Rank', 'Song', 'Artist', 'Year']
years = ['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
df = pd.DataFrame(columns=columns)
for year in years:
    url = 'https://www.billboard.com/charts/year-end/' + year + '/hot-100-songs' #get URL with year
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser') 
    type(html_soup)
    rows = html_soup.findAll('div', {'class': 'ye-chart-item__primary-row decade-end-chart-item__no-expand'}) #get all rows from page
    for row in rows:
        rank = row.find('div', {'class': 'ye-chart-item__rank'}).text.strip() #find rank and strip text
        song = row.find('div', {'class': 'ye-chart-item__title'}).text.strip() #find song and strip text
        artist = row.find('div', {'class': 'ye-chart-item__artist'}).text.strip() #find artist and strip text
        data = {'Rank': [rank], 'Song': [song], 'Artist': [artist], 'Year': [year]}
        dfRow = pd.DataFrame(data, columns=columns)  #add data to a dfrow
        df = pd.concat([df, dfRow], ignore_index=True) #append dfrow to df
        print('Adding ' + song + ', ranked ' + rank + ' to data.')
print(df)
df.to_csv('2005-2018top100.csv') #export to csv

