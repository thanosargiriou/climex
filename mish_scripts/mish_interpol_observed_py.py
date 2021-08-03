"""
Creates the MISH OBSERVED.DAT input file, used in the INTERPOL subdirectory

Athanassios A. Argiriou, LAPUP, 2021-03-27
"""
import pandas as pd

df = pd.read_csv("filambdahst_climex_GR.dat", sep="\s+")

station = df['st.index'].to_numpy()
longitude = df['lambda(x)'].to_numpy()
latitude = df['fi(y)'].to_numpy()

for i in range(12):
    month = i + 1
    print(month)
    dp = pd.read_csv("TG_mish_dataseries_" + str(month) + ".dat", sep=" ", index_col=[0], parse_dates=True)
    dp_av = dp[dp.index.year >= 1981].mean()
    output_file = open("TG_mish_observed_" + str(month) + ".dat", "w")
    output_file.write("index   lambda(x)       fi(y)    observation")
    output_file.write("\n")
    for k in range(len(station)):
        output_file.write(f'{station[k]:4.0f}   {longitude[k]:11.8f}   {latitude[k]:11.8f}  {dp_av.values[k]:6.2f}')
        output_file.write("\n")
    output_file.close()


