import pandas
import urllib.request
from urllib.parse import unquote

# Get VA station ids in GHCN, 416 in total
colnames=['station', 'lat', 'long', 'elev', 'state']
ghcn_df = pandas.read_csv('va-ghcn-stations.csv', names=colnames)
ghcn_stations = ghcn_df.station.tolist()
print(len(ghcn_stations))

# Get daily tmax from 1989 to 2015 from each station
tmax_results = {}
for station_id in ghcn_stations:
    url = "https://www.ncdc.noaa.gov/access-data-service/api/v1/data?dataset=daily-summaries&dataTypes=TMAX&stations={}&startDate=1989-01-01&endDate=2015-12-31&includeAttributes=true&format=json".format(station_id)
    response = urllib.request.urlopen(url)
    if len(response.read().decode("utf-8")) > 0:
        print(len(response.read().decode("utf-8")))
        tmax_results['station_id'] = station_id
        for item in response.read():
            tmax_results['station_id']['date'] = item['DATE']
            tmax_results['station_id']['date']['tmax'] = item['TMAX']

# Get VA station ids in ISD, 161 in total
colnames=['USAF', 'WBAN', 'Global-Hourly Number', 'STATION NAME', 'CT', 'ST', 'CALL', 'LAT', 'LON', 'ELEV(M)', 'BEGIN', 'END']
isd_df = pandas.read_csv('va-isd-stations.csv', names=colnames)
isd_stations = isd_df.station.tolist()
print(len(isd_stations))

# Get daily relative humidity from 1989 to 2015 from each station
for isd_station in isd_stations:
    url = "https://www.ncdc.noaa.gov/access-data-service/api/v1/data?dataset=daily-summaries&dataTypes=TMAX&stations={}&startDate=1989-01-01&endDate=2015-12-31&includeAttributes=true&format=json".format(station_id)
    response = urllib.request.urlopen(url)
    if len(response.read().decode("utf-8")) > 0:
        print(len(response.read().decode("utf-8")))
        tmax_results['station_id'] = station_id
        for item in response.read():
            tmax_results['station_id']['date'] = item['DATE']
            tmax_results['station_id']['date']['tmax'] = item['TMAX']
            

    
