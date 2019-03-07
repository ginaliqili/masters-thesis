import pandas as pd
import datetime as dt

data_csv = "G:\My Drive\Year 2\Thesis\Data\\1979-1988\\all_data\\all_data_weather_mortality_population_dow.csv"
df = pd.read_csv(data_csv)
df['date'] = pd.to_datetime(df['date'])
#df['date'] = df['date'].dt.date
df_subset = df.loc[df['date'] > '1/10/1979']
df_subset['date'] = df_subset['date'].apply(lambda x: x.to_pydatetime().date())
# append lag days up to 10 days
# iterate from 1-10-1979 to 12-31-1988
tmmx_lag_1 = []
tmmx_lag_2 = []
tmmx_lag_3 = []
tmmx_lag_4 = []
tmmx_lag_5 = []
tmmx_lag_6 = []
tmmx_lag_7 = []
tmmx_lag_8 = []
tmmx_lag_9 = []
tmmx_lag_10 = []

rmax_lag_1 = []
rmax_lag_2 = []
rmax_lag_3 = []
rmax_lag_4 = []
rmax_lag_5 = []
rmax_lag_6 = []
rmax_lag_7 = []
rmax_lag_8 = []
rmax_lag_9 = []
rmax_lag_10 = []

heat_index_lag_1 = []
heat_index_lag_2 = []
heat_index_lag_3 = []
heat_index_lag_4 = []
heat_index_lag_5 = []
heat_index_lag_6 = []
heat_index_lag_7 = []
heat_index_lag_8 = []
heat_index_lag_9 = []
heat_index_lag_10 = []



