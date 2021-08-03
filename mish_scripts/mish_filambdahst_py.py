"""
Creates the MISH filambdahst.dat input file.

Athanassios A. Argiriou, LAPUP, 2021-03-24
"""
import pandas as pd

df = pd.read_csv("HNMS_Climex_network.csv", sep=";", usecols=[0, 2, 3, 4])
# df = pd.read_csv("CN_Climex_network.txt", sep=";")

station = df['WMOcode'].to_numpy()
station = station - 16000
longitude = df['Lon'].to_numpy()
latitude = df['Lat'].to_numpy()
height = df['Alt'].to_numpy()

output_file = open("filambdahst_climex_CN.dat", "w")

output_file.write("st.index   lambda(x)         fi(y)  height")
output_file.write("\n")

for i in range(len(df)):
    output_file.write(f'{station[i]:4.0f}     {longitude[i]:11.8f}   {latitude[i]:11.8f}   {height[i]:5.1f}')
    output_file.write("\n")

output_file.close()
