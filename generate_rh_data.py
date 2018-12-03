import pandas as pd
import urllib.request
from urllib.parse import unquote
import json
import pprint
from datetime import datetime, timedelta
import calendar
import time
from multiprocessing import Pool
import time
import statistics

def get_rh3_data(start_year):
    colnames=['USAF', 'WBAN', 'API_Station', 'STATION_NAME', 'CT', 'ST', 'CALL', 'LAT', 'LON', 'ELEV_M', 'BEGIN', 'END']
    gh_df = pd.read_csv('VA-Global-Hourly-Stations.csv', names=colnames)
    gh_stations = gh_df.API_Station.tolist()
    gh_stations = gh_stations[1:]
    lat_list = gh_df.LAT.tolist()
    lat_list = lat_list[1:]
    lon_list = gh_df.LON.tolist()
    lon_list = lon_list[1:]
    print(str(len(gh_stations)) + " viable GH stations in VA in total during study time period")

    # Get daily relative humidity from 1990 to 2016 from every station, one file per day
    gh_stations_str1 = ",".join(gh_stations[:100])
    gh_stations_str2 = ",".join(gh_stations[100:])

    #gh_stations_str1 = ",".join(gh_stations[:2])
    #gh_stations_str2 = ",".join(gh_stations[2:40])

    # 9861
    for year in range(start_year, start_year+1):
            if calendar.isleap(year):
                end_date = 366
                month_end_list = [1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336]
            else:
                end_date = 365
                month_end_list = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
            cadence = range(1, end_date+1)
            # Iterate over all dates in year
            '''
            dp_df = pd.DataFrame()
            dp_df['station'] = []
            dp_df['date'] = []
            dp_df['dp'] = []
            '''

            stations = []
            dates = []
            dps = []

            for julian_day in cadence:
                
                print("Retrieving data sets for year " + str(year) + " and julian day " + str(julian_day))
                # get all the tmax data for all va stations
                julian_day_str = str(year) + str(julian_day)
                print(julian_day_str)
                month_date_obj = datetime.strptime(julian_day_str, '%Y%j').date()
                month_date_str = str(month_date_obj)
                print(month_date_str)
        
                url1 = "https://www.ncdc.noaa.gov/access-data-service/api/v1/data?dataset=global-hourly&dataTypes=DEW&stations={}&startDate={}&endDate={}&includeAttributes=true&format=json".format(gh_stations_str1, month_date_str, month_date_str)
                url2 = "https://www.ncdc.noaa.gov/access-data-service/api/v1/data?dataset=global-hourly&dataTypes=DEW&stations={}&startDate={}&endDate={}&includeAttributes=true&format=json".format(gh_stations_str2, month_date_str, month_date_str)
                print(url1)
                print(url2)
                response = urllib.request.urlopen(url1)
                response_str = response.read().decode("utf-8")
                response_json = json.loads(response_str)
                if len(response_json) > 0:
                    for x in response_json:
                        dp_flag = x['DEW'].split(',')[1]
                        if dp_flag != '2' and dp_flag != '3' and dp_flag != '6' and dp_flag != '7':
                            station = x['STATION']
                            dp = int(x['DEW'].split(',')[0])
                            date = x['DATE'][:10]
                            stations.append(station)
                            dates.append(date)
                            dps.append(dp)

                        
                response = urllib.request.urlopen(url2)
                response_str = response.read().decode("utf-8")
                response_json = json.loads(response_str)
                if len(response_json) > 0:
                    for x in response_json:
                        dp_flag = x['DEW'].split(',')[1]
                        if dp_flag != '2' and dp_flag != '3' and dp_flag != '6' and dp_flag != '7':
                            station = x['STATION']
                            dp = int(x['DEW'].split(',')[0])
                            date = x['DATE'][:10]
                            stations.append(station)
                            dates.append(date)
                            dps.append(dp)      

            dp_df = pd.DataFrame({
                'station': stations,
                'date': dates,
                'dp': dps
            })
            dp_df_no_nas = dp_df.loc[dp_df['dp'] != 9999]
            dp_df_no_nas['dp'] = dp_df_no_nas['dp'].apply(lambda x: x*0.1)
            #dp_avg_df = dp_df_no_nas.groupby(by=['date', 'station']).mean().reset_index()
            dp_avg_df = dp_df_no_nas.groupby(by=['date', 'station']).max().reset_index()

    dp_avg_df.to_csv('C:\\Users\\ginal\Documents\\thesis_data\\DP_max_adj\\rh_data_' + str(start_year) + '.csv', index=False)

if __name__ == "__main__":
    
    '''
    years = [y for y in range(2014, 2017)]
    
    with Pool() as p:
        p.map(get_rh3_data, years)
    '''
    get_rh3_data(2014) 