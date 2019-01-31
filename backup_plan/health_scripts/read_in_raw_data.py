import pandas as pd

# applies to 1968-1978
filename='G:/My Drive/Year 2/Thesis/Backup_Plan/mortality/raw_data/mort1978us/Mort78'
df = pd.read_fwf(filename, colspecs=[(0, 1), (25, 27), (27, 30), (30, 32), (32, 34), (59, 63)], names=["year_of_death", "state_fips", "county_fips", "month_of_death", "date_of_death", "underlying"])
print("done reading colspecs")
df = df.loc[df['state_fips'] == 47]
print("done subsetting for VA")
df.to_csv("C:/Users/ginal/Documents/GitHub/masters-thesis/backup_plan/data_1978.csv")
print("done writing out to csv")

# applies to 1979
filename='G:/My Drive/Year 2/Thesis/Backup_Plan/mortality/raw_data/mort1979us/Vs79mort'
df = pd.read_fwf(filename, colspecs=[(0, 2), (20, 22), (22, 25), (26, 28), (54, 56), (56, 58), (141, 145)], names=["year_of_death", "state_fips", "county_fips", "division_state", "month_of_death", "date_of_death", "underlying"])
print("done reading colspecs")
df = df.loc[df['state_fips'] == 47]
print("done subsetting for VA")
df.to_csv("C:/Users/ginal/Documents/GitHub/masters-thesis/backup_plan/data_1979.csv")
print("done writing out to csv")

# applies to 1980
filename='G:/My Drive/Year 2/Thesis/Backup_Plan/mortality/raw_data/mort1980us/Vs80mort'
# year_of_death, state_fips, county_fips, division_state, month_of_death, date_of_death, underlying
df = pd.read_fwf(filename, colspecs=[(0, 2), (20, 22), (22, 25), (25, 27), (54, 56), (56, 58), (141, 145)], names=["year_of_death", "state_fips", "county_fips", "division_state", "month_of_death", "date_of_death", "underlying"])
print("done reading colspecs")
df = df.loc[df['state_fips'] == 47]
print("done subsetting for VA")
df.to_csv("C:/Users/ginal/Documents/GitHub/masters-thesis/backup_plan/data_1980.csv")
print("done writing out to csv")

# applies to 1981
filename='G:/My Drive/Year 2/Thesis/Backup_Plan/mortality/raw_data/mort1981us/Vs81mort'
# year_of_death, state_fips, county_fips, division_state, month_of_death, date_of_death, underlying
df = pd.read_fwf(filename, colspecs=[(0, 2), (20, 22), (22, 25), (25, 27), (54, 56), (56, 58), (141, 145)], names=["year_of_death", "state_fips", "county_fips", "division_state", "month_of_death", "date_of_death", "underlying"])
print("done reading colspecs")
df = df.loc[df['state_fips'] == 47]
print("done subsetting for VA")
df.to_csv("C:/Users/ginal/Documents/GitHub/masters-thesis/backup_plan/data_1981.csv")
print("done writing out to csv")

# applies to 1982
filename='G:/My Drive/Year 2/Thesis/Backup_Plan/mortality/raw_data/mort1982us/Vs82mort'
# year_of_death, state_fips, county_fips, division_state, month_of_death, date_of_death, underlying
df = pd.read_fwf(filename, colspecs=[(0, 2), (20, 22), (22, 25), (25, 27), (54, 56), (56, 58), (141, 145)], names=["year_of_death", "state_fips", "county_fips", "division_state", "month_of_death", "date_of_death", "underlying"])
print("done reading colspecs")
df = df.loc[df['state_fips'] == 47]
print("done subsetting for VA")
df.to_csv("C:/Users/ginal/Documents/GitHub/masters-thesis/backup_plan/data_1982.csv")
print("done writing out to csv")

# applies to 1983
filename='G:/My Drive/Year 2/Thesis/Backup_Plan/mortality/raw_data/mort1983us/Vs83mort'
# year_of_death, state_fips, county_fips, division_state, month_of_death, date_of_death, underlying
df = pd.read_fwf(filename, colspecs=[(0, 2), (20, 22), (22, 25), (25, 27), (54, 56), (56, 58), (141, 145)], names=["year_of_death", "state_fips", "county_fips", "division_state", "month_of_death", "date_of_death", "underlying"])
print("done reading colspecs")
df = df.loc[df['state_fips'] == 47]
print("done subsetting for VA")
df.to_csv("C:/Users/ginal/Documents/GitHub/masters-thesis/backup_plan/data_1983.csv")
print("done writing out to csv")

