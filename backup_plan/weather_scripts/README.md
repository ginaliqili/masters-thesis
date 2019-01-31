step 1: Download yearly (1979-1988) reanalysis data from gridMET http://www.climatologylab.org/gridmet.html using THREDDS catalog (OPENDAP) option

step 2: Convert netCDF yearly files to daily GeoTIFF files using nc_to_tiff.py. This will read in each netCDF file and extract each band (representing a single day) out and save out to a tif file.

step 3: Clip rasters to Virginia using subset_virginia.py. This will use arcpy to clip the raster to a Virginia boundary.

step 4: Perform zonal statistics for each day for each climate division using zonal_stats.py. This will use arcpy to summarize the daily max temperature or humidity in each climate division via averaging. Sort resulting csv by ascending date in Excel. Delete index column from pandas.

step 5: Merge rmax and tmmx data sets together using tmmx_rmax_merge.py. This script also appends temperature in F, temperatuer in C, and heat index columns. 