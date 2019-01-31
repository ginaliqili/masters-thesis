import pandas as pd

df = pd.read_csv("G:\\My Drive\\Year 2\\Thesis\\Backup_Plan\\demographic\\raw_data\\va_1980s_by_race.csv")

df2 = df.groupby(['Year of Estimate', 'FIPS State and County Codes']).agg(sum)
df2['total population'] = df2.sum(axis=1)
df2.to_csv("G:\\My Drive\\Year 2\\Thesis\\Backup_Plan\\demographic\\raw_data\\va_1980s_agg.csv")