# applies to 1984
filename='G:/My Drive/Year 2/Thesis/Backup_Plan/mortality/raw_data/mort1984us/Vs84mort'
# year_of_death, state_fips, county_fips, division_state, month_of_death, date_of_death, underlying
df = pd.read_fwf(filename, colspecs=[(0, 2), (20, 22), (22, 25), (25, 27), (54, 56), (56, 58), (141, 145)], names=["year_of_death", "state_fips", "county_fips", "division_state", "month_of_death", "date_of_death", "underlying"])
print("done reading colspecs")
df = df.loc[df['state_fips'] == 47]
print("done subsetting for VA")
df.to_csv("C:/Users/ginal/Documents/GitHub/masters-thesis/backup_plan/data_1984.csv")
print("done writing out to csv")

# applies to 1985
filename='G:/My Drive/Year 2/Thesis/Backup_Plan/mortality/raw_data/mort1985us/MORT85.PUB'
# year_of_death, state_fips, county_fips, division_state, month_of_death, date_of_death, underlying
df = pd.read_fwf(filename, colspecs=[(0, 2), (20, 22), (22, 25), (25, 27), (54, 56), (56, 58), (141, 145)], names=["year_of_death", "state_fips", "county_fips", "division_state", "month_of_death", "date_of_death", "underlying"])
print("done reading colspecs")
df = df.loc[df['state_fips'] == 47]
print("done subsetting for VA")
df.to_csv("C:/Users/ginal/Documents/GitHub/masters-thesis/backup_plan/data_1985.csv")
print("done writing out to csv")

# applies to 1986
filename='G:/My Drive/Year 2/Thesis/Backup_Plan/mortality/raw_data/mort1986us/MORT86.PUB'
# year_of_death, state_fips, county_fips, division_state, month_of_death, date_of_death, underlying
df = pd.read_fwf(filename, colspecs=[(0, 2), (20, 22), (22, 25), (25, 27), (54, 56), (56, 58), (141, 145)], names=["year_of_death", "state_fips", "county_fips", "division_state", "month_of_death", "date_of_death", "underlying"])
print("done reading colspecs")
df = df.loc[df['state_fips'] == 47]
print("done subsetting for VA")
df.to_csv("C:/Users/ginal/Documents/GitHub/masters-thesis/backup_plan/data_1986.csv")
print("done writing out to csv")

# applies to 1987
filename='G:/My Drive/Year 2/Thesis/Backup_Plan/mortality/raw_data/mort1987us/MORT87.PUB'
# year_of_death, state_fips, county_fips, division_state, month_of_death, date_of_death, underlying
df = pd.read_fwf(filename, colspecs=[(0, 2), (20, 22), (22, 25), (25, 27), (54, 56), (56, 58), (141, 145)], names=["year_of_death", "state_fips", "county_fips", "division_state", "month_of_death", "date_of_death", "underlying"])
print("done reading colspecs")
df = df.loc[df['state_fips'] == 47]
print("done subsetting for VA")
df.to_csv("C:/Users/ginal/Documents/GitHub/masters-thesis/backup_plan/data_1987.csv")
print("done writing out to csv")

# applies to 1988
filename='G:/My Drive/Year 2/Thesis/Backup_Plan/mortality/raw_data/mort1988us/Vs88mort'
# year_of_death, state_fips, county_fips, division_state, month_of_death, date_of_death, underlying
df = pd.read_fwf(filename, colspecs=[(0, 2), (20, 22), (22, 25), (25, 27), (54, 56), (56, 58), (141, 145)], names=["year_of_death", "state_fips", "county_fips", "division_state", "month_of_death", "date_of_death", "underlying"])
print("done reading colspecs")
df = df.loc[df['state_fips'] == 47]
print("done subsetting for VA")
df.to_csv("C:/Users/ginal/Documents/GitHub/masters-thesis/backup_plan/data_1988.csv")
print("done writing out to csv")

