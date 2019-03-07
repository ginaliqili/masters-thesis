import pandas as pd

dem_data_1970s = "G:\My Drive\Year 2\Thesis\Data\\1979-1988\demographic\\va_1970s.csv"
dem_data_1980s = "G:\My Drive\Year 2\Thesis\Data\\1979-1988\demographic\\va_1980s_agg.csv"
weather_mort_data = "G:\My Drive\Year 2\Thesis\Data\\1979-1988\\all_data\\all_data_weather_mortality.csv"
va_counties_data = "C:\\Users\ginal\Documents\GitHub\masters-thesis\\backup_plan\demographic_scripts\\va_counties_wgs84.csv"

df_1970s = pd.read_csv(dem_data_1970s)
df_1980s = pd.read_csv(dem_data_1980s)
df_weather_mort = pd.read_csv(weather_mort_data)
df_counties = pd.read_csv(va_counties_data)

# join 1979 demographic data to weather and mortality data by matching year and FIPS code
# first, append clim_div column to demographic data
for idx, row in df_1970s.iterrows():
    if row['FIPS Code'] != 51000:
        clim_div = df_counties.loc[df_counties['fips_cd']==row['FIPS Code'], 'clim_div'].values[0]
        df_1970s.at[idx, 'clim_div'] = clim_div

# aggregate by climate division and sum
df_1970s_agg = df_1970s.groupby(['clim_div']).agg(sum)
# assign all the rows with 1979 in subset of df_weather_mort the correct population
df_final = pd.DataFrame()
df_temp = df_weather_mort.loc[df_weather_mort['date'].str.contains('1979')]
for idx, row in df_temp.iterrows():
        clim_div = row['clim_div']
        df_temp.at[idx, 'tot_pop'] = df_1970s_agg.loc[clim_div, 'Estimate 1979']
df_final = df_final.append(df_temp)
print("appended 1979 demographic data")

# join 1980-1988 demographic data to weather and mortality data by matching year and FIPS code
for idx, row in df_1980s.iterrows():
        clim_div = df_counties.loc[df_counties['fips_cd']==row['FIPS State and County Codes'], 'clim_div'].values[0]
        df_1980s.at[idx, 'clim_div'] = clim_div

# aggregate by climate division and sum
df_1980s_agg = df_1980s.groupby(['clim_div'])[['total population']].agg(sum)
# assign rows in subset of df_weather_mort the correct population depending on the year in 1980s
for year in range (1980, 1989): 
        df_year = df_1980s.loc[df_1980s['Year of Estimate']==year]
        df_year_agg = df_year.groupby(['clim_div'])[['total population']].agg(sum)
        
        df_temp = df_weather_mort.loc[df_weather_mort['date'].str.contains(str(year))]
        
        for idx, row in df_temp.iterrows():
                clim_div = row['clim_div']
                df_temp.at[idx, 'tot_pop'] = df_year_agg.loc[clim_div, 'total population']

        df_final = df_final.append(df_temp)
        print("appended " + str(year) + " demographic data")

df_final.to_csv("G:\My Drive\Year 2\Thesis\Data\\1979-1988\\all_data\\all_data_weather_mortality_population.csv", index=False)       

