"""
Reads the daily_data_allstations_20210319.csv file and finds the time - series length for each station and parameter

Thanos Argiriou, 2921-07-11, LAPUP
"""

import pandas as pd

params = ['TN', 'TG', 'TX', 'DTR', 'RR']  # Meteorological parameters to be processed
# params = ['TN']

# Reads the datafile
df = pd.read_csv("daily_data_allstations_20210319.csv", na_values='NA', parse_dates=True, index_col=1)

stations = df['Station'].unique()  # Extracts the station codes
# stations = [16606]

df_2bchecked = pd.DataFrame()
df_output = pd.DataFrame(columns=['Station', 'Parameter', 'Start', 'End'])

for wmo_code in stations:
    df_station = df.loc[df['Station'] == wmo_code]  # Extracts the data of a single station
    for parameter in params:
        df_2bchecked = df_station[parameter].dropna()
        print(f"Station: {wmo_code}, Parameter: {parameter}, Start date: {df_2bchecked.index.min()}, "
              f"End date: {df_2bchecked.index.max()}")
        s2 = pd.Series([wmo_code, parameter, df_2bchecked.index.min(), df_2bchecked.index.max()],
                       index=['Station', 'Parameter', 'Start', 'End'])
        df_output = df_output.append(s2, ignore_index=True)
        df_output.sort_values(by=['Parameter', 'Start']).to_csv('time_series_length.csv', index=False)
