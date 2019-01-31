import arcpy
import glob

arcpy.env.workspace = "G:\My Drive\Year 2\Thesis\Backup_Plan\weather\\virginia\\tmmx\\"
va_climate_divisions_shp = "C:\Users\ginal\Documents\GitHub\masters-thesis\Maps\VA_Climate_Divisions_wgs84.shp"

us_tif_files = "G:\My Drive\Year 2\Thesis\Backup_Plan\weather\\us\\tmmx\\"

for tif_file in glob.glob(us_tif_files + "*.tif"):
    out_raster = tif_file.split("\\")[-1].split(".")[0] + "_va.tif"
    arcpy.Clip_management (tif_file, "-83.675413 36.540739 -75.241390 39.466012", out_raster, va_climate_divisions_shp, '0', "ClippingGeometry", "MAINTAIN_EXTENT")
