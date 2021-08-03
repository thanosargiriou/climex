"""
Creates the MISH dataseries.dat monthly input files.

Input file format: CLIMATOL homogenized monthly series.
The list 'stations' lists the columns homogenized on the latest period.

Athanassios A. Argiriou, LAPUP, 2021-03-24
"""
import pandas as pd

stations = ['16606', '16607', '16613', '16614', '16619', '16622', '16624', '16627', '16632', '16641', '16642', '16643',
            '16645', '16648', '16650', '16654', '16655', '16665', '16667', '16672', '16674', '16675', '16682', '16684',
            '16685', '16687', '16693', '16699', '16701', '16706', '16707', '16710', '16715', '16716', '16717', '16718',
            '16719', '16723', '16726', '16732', '16734', '16738', '16741', '16742', '16743', '16744', '16746', '16749',
            '16750', '16754', '16756', '16757', '16758', '16759', '16760', '16766', 'Date']

df = pd.read_csv("TG-m_1960-2010_series.csv", index_col=[0], usecols=lambda x: x in stations, parse_dates=True)

for month in range(12):
    print(month+1)
    df_m = df[df.index.month == month+1]
    df_m.insert(0, "Year", df_m.index.year, True)
    df_m.to_csv("TG_mish_dataseries_"+str(month+1)+".dat", index=False, sep=" ", float_format='%.2f')
