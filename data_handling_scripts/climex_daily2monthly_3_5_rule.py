"""
Calculation of monthly values from daily values using the 5/3 rule for temperature and the 0 rule for precipitation

Thanos Argiriou, 2020-10-13, LAPUP
"""

import pandas as pd
import numpy as np
import datetime


def years(df_input):  # Determines the start and end year of the time series
    return df_input.index.min().year, df_input.index.max().year


def monthly_avg_5_3(df_input):  # Calculates monthly averages from the daily data applying the WMO 5/3 averaging rule
    df_monthly_of_a_year = pd.DataFrame()

    for m in range(1, 13):
        # print(f"Processed month {m}")

        df_single_month = df_input[df_input.index.month == m]  # Extracts daily values of a specific month

        df_monthly = df_single_month.resample('M').mean()  # Calculates the mean monthly value

        count = df_single_month.isna().sum()  # Counts the number of missing values in the month
        # print(f"Number of missing days: {count[0]}")

        if count[0] > 4:  # If more than 5 missing days, set mean monthly value equal to zero
            df_monthly[df_monthly.columns[0]] = np.nan
        if (count[0] <= 4) and (count[0] >= 3):
            missing_dates = df_single_month[df_single_month[df_single_month.columns[0]].isna()]
            steps = len(missing_dates) - 3
            for i in range(steps + 1):
                if missing_dates.index[i + 2] - missing_dates.index[i] == datetime.timedelta(days=3):
                    df_monthly[df_monthly.columns[0]] = np.nan

        df_monthly_of_a_year = pd.concat([df_monthly_of_a_year, df_monthly])

    return df_monthly_of_a_year


def monthly_precipitation(df_input):  # Calculates monthly sums from the daily precipitation data
    # applying the WMO 0 missing days rule
    df_monthly_of_a_year = pd.DataFrame()

    for m in range(1, 13):
        # print(f"Processed month {m}")

        df_single_month = df_input[df_input.index.month == m]  # Extracts daily values of a specific month

        df_monthly = df_single_month.resample('M').sum()  # Calculates the mean monthly value

        count = df_single_month.isna().sum()  # Counts the number of missing values in the month
        # print(f"Number of missing days: {count[0]}")

        if count[0] > 0:  # If there are missing days, set monthly value equal to zero
            df_monthly[df_monthly.columns[0]] = np.nan

        df_monthly_of_a_year = pd.concat([df_monthly_of_a_year, df_monthly])

    return df_monthly_of_a_year


if __name__ == "__main__":

    params = ['TN', 'TG', 'TX', 'DTR', 'RR']  # Meteorological parameters to be processed
    # params = ['TN']

    df = pd.read_csv("data_unified.csv", na_values='NA', parse_dates=True, index_col=1)  # Reads the global datafile

    stations = df['Station'].unique()  # Extracts the station codes

    df_monthly_global = pd.DataFrame()

    for wmo_code in stations:
        # for wmo_code in [16606]:

        df_station = df.loc[df['Station'] == wmo_code]  # Extracts the data of a single station

        # print(f"Station: {wmo_code}, Start year: {years(df_station)[0]}, End year: {years(df_station)[1]}")

        for param in params:

            df_monthly_param = pd.DataFrame()  # Empty dataframe for a specific parameter

            for year in range(years(df_station)[0], years(df_station)[1] + 1):  # Processing period
                # print(f"Processed year: {year}")

                df_daily_of_year = df_station[df_station.index.year == year]  # Extracts the data of a specific year

                df_param = df_daily_of_year[param]

                if param == 'RR':
                    df_param = pd.DataFrame(df_daily_of_year[param], df_daily_of_year.index)
                    df_monthly_param = pd.concat([df_monthly_param, monthly_precipitation(df_param)])
                else:
                    df_param = pd.DataFrame(df_daily_of_year[param], df_daily_of_year.index)
                    df_monthly_param = pd.concat([df_monthly_param, monthly_avg_5_3(df_param)])

            filename = str(wmo_code) + '_' + param + '_m.csv'
            df_monthly_param.to_csv(filename, na_rep='NaN')
