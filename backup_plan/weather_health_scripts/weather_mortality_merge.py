import glob
import pandas as pd

mortality_yearly_files = "C:\\Users\ginal\Documents\GitHub\masters-thesis\\backup_plan\health\\"
weather_csv = "G:\My Drive\Year 2\Thesis\Backup_Plan\weather\\virginia\\all_weather\\all_weather_data.csv"

# weather df
weather_df = pd.read_csv(weather_csv)
weather_df['death_count'] = 0

# make the final_df
final_df = pd.DataFrame()

for file in glob.glob(mortality_yearly_files + "*.csv"):
    mortality_df = pd.read_csv(file)
    subset_weather_df = weather_df.loc[weather_df['date'].str.contains(file.split("\\")[-1].split("_")[1])]
    
    for idx, row in subset_weather_df.iterrows():
        # subset mortality df by climate division, date
        temp_df = mortality_df.loc[(mortality_df['date'] == row['date']) & (mortality_df['climdiv'] == row['clim_div'])]
        # subset mortality df again by non-accidental death
        temp_df.loc[temp_df['underlying'] >=1000, 'underlying'] = temp_df['underlying']*0.1
        temp_df = temp_df.loc[(temp_df['underlying'] < 800) | ((temp_df['underlying'] >=992) & (temp_df['underlying'] < 993))]
        
        # get number of rows (number of deaths) and assign it to the death_count column
        subset_weather_df.at[idx, 'death_count'] = temp_df.shape[0]
    
    final_df = final_df.append(subset_weather_df)
    print("done with " + file)

final_df.to_csv("G:\My Drive\Year 2\Thesis\Backup_Plan\\all_data\\all_data_weather_mortality.csv", index=False)
        

