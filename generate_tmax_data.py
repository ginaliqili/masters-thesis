import pandas
import urllib.request
from urllib.parse import unquote
import ast
import json
import pprint
from datetime import datetime, timedelta
import calendar
import time
from multiprocessing import Pool

def get_tmax_data():
    # Get VA station ids in GHCN, 416 in total
    colnames=['station_na', 'lat', 'lon', 'elevation', 'state', 'viable']
    ghcn_df = pandas.read_csv('viable-va-ghcn-stations.csv', names=colnames)
    ghcn_stations = ghcn_df.station_na.tolist()
    ghcn_stations = ghcn_stations[2:]
    lat_list = ghcn_df.lat.tolist()
    lat_list = lat_list[1:]
    lon_list = ghcn_df.lon.tolist()
    lon_list = lon_list[1:]
    print(str(len(ghcn_stations)) + " viable GHCN stations in VA in total during study time period")

    # Get daily tmax from 1989 to 2015 from every station, one file per day
    #ghcn_stations_str1 = ",".join(['USC00445300'])
    ghcn_stations_str1 = ",".join(ghcn_stations[:100])
    ghcn_stations_str2 = ",".join(ghcn_stations[100:])
    start_date = datetime.strptime('2013-05-01', '%Y-%M-%d')
    dates = []
    station_names = []
    tmaxes = []
    # 9861
    for year in range(1990, 2017+1):
            if calendar.isleap(year):
                month_end_list = [1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336]
                end_date = 366
            else:
                month_end_list = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
                end_date = 365
            cadence = range(1, end_date+1)
            # Iterate over all dates in year
            for julian_day in cadence:
                print("Retrieving data sets for year " + str(year) + " and julian day " + str(julian_day))
                # get all the tmax data for all va stations
                julian_day_str = str(year) + str(julian_day)
                print(julian_day_str)
                month_date_obj = datetime.strptime(julian_day_str, '%Y%j').date()
                month_date_str = str(month_date_obj)
                print(month_date_str)
        
                url1 = "https://www.ncdc.noaa.gov/access-data-service/api/v1/data?dataset=daily-summaries&dataTypes=TMAX&stations={}&startDate={}&endDate={}&includeAttributes=true&format=json".format(ghcn_stations_str1, month_date_str, month_date_str)
                url2 = "https://www.ncdc.noaa.gov/access-data-service/api/v1/data?dataset=daily-summaries&dataTypes=TMAX&stations={}&startDate={}&endDate={}&includeAttributes=true&format=json".format(ghcn_stations_str2, month_date_str, month_date_str)
                print(url1)
                print(url2)
                response = urllib.request.urlopen(url1)
                response_str = response.read().decode("utf-8")
                response_json = json.loads(response_str)
                if len(response_json) > 0:
                    for x in response_json:
                        dates.append(x['DATE'])
                        station_names.append(x['STATION'])
                        tmax = ((float(x['TMAX'])*0.1)*1.8) + 32
                        tmaxes.append(tmax)

                
                response = urllib.request.urlopen(url2)
                response_str = response.read().decode("utf-8")
                response_json = json.loads(response_str)
                if len(response_json) > 0:
                    for x in response_json:
                        dates.append(x['DATE'])
                        station_names.append(x['STATION'])
                        tmax = ((float(x['TMAX'])*0.1)*1.8) + 32
                        tmaxes.append(tmax)
                
    tmax_df = pandas.DataFrame(
        {'Date': dates,
        'Station': station_names,
        'Tmax': tmaxes
        })
    tmax_df.to_csv('tmax_data_1990-2017.csv', index=False)

