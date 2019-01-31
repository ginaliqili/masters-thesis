# create date column from month, day, and year
# append climdiv column based on nhcs county code, using the nchs to fips mapping
import pandas as pd
import glob, os

path = "C:/Users/ginal/Documents/GitHub/masters-thesis/backup_plan/"
os.chdir(path)
# read in the each yearly csv file
for file in glob.glob("data_198*.csv"):
    # add date column
    df = pd.read_csv(file)
    year = int(file.split(".")[0].split("_")[1])
    print(year)
    df['year_of_death'] = year
    df = df.rename(index=str, columns={"year_of_death": "year", "month_of_death": "month", "date_of_death": "day"})
    
    df['date'] = df.month.astype(str).str.zfill(2) + "/" + df.day.astype(str).str.zfill(2) + "/" + df.year.astype(str)

    # add the climdiv column and populate it
    #df['climdiv'] = ""
    climdiv = []
    if year <=1981:
        map_file = "nchs_county_mapping_1968-1981.csv"
        map_df = pd.read_csv(map_file)
        for idx, row in df.iterrows():
            # look at nchs county_fips and match with climdiv
            nchs_county_fips = row['county_fips']
            print(map_df.loc[map_df['nchs_county_code'] == nchs_county_fips, 'clim_div'].values[0])
            climdiv.append(map_df.loc[map_df['nchs_county_code'] == nchs_county_fips, 'clim_div'].values[0])

            

    if year > 1981:
        map_file = "nchs_county_mapping_1982-1988.csv"
        map_df = pd.read_csv(map_file)
        for idx, row in df.iterrows():
            nchs_county_fips = row['county_fips']
            # look at nchs county_fips and match with climdiv
            print(map_df.loc[map_df['nchs_county_code'] == nchs_county_fips, 'clim_div'].values[0])
            climdiv.append(map_df.loc[map_df['nchs_county_code'] == nchs_county_fips, 'clim_div'].values[0])

    df['climdiv'] = climdiv
    df.to_csv("health/" + file.split(".")[0] + "_climdiv.csv")

