"""
Example of producing maps and specific locations
S. Logothetis LAPUP, 2020-12-21

For eventual issues during installation please refer to the following link
https://stackoverflow.com/questions/53697814/using-pip-install-to-install-cartopy-but-missing-proj-version-at-least-4-9-0

A. Argriou, LAPUP, 2020-12-22
"""

from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy

# Define the points to be shown on the map.
# This is done by defining a dictionary with the Lat and Lon (in decimal degrees) of the stations.

Stations = {"Athens": {'Lat': 37.98, 'Lon': 23.72}, "Patra": {'Lat': 38.25, 'Lon': 21.73}}
Station_names = Stations.keys()

plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"

fig = plt.figure(figsize=(14, 8), dpi=300)
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.stock_img()
ax.coastlines(resolution='10m')
ax.add_feature(cartopy.feature.LAND)
ax.add_feature(cartopy.feature.OCEAN)
ax.add_feature(cartopy.feature.COASTLINE)
ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=.5)
ax.add_feature(cartopy.feature.LAKES, alpha=0.3)
ax.add_feature(cartopy.feature.RIVERS)

ax.set_extent([20, 30, 34, 42], ccrs.PlateCarree())

gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=1, color='k', alpha=0.5, linestyle='--')

gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

for station in Station_names:
    ax.scatter(Stations[station]['Lon'], Stations[station]['Lat'], color='green', marker="*", s=80)
    ax.text(Stations[station]['Lon'], Stations[station]['Lat'], station, color='red')

plt.savefig("Greece.png", format="png", dpi=300, bbox_inches="tight")
plt.close()
