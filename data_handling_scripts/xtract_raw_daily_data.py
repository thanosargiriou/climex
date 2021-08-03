"""
Reads the daily_data_allstations_20210319.csv file and extracts all data for the station and parameter specified

Thanos Argiriou, 2021-07-11, LAPUP
"""
import pandas as pd

parameter = 'TX'  # Parameter to be extracted among TN, TG, TX, DTR, RR
Station = 16648  # Station to be extracted

# Reads the datafile
df = pd.read_csv("daily_data_allstations_20210319.csv", na_values='NA', usecols=['Station', 'Date', parameter],
                 parse_dates=True, index_col=1)

filename = str(Station) + '_' + parameter + '_d.csv'
df[df['Station'] == Station]['TX'].to_csv(filename)
