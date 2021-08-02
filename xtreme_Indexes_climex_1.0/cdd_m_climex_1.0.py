import pandas as pd
import glob

"""
Climate indexes as defined by http://etccdi.pacificclimate.org/list_27_indices.shtml
Authors: Ioannidis Panagiotis, Athanassios Argiriou,
github: ioannidispanagiotis,
email: panagiwths.ioannidis117@gmail.com
Laboratory of Atmospheric Physics - Department of Physics - University of Patras (https://www.atmosphere-upatras.gr/en)
"""
"""
Climate index: CDD
Definition: [Consecutive dry days]. Let RR be daily precipitation. Maximum number of consecutive days with RR < 1 mm 
            per month.
Version 1.0, 2021-07-08
"""
# csv input files must have the following format name "[station_number(5 digits)]_rr.csv"
for filename in glob.glob("*_rr.csv"):
    cdd_lst = []  # List to save index values per year
    df = pd.read_csv(filename, index_col=[0], parse_dates=True)  # Data import

    for y in range(df.index.year[0], df.index.year[-1] + 1):  # Iteration over every year
        if y in df.index.year:  # Checks if values for given year exist
            df_year = df[df.index.year == y]
            for m in range(1, 13):
                if m in df_year.index.month:
                    # Monthly count of consecutive days with daily precipitation < 1 mm
                    cdd_df = df_year[df_year.index.month == m][df_year[df_year.index.month == m] < 1].dropna()
                    # Check if the days are consecutive
                    count = 0
                    count_lst = []
                    for q in range(1, len(cdd_df.index)):
                        if (cdd_df.index[q] - cdd_df.index[q-1]).days != 1:
                            count = 0
                        else:
                            count = count + 1
                        count_lst.append(count)
                    if len(count_lst) == 0:
                        pass
                    else:
                        cdd = max(count_lst) + 1
                    cdd_lst.append(cdd)
                else:
                    cdd = float("NaN")
                    cdd_lst.append(cdd)
        else:
            cdd = float("NaN")
            cdd_lst.append(cdd)
    # Dataframe to save files
    dates = pd.date_range(start=str(df.index.year[0]), end=str(df.index.year[-1] + 1), freq="M")  # Date column
    df_output = pd.DataFrame({"Date": dates, "CDD per month (# of days)": cdd_lst})
    # filename[:5] to select the station code
    df_output.to_csv("CDD_monthly_" + filename[:5] + ".csv", sep=";", index=False)
