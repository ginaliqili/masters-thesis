from rasterstats import zonal_stats
import glob
import datetime
import pandas as pd

tif_path = "G:\My Drive\Year 2\Thesis\Backup_Plan\weather\\virginia\\tmmx\\"
va_climate_divisions_shp = "C:\\Users\ginal\Documents\GitHub\masters-thesis\Maps\VA_Climate_Divisions_wgs84.shp"

dates = []
clim_divs = []
means = []

for tif_file in glob.glob(tif_path + "*.tif"):
    div_stats = zonal_stats(va_climate_divisions_shp, tif_file, stats="mean", geojson_out=True)
    year_str = tif_file.split("\\")[-1].split("_")[1]
    julian_day_str = tif_file.split("\\")[-1].split("_")[2]
    date_obj = datetime.datetime.strptime(year_str+julian_day_str, '%Y%j').date()
    standard_date_str = date_obj.strftime('%m/%d/%Y')
    for idx in range(0, len(div_stats)):
        dates.append(standard_date_str)
        clim_divs.append(div_stats[idx]['properties']['NAME'])
        means.append(div_stats[idx]['properties']['mean'])
    print(tif_file + " done")

zonal_stats_df = pd.DataFrame(
    {
        'date': dates,
        'clim_div': clim_divs,
        'mean': means
    }
)

output_path = tif_path + "zonal_stats2\\"
import IPython
IPython.embed()
zonal_stats_df.to_csv(output_path + "zonal_stats.csv")

