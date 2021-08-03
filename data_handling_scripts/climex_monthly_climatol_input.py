"""
Reads the monthly data files (1 file per station and per parameter) and creates a global input file for the
CLIMATOL software.

Thanos Argiriou, 2020-12-11, LAPUP
"""
import pandas as pd

stations = [16606, 16607, 16613, 16614, 16619, 16622, 16624, 16627, 16632, 16641, 16642,
            16643, 16645, 16648, 16650, 16654, 16655, 16665, 16667, 16672, 16674, 16675, 16682,
            16684, 16685, 16687, 16693, 16699, 16701, 16706, 16707, 16710, 16715, 16716,
            16717, 16718, 16719, 16723, 16726, 16732, 16734, 16738, 16741, 16742, 16743,
            16744, 16746, 16749, 16750, 16754, 16756, 16757, 16758, 16759, 16760, 16766]  # WMO station codes

parameters = ['TN', 'TG', 'TX', 'DTR', 'RR']  # Available time series

for parameter in parameters:

    output_file = parameter + '-m_1960-2010.dat'  # Definition of monthly files name compatible with CLIMATOL
    print(output_file)

    for station in stations:

        input_file = str(station) + '_' + parameter + '_m.csv'  # Parameter per station monthly files

        df = pd.read_csv(input_file, usecols=[1])
        df.transpose().to_csv(output_file, sep=',', na_rep='NA', index=False, header=False, float_format='%.1f',
                              mode='a')

