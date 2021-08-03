"""
Map of the CLIMEX HNMS weather station network

For eventual issues during installation please refer to the following link
https://stackoverflow.com/questions/53697814/using-pip-install-to-install-cartopy-but-missing-proj-version-at-least-4-9-0

S. Logothetis, A. Argriou, LAPUP, 2020-12-29
"""

from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.io.shapereader as shpreader
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import pandas as pd

df = pd.read_excel('HNMS_data_coverage_20200826.xls', usecols=[1, 2, 3])

name = df['Name '].tolist()
lat = df['Lat'].tolist()
lon = df['Lon'].tolist()

# Define the points to be shown on the map.
# This is done by defining a dictionary with the Lat and Lon (in decimal degrees) of the stations.
Stations = dict()
for i, index_a in enumerate(name):
    Stations[index_a] = {'Lat': lat[i], 'Lon': lon[i]}

Station_names = Stations.keys()

# Map background definition files (https://gadm.org/download_country_v3.html)
fname = 'gadm36_GRC_1.shp'
adm1_shapes = list(shpreader.Reader(fname).geometries())

fig = plt.figure(figsize=(14, 8), dpi=300)
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

ax.coastlines(resolution='10m')
ax.add_geometries(adm1_shapes, ccrs.PlateCarree(),
                  edgecolor='black', facecolor='gray', alpha=0.5)

ax.set_extent([19, 30, 34, 42], ccrs.PlateCarree())

gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=1, color='k', alpha=0.5, linestyle='--')

gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
for station in Station_names:
    ax.scatter(Stations[station]['Lon'], Stations[station]['Lat'], color='green', marker="*", s=80)
    ax.text(Stations[station]['Lon'], Stations[station]['Lat'], station, color='red')
plt.savefig("Greece.png", format="png", dpi=300, bbox_inches="tight")
plt.close()
