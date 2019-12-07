from bs4 import BeautifulSoup
from requests import get
import json
import pandas as pd

columns = ['Rank', 'Artist', 'Year']
years = ['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
df = pd.DataFrame(columns=columns)
for year in years:
    url = 'https://www.billboard.com/charts/year-end/' + year + '/top-artists'
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)
    rows = html_soup.findAll('div', {'class': 'ye-chart-item__primary-row decade-end-chart-item__no-expand'})
    for row in rows:
        rank = row.find('div', {'class': 'ye-chart-item__rank'}).text.strip()
        artist = row.find('div', {'class': 'ye-chart-item__title'}).text.strip()
        data = {'Rank': [rank], 'Artist': [artist], 'Year': [year]}
        dfRow = pd.DataFrame(data, columns=columns)
        df = pd.concat([df, dfRow], ignore_index=True)
        print('Adding ' + artist + ', ranked ' + rank + ' to data.')
print(df)
df.to_csv('2005-2018top100artists.csv')

