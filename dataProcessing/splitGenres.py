import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

genre_data = pd.read_csv('genreData.csv')
df_pop = genre_data.iloc[:639 ,:]
df_pop.to_csv("top_pop_tracks.csv")
df_adultPop = genre_data.iloc[639:1294 ,:]
df_adultPop.to_csv("top_adultPop_tracks.csv")
df_country = genre_data.iloc[1294:2433 ,:]
df_country.to_csv("top_country_tracks.csv")
df_rock = genre_data.iloc[2433:3340 ,:]
df_rock.to_csv("top_rock_tracks.csv")
df_rbHipHop = genre_data.iloc[3340:4700 ,:]
df_rbHipHop.to_csv("top_rbHipHop_tracks.csv")
df_rap = genre_data.iloc[4700:5262 ,:]
df_rap.to_csv("top_rap_tracks.csv")
df_rythmic = genre_data.iloc[5262:5969 ,:]
df_rythmic.to_csv("top_rythmic_tracks.csv")
df_latin = genre_data.iloc[5969:6966 ,:]
df_latin.to_csv("top_latin_tracks.csv")
df_electronic = genre_data.iloc[6966:8260 ,:]
df_electronic.to_csv("top_electronic_tracks.csv")
df_christian = genre_data.iloc[8260:9050 ,:]
df_christian.to_csv("top_christian_tracks.csv")
df_gospel = genre_data.iloc[9050:9603 ,:]
df_gospel.to_csv("top_pop_tracks.csv")
df_smoothJazz = genre_data.iloc[9603: ,:]
df_smoothJazz.to_csv("top_smoothJazz_tracks.csv")