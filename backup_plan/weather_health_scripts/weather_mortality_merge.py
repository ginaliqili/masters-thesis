import glob
import pandas as pd

mortality_yearly_files = "G:\\My Drive\\Year 2\\Thesis\\Data\\1979-1988\\mortality\\formatted_with_climdiv\\"
weather_csv = "G:\\My Drive\\Year 2\\Thesis\\Data\\1979-1988\\weather\\virginia\\all_weather\\all_weather_data.csv"

# weather df
weather_df = pd.read_csv(weather_csv)
weather_df['date'] = pd.to_datetime(weather_df['date'], format='%m/%d/%Y')
weather_df['death_count'] = 0

# make the final_df
final_df = pd.DataFrame()

for file in glob.glob(mortality_yearly_files + "*.csv"):
    mortality_df = pd.read_csv(file)
    mortality_df['underlying'] = mortality_df['underlying'].apply(str)
    mortality_df['underlying'] = mortality_df['underlying'].str.ljust(4, '0')
    mortality_df['underlying'] = mortality_df['underlying'].apply(int)
    mortality_df['underlying'] = mortality_df['underlying'] * 0.1
    
    # only keep rows that have exact day of death
    mortality_df = mortality_df.loc[mortality_df['day']!=99] 
    mortality_df['date'] = pd.to_datetime(mortality_df['date'], format='%m/%d/%Y')


    subset_weather_df = weather_df.loc[weather_df['date'].dt.year==int(file.split("\\")[-1].split("_")[1])]
    
    for idx, row in subset_weather_df.iterrows():
        # subset mortality df by climate division, date
        temp_df = mortality_df.loc[(mortality_df['date'] == row['date']) & (mortality_df['climdiv'] == row['clim_div'])]
        # subset mortality df again by non-accidental death
        temp_df = temp_df.loc[(temp_df['underlying'] < 800) | ((temp_df['underlying'] >=992) & (temp_df['underlying'] < 993))]
        # get number of rows (number of deaths) and assign it to the death_count column
        subset_weather_df.at[idx, 'death_count'] = temp_df.shape[0]
    
    final_df = final_df.append(subset_weather_df)
    print("done with " + file)

final_df.to_csv("G:\\My Drive\\Year 2\\Thesis\\Data\\1979-1988\\all_data\\all_data_weather_mortality.csv", index=False)
        

