import pandas as pd

data = "G:\My Drive\Year 2\Thesis\Data\\1979-1988\\all_data\\all_data_weather_mortality_population.csv"
df = pd.read_csv(data)
df['date_obj'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['dow'] = df['date_obj'].dt.day_name()
df['year'] = df['date_obj'].dt.year
df['doy'] = df['date_obj'].dt.dayofyear

#time = list(range(1, df.shape[0] + 1))
#df['time'] = time

current_date = pd.to_datetime('1/1/1979')
time = []
count = 1
for idx, row in df.iterrows():
    if row['date_obj'] == current_date:
        time.append(count)
    else:
        count+=1
        current_date = row['date_obj']
        time.append(count)

df['time'] = time
df = df.drop(columns=['date_obj'])
df.to_csv("G:\My Drive\Year 2\Thesis\Data\\1979-1988\\all_data\\all_data_weather_mortality_population_dow.csv", index=False)