#for idx, row in df_subset.iterrows():
for idx, row in df.iterrows():
    lag_days = []
    lag_1_day = row['date'] - dt.timedelta(days=1)
    lag_2_day = row['date'] - dt.timedelta(days=2)
    lag_3_day = row['date'] - dt.timedelta(days=3)
    lag_4_day = row['date'] - dt.timedelta(days=4)
    lag_5_day = row['date'] - dt.timedelta(days=5)
    lag_6_day = row['date'] - dt.timedelta(days=6)
    lag_7_day = row['date'] - dt.timedelta(days=7)
    lag_8_day = row['date'] - dt.timedelta(days=8)
    lag_9_day = row['date'] - dt.timedelta(days=9)
    lag_10_day = row['date'] - dt.timedelta(days=10)
    #lag_days.extend((lag_1_day, lag_2_day, lag_3_day, lag_4_day, lag_5_day, lag_6_day, lag_7_day, lag_8_day, lag_9_day, lag_10_day))
    try:
        tmmx_lag_1.append(df.loc[(df['date'] == lag_1_day) & (df['clim_div'] == row['clim_div'])]['tmmx_f'].values[0])
    except: 
        tmmx_lag_1.append(-999)
    try:
        tmmx_lag_2.append(df.loc[(df['date'] == lag_2_day) & (df['clim_div'] == row['clim_div'])]['tmmx_f'].values[0])
    except:
        tmmx_lag_2.append(-999)
    try:
        tmmx_lag_3.append(df.loc[(df['date'] == lag_3_day) & (df['clim_div'] == row['clim_div'])]['tmmx_f'].values[0])
    except:
        tmmx_lag_3.append(-999)
    try:
        tmmx_lag_4.append(df.loc[(df['date'] == lag_4_day) & (df['clim_div'] == row['clim_div'])]['tmmx_f'].values[0])
    except:
        tmmx_lag_4.append(-999)
    try:
        tmmx_lag_5.append(df.loc[(df['date'] == lag_5_day) & (df['clim_div'] == row['clim_div'])]['tmmx_f'].values[0])
    except:
        tmmx_lag_5.append(-999)
    try:
        tmmx_lag_6.append(df.loc[(df['date'] == lag_6_day) & (df['clim_div'] == row['clim_div'])]['tmmx_f'].values[0])
    except:
        tmmx_lag_6.append(-999)
    try:
        tmmx_lag_7.append(df.loc[(df['date'] == lag_7_day) & (df['clim_div'] == row['clim_div'])]['tmmx_f'].values[0])
    except:
        tmmx_lag_7.append(-999)
    try:
        tmmx_lag_8.append(df.loc[(df['date'] == lag_8_day) & (df['clim_div'] == row['clim_div'])]['tmmx_f'].values[0])    
    except:
        tmmx_lag_8.append(-999)
    try:
        tmmx_lag_9.append(df.loc[(df['date'] == lag_9_day) & (df['clim_div'] == row['clim_div'])]['tmmx_f'].values[0])
    except:
        tmmx_lag_9.append(-999)
    try:
        tmmx_lag_10.append(df.loc[(df['date'] == lag_10_day) & (df['clim_div'] == row['clim_div'])]['tmmx_f'].values[0])
    except:
        tmmx_lag_10.append(-999)

    try:    
        rmax_lag_1.append(df.loc[(df['date'] == lag_1_day) & (df['clim_div'] == row['clim_div'])]['rmax'].values[0])
    except:
        rmax_lag_1.append(-999)
    try:
        rmax_lag_2.append(df.loc[(df['date'] == lag_2_day) & (df['clim_div'] == row['clim_div'])]['rmax'].values[0])   
    except:
        rmax_lag_2.append(-999)
    try:
        rmax_lag_3.append(df.loc[(df['date'] == lag_3_day) & (df['clim_div'] == row['clim_div'])]['rmax'].values[0])
    except:
        rmax_lag_3.append(-999)
    try:
        rmax_lag_4.append(df.loc[(df['date'] == lag_4_day) & (df['clim_div'] == row['clim_div'])]['rmax'].values[0])
    except:
        rmax_lag_4.append(-999)
    try:
        rmax_lag_5.append(df.loc[(df['date'] == lag_5_day) & (df['clim_div'] == row['clim_div'])]['rmax'].values[0])
    except:
        rmax_lag_5.append(-999)
    try:
        rmax_lag_6.append(df.loc[(df['date'] == lag_6_day) & (df['clim_div'] == row['clim_div'])]['rmax'].values[0])
    except:
        rmax_lag_6.append(-999)
    try:
        rmax_lag_7.append(df.loc[(df['date'] == lag_7_day) & (df['clim_div'] == row['clim_div'])]['rmax'].values[0])
    except:
        rmax_lag_7.append(-999)
    try:
        rmax_lag_8.append(df.loc[(df['date'] == lag_8_day) & (df['clim_div'] == row['clim_div'])]['rmax'].values[0])
    except:
        rmax_lag_8.append(-999)
    try:
        rmax_lag_9.append(df.loc[(df['date'] == lag_9_day) & (df['clim_div'] == row['clim_div'])]['rmax'].values[0])    
    except:
        rmax_lag_9.append(-999)
    try:
        rmax_lag_10.append(df.loc[(df['date'] == lag_10_day) & (df['clim_div'] == row['clim_div'])]['rmax'].values[0])
    except:
        rmax_lag_10.append(-999)
    
    try:
        heat_index_lag_1.append(df.loc[(df['date'] == lag_1_day) & (df['clim_div'] == row['clim_div'])]['heat_index'].values[0])
    except:
        heat_index_lag_1.append(-999)
    try:
        heat_index_lag_2.append(df.loc[(df['date'] == lag_2_day) & (df['clim_div'] == row['clim_div'])]['heat_index'].values[0])
    except:
        heat_index_lag_2.append(-999)
    try:
        heat_index_lag_3.append(df.loc[(df['date'] == lag_3_day) & (df['clim_div'] == row['clim_div'])]['heat_index'].values[0])
    except:
        heat_index_lag_3.append(-999)
    try:
        heat_index_lag_4.append(df.loc[(df['date'] == lag_4_day) & (df['clim_div'] == row['clim_div'])]['heat_index'].values[0])
    except:
        heat_index_lag_4.append(-999)
    try:
        heat_index_lag_5.append(df.loc[(df['date'] == lag_5_day) & (df['clim_div'] == row['clim_div'])]['heat_index'].values[0])
    except:
        heat_index_lag_5.append(-999)
    try:
        heat_index_lag_6.append(df.loc[(df['date'] == lag_6_day) & (df['clim_div'] == row['clim_div'])]['heat_index'].values[0])
    except:
        heat_index_lag_6.append(-999)
    try:
        heat_index_lag_7.append(df.loc[(df['date'] == lag_7_day) & (df['clim_div'] == row['clim_div'])]['heat_index'].values[0])
    except:
        heat_index_lag_7.append(-999)
    try:
        heat_index_lag_8.append(df.loc[(df['date'] == lag_8_day) & (df['clim_div'] == row['clim_div'])]['heat_index'].values[0])
    except:
        heat_index_lag_8.append(-999)
    try:
        heat_index_lag_9.append(df.loc[(df['date'] == lag_9_day) & (df['clim_div'] == row['clim_div'])]['heat_index'].values[0])
    except:
        heat_index_lag_9.append(-999)
    try:
        heat_index_lag_10.append(df.loc[(df['date'] == lag_10_day) & (df['clim_div'] == row['clim_div'])]['heat_index'].values[0])
    except:
        heat_index_lag_10.append(-999)

