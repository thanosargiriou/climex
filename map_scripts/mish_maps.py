"""
Map of the MISH spatio-temporal results

For eventual issues during installation please refer to the following link
https://stackoverflow.com/questions/53697814/using-pip-install-to-install-cartopy-but-missing-proj-version-at-least-4-9-0

https://lsterzinger.github.io/codeblog/map_plotting/plot_map.html

Input file: intermap.res file types

S. Logothetis - A. Argriou, LAPUP, 2021-03-30
"""

from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.io.shapereader as shpreader
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import pandas as pd

meteo_parameter = "TG"

df = pd.read_csv('intermap.res', skiprows=6, sep=r"\s+", header=None)

x0 = 19.3666666667
y0 = 34.475
delta = 0.00833

rows = 877
columns = 1235

gridded_data = []
df_gridded = pd.DataFrame()

for row in reversed(range(rows)):
    for column in reversed(range(columns)):
        gridded_data.append([y0 + 0.00833 * (rows - row - 1), x0 + 0.00833 * (columns - column - 1),
                             df[columns - column - 1][row]])

df_gridded = pd.DataFrame(gridded_data, columns=['lat', 'lon', 'variable'])

lat = df_gridded['lat'].to_numpy()
lon = df_gridded['lon'].to_numpy()
variable = df_gridded['variable'].to_numpy()

# Stavros: convert the gridded data to xarray object

arrays = [lat, lon]
tuples = list(zip(*arrays))
index = pd.MultiIndex.from_tuples(tuples, names=['Lat', 'Lon'])

df_merged = pd.DataFrame(data=variable, columns=[meteo_parameter], index=index)

my_xarray = df_merged[meteo_parameter].to_xarray()

# Map background definition files (https://gadm.org/download_country_v3.html)

fname = 'gadm36_GRC_1.shp'
adm1_shapes = list(shpreader.Reader(fname).geometries())

fig = plt.figure(figsize=(14, 8), dpi=300)
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

ax.coastlines(resolution='10m')
ax.add_geometries(adm1_shapes, ccrs.PlateCarree(), edgecolor='black', facecolor='gray', alpha=0.5)

ax.set_extent([19.5, 28.5, 34, 42], ccrs.PlateCarree())

gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=1, color='k', alpha=0.5, linestyle='--')
gl.xlabel_style = {'size': 40, 'color': 'gray'}
gl.xlabel_style = {'color': 'black', 'weight': 'bold'}
gl.ylabel_style = {'size': 40, 'color': 'gray'}
gl.ylabel_style = {'color': 'black', 'weight': 'bold'}
ax.tick_params(labelsize=30)
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

my_xarray.plot(vmin=-2, vmax=20, cmap='plasma')

ax.set_title("TG (°C) January mean for 1981-2010")
plt.savefig(meteo_parameter+".png", format="png", dpi=300, bbox_inches="tight")
plt.close()
