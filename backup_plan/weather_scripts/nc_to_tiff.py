from osgeo import gdal
import glob

data_path = "G:\My Drive\Year 2\Thesis\Backup_Plan\weather\\us\\rmax\\"

for nc_file in glob.glob(data_path + "*.nc"):
    src_ds = gdal.Open(nc_file)
    num_days = src_ds.RasterCount
    for day in range(1, num_days+1):
        output_tif = nc_file.split('.')[0] + "_" + str(day) + ".tif"
        ds = gdal.Translate(output_tif, src_ds, bandList=[day])