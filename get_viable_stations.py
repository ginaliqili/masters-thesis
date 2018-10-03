import pandas
import urllib.request
from urllib.parse import unquote
import ast
import json

def get_tmax_data():
    # Get VA station ids in GHCN, 416 in total
    colnames=['station', 'lat', 'long', 'elev', 'state']
    ghcn_df = pandas.read_csv('va-ghcn-stations.csv', names=colnames)
    ghcn_stations = ghcn_df.station.tolist()
    print(str(len(ghcn_stations)) + " GHCN stations in VA")

    # Get daily tmax from 1989 to 2015 from each station
    viable_stations = []
    count = 0
    for station_id in ghcn_stations:
        count += 1
        print("station number " + str(count))
        url = "https://www.ncdc.noaa.gov/access-data-service/api/v1/data?dataset=daily-summaries&dataTypes=TMAX&stations={}&startDate=1989-01-01&endDate=2015-12-31&includeAttributes=true&format=json".format(station_id)
        response = urllib.request.urlopen(url)
        response_str = response.read().decode("utf-8")
        response_json = json.loads(response_str)
        print(str(len(response_json)) + " data points")

        if len(response_json) > 0:
            viable_stations.append(station_id)

    print(viable_stations)

def get_humidity_data():
    # Get VA station ids in ISD, 161 in total
    colnames=['USAF', 'WBAN', 'Global_Hourly_Number', 'STATION_NAME', 'CT', 'ST', 'CALL', 'LAT', 'LON', 'ELEV(M)', 'BEGIN', 'END']
    isd_df = pandas.read_csv('va-isd-stations.csv', names=colnames)
    isd_stations = isd_df.Global_Hourly_Number.tolist()
    print(str(len(isd_stations)) + " ISD stations in VA")

    # Get daily relative humidity from 1989 to 2015 from each station
    viable_stations = []
    count = 0
    for isd_station in isd_stations:
        count += 1
        print("station number " + str(count))
        url = "https://www.ncdc.noaa.gov/access-data-service/api/v1/data?dataset=global-hourly&dataTypes=RH1&stations={}&startDate=1989-01-01&endDate=2015-12-31&includeAttributes=true&format=json".format(isd_station)
        print(url)
        response = urllib.request.urlopen(url)
        response_str = response.read().decode("utf-8")
        response_json = json.loads(response_str)
        print(str(len(response_json)) + " data points")

        if len(response_json) > 0:
            viable_stations.append(isd_station)
    print(viable_stations)



if __name__ == "__main__":
    #get_tmax_data()
    #get_humidity_data()
    