def get_tmax_data2(start_year):
    # Get VA station ids in GHCN, 416 in total
    colnames=['station_na', 'lat', 'lon', 'elevation', 'state', 'viable']
    ghcn_df = pandas.read_csv('viable-va-ghcn-stations.csv', names=colnames)
    ghcn_stations = ghcn_df.station_na.tolist()
    ghcn_stations = ghcn_stations[2:]
    lat_list = ghcn_df.lat.tolist()
    lat_list = lat_list[1:]
    lon_list = ghcn_df.lon.tolist()
    lon_list = lon_list[1:]
    print(str(len(ghcn_stations)) + " viable GHCN stations in VA in total during study time period")

    # Get daily tmax from 1989 to 2015 from every station, one file per day
    #ghcn_stations_str1 = ",".join(['USC00445300'])
    ghcn_stations_str1 = ",".join(ghcn_stations[:100])
    ghcn_stations_str2 = ",".join(ghcn_stations[100:])
    start_date = datetime.strptime('2013-05-01', '%Y-%M-%d')
    dates = []
    station_names = []
    tmaxes = []
    # 9861
    for year in range(start_year, start_year+1):
            if calendar.isleap(year):
                month_end_list = [1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336]
                end_date = 366
            else:
                month_end_list = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
                end_date = 365
            cadence = range(1, end_date+1)
            # Iterate over all dates in year
            for julian_day in cadence:
                print("Retrieving data sets for year " + str(year) + " and julian day " + str(julian_day))
                # get all the tmax data for all va stations
                julian_day_str = str(year) + str(julian_day)
                print(julian_day_str)
                month_date_obj = datetime.strptime(julian_day_str, '%Y%j').date()
                month_date_str = str(month_date_obj)
                print(month_date_str)
        
                url1 = "https://www.ncdc.noaa.gov/access-data-service/api/v1/data?dataset=daily-summaries&dataTypes=TMAX&stations={}&startDate={}&endDate={}&includeAttributes=true&format=json".format(ghcn_stations_str1, month_date_str, month_date_str)
                url2 = "https://www.ncdc.noaa.gov/access-data-service/api/v1/data?dataset=daily-summaries&dataTypes=TMAX&stations={}&startDate={}&endDate={}&includeAttributes=true&format=json".format(ghcn_stations_str2, month_date_str, month_date_str)
                print(url1)
                print(url2)
                response = urllib.request.urlopen(url1)
                response_str = response.read().decode("utf-8")
                response_json = json.loads(response_str)
                if len(response_json) > 0:
                    for x in response_json:
                        dates.append(x['DATE'])
                        station_names.append(x['STATION'])
                        tmax = ((float(x['TMAX'])*0.1)*1.8) + 32
                        tmaxes.append(tmax)

                
                response = urllib.request.urlopen(url2)
                response_str = response.read().decode("utf-8")
                response_json = json.loads(response_str)
                if len(response_json) > 0:
                    for x in response_json:
                        dates.append(x['DATE'])
                        station_names.append(x['STATION'])
                        tmax = ((float(x['TMAX'])*0.1)*1.8) + 32
                        tmaxes.append(tmax)
                
    tmax_df = pandas.DataFrame(
        {'Date': dates,
        'Station': station_names,
        'Tmax': tmaxes
        })
    tmax_df.to_csv('tmax_data_1990-2017.csv', index=False)

def get_rh_data():
    colnames=['USAF', 'WBAN', 'API_Station', 'STATION_NAME', 'CT', 'ST', 'CALL', 'LAT', 'LON', 'ELEV_M', 'BEGIN', 'END']
    gh_df = pandas.read_csv('Viable-Va-Global-Hourly-Stations.csv', names=colnames)
    gh_stations = gh_df.API_Station.tolist()
    gh_stations = gh_stations[1:]
    lat_list = gh_df.LAT.tolist()
    lat_list = lat_list[1:]
    lon_list = gh_df.LON.tolist()
    lon_list = lon_list[1:]
    print(str(len(gh_stations)) + " viable GH stations in VA in total during study time period")

    # Get daily tmax from 1989 to 2015 from every station, one file per day
    #ghcn_stations_str1 = ",".join(['USC00445300'])
    gh_stations_str1 = ",".join(gh_stations[:100])
    gh_stations_str2 = ",".join(gh_stations[100:])
    #start_date = datetime.strptime('2013-01-01', '%Y-%M-%d')
    dates = []
    station_names = []
    rhs = []
    # 9861
    for year in range(1990, 2017+1):
            if calendar.isleap(year):
                end_date = 366
                month_end_list = [1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336]
            else:
                end_date = 365
                month_end_list = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
            cadence = range(1, end_date+1)
            # Iterate over all dates in year
            for julian_day in cadence:
                print("Retrieving data sets for year " + str(year) + " and julian day " + str(julian_day))
                # get all the tmax data for all va stations
                julian_day_str = str(year) + str(julian_day)
                print(julian_day_str)
                month_date_obj = datetime.strptime(julian_day_str, '%Y%j').date()
                month_date_str = str(month_date_obj)
                print(month_date_str)
        
                url1 = "https://www.ncdc.noaa.gov/access-data-service/api/v1/data?dataset=global-hourly&dataTypes=RH1&stations={}&startDate={}&endDate={}&includeAttributes=true&format=json".format(gh_stations_str1, month_date_str, month_date_str)
                url2 = "https://www.ncdc.noaa.gov/access-data-service/api/v1/data?dataset=global-hourly&dataTypes=RH1&stations={}&startDate={}&endDate={}&includeAttributes=true&format=json".format(gh_stations_str2, month_date_str, month_date_str)
                print(url1)
                print(url2)
                response = urllib.request.urlopen(url1)
                response_str = response.read().decode("utf-8")
                response_json = json.loads(response_str)
                if len(response_json) > 0:
                    for x in response_json:
                        dates.append(x['DATE'])
                        station_names.append(x['STATION'])
                        rh = x['RH1'].split(',')[0]
                        rhs.append(rh)

                
                response = urllib.request.urlopen(url2)
                response_str = response.read().decode("utf-8")
                response_json = json.loads(response_str)
                if len(response_json) > 0:
                    for x in response_json:
                        dates.append(x['DATE'])
                        station_names.append(x['STATION'])
                        rh = x['RH1'].split(',')[0]
                        rhs.append(rh)          

    rh_df = pandas.DataFrame(
        {'Date': dates,
        'Station': station_names,
        'RH': rhs
        })
    rh_df.to_csv('rh_data_daily2015.csv', index=False)

if __name__ == "__main__":
    years = [y for y in range(1990, 2016)]
    with Pool(5) as p:
        print(p.map(get_tmax_data2, years))

    #get_tmax_data()
    #get_rh_data()
    