df['tmmx_lag_1'] = tmmx_lag_1
df['tmmx_lag_2'] = tmmx_lag_2
df['tmmx_lag_3'] = tmmx_lag_3
df['tmmx_lag_4'] = tmmx_lag_4
df['tmmx_lag_5'] = tmmx_lag_5
df['tmmx_lag_6'] = tmmx_lag_6
df['tmmx_lag_7'] = tmmx_lag_7
df['tmmx_lag_8'] = tmmx_lag_8
df['tmmx_lag_9'] = tmmx_lag_9
df['tmmx_lag_10'] = tmmx_lag_10

df['rmax_lag_1'] = rmax_lag_1
df['rmax_lag_2'] = rmax_lag_2
df['rmax_lag_3'] = rmax_lag_3
df['rmax_lag_4'] = rmax_lag_4
df['rmax_lag_5'] = rmax_lag_5
df['rmax_lag_6'] = rmax_lag_6
df['rmax_lag_7'] = rmax_lag_7
df['rmax_lag_8'] = rmax_lag_8
df['rmax_lag_9'] = rmax_lag_9
df['rmax_lag_10'] = rmax_lag_10

df['heat_index_lag_1'] = heat_index_lag_1
df['heat_index_lag_2'] = heat_index_lag_2
df['heat_index_lag_3'] = heat_index_lag_3
df['heat_index_lag_4'] = heat_index_lag_4
df['heat_index_lag_5'] = heat_index_lag_5
df['heat_index_lag_6'] = heat_index_lag_6
df['heat_index_lag_7'] = heat_index_lag_7
df['heat_index_lag_8'] = heat_index_lag_8
df['heat_index_lag_9'] = heat_index_lag_9
df['heat_index_lag_10'] = heat_index_lag_10


#df_subset['date']=pd.to_datetime(df_subset['date'])
#df_subset = df_subset.drop(['tmmx_k', 'tmmx_c', 'tmmx_f', 'rmax', 'heat_index', 'death_count', 'tot_pop', 'dow', 'year', 'doy', 'time'], axis=1)
#df_final = df.join(df_subset, on=['date', 'clim_div'])
df.to_csv("G:\My Drive\Year 2\Thesis\Data\\1979-1988\\all_data\\all_data_weather_mortality_population_dow_lags.csv", index=False, index_label=False)