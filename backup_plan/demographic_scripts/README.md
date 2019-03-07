step 1: download intercensal data for 1979-1980. 
step 2: organize the 1970s data. subset the VA data and fix spacing, then do text to columns in Excel
step 3: organize the 1980s data. subset the VA data and do text to columns in Excel. Then aggregate the racial and age groups to get total counts using agg_sex_age_80s.py.

Note: county fips code changes https://www.census.gov/geo/reference/county-changes.html

step 4: append the population data to the health and weather data using join_demographic_data.py
step 5: append day of week using append_dow.py
step 6: append lag day death counts with lag_days.py