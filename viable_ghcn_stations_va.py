import csv
import pandas as pd
from geopandas import GeoDataFrame
from shapely.geometry import Point

def get_viable_ghcn_stations():
    stations = ['USC00440021', 'USC00440187', 'USC00440188', 'USC00440243', 'USC00440327', 'USC00440385', 'USC00440551', 'USC00440561', 'USC00440720', 'USC00440735', 'USC00440766', 'USC00440792', 'USC00440860', 'USC00440982', 'USC00440993', 'USC00441082', 'USC00441121', 'USC00441159', 'USC00441209', 'USC00441322', 'USC00441434', 'USC00441585', 'USC00441593', 'USC00441606', 'USC00441614', 'USC00441692', 'USC00441746', 'USC00441825', 'USC00441913', 'USC00441955', 'USC00441986', 'USC00441999', 'USC00442009', 'USC00442044', 'USC00442142', 'USC00442155', 'USC00442208', 'USC00442245', 'USC00442400', 'USC00442600', 'USC00442635', 'USC00442663', 'USC00442790', 'USC00442941', 'USC00443006', 'USC00443071', 'USC00443192', 'USC00443204', 'USC00443213', 'USC00443229', 'USC00443267', 'USC00443272', 'USC00443310', 'USC00443375', 'USC00443466', 'USC00443468', 'USC00443565', 'USC00443640', 'USC00443713', 'USC00444039', 'USC00444044', 'USC00444101', 'USC00444128', 'USC00444148', 'USC00444410', 'USC00444414', 'USC00444568', 'USC00444600', 'USC00444692', 'USC00444768', 'USC00444777', 'USC00444876', 'USC00444909', 'USC00445050', 'USC00445096', 'USC00445117', 'USC00445150', 'USC00445204', 'USC00445271', 'USC00445300', 'USC00445338', 'USC00445453', 'USC00445595', 'USC00445685', 'USC00445690', 'USC00445698', 'USC00445700', 'USC00445756', 'USC00445828', 'USC00445833', 'USC00445851', 'USC00445880', 'USC00446125', 'USC00446147', 'USC00446161', 'USC00446173', 'USC00446470', 'USC00446475', 'USC00446491', 'USC00446593', 'USC00446626', 'USC00446656', 'USC00446692', 'USC00446712', 'USC00446955', 'USC00446999', 'USC00447130', 'USC00447174', 'USC00447278', 'USC00447338', 'USC00447506', 'USC00447541', 'USC00447904', 'USC00447925', 'USC00447985', 'USC00448022', 'USC00448046', 'USC00448062', 'USC00448084', 'USC00448129', 'USC00448170', 'USC00448192', 'USC00448323', 'USC00448396', 'USC00448448', 'USC00448547', 'USC00448600', 'USC00448737', 'USC00448800', 'USC00448829', 'USC00448837', 'USC00448888', 'USC00448894', 'USC00448902', 'USC00448941', 'USC00449025', 'USC00449151', 'USC00449169', 'USC00449181', 'USC00449186', 'USC00449215', 'USC00449263', 'USC00449301']
    viable = []

    va_stations = pd.read_csv('va-ghcn-stations.csv')
    print(va_stations)

    for index, row in va_stations.iterrows():
        if row['station_name'] in stations:
            viable.append(1)
        else:
            viable.append(0)
    va_stations['viable'] = viable
    print(va_stations)
    va_stations_viable = va_stations[va_stations['viable'] == 1]
    print(va_stations_viable)

    geometry = [Point(xy) for xy in zip(va_stations_viable.lon, va_stations_viable.lat)]
    df = va_stations_viable.drop(['lon', 'lat'], axis=1)
    crs = {'init': 'epsg:4326'}
    gdf = GeoDataFrame(va_stations_viable, crs=crs, geometry=geometry)
    print(gdf)

    gdf.to_file('va_ghcn_stations_viable.shp', driver='ESRI Shapefile')

def get_viable_isd_stations():
    colnames=['USAF', 'WBAN', 'Global_Hourly_Number', 'STATION_NAME', 'CT', 'ST', 'CALL', 'LAT', 'LON', 'ELEV(M)', 'BEGIN', 'END']
    isd_df = pd.read_csv('va-isd-stations.csv', names=colnames, header=None)
    
    isd_df = isd_df.iloc[1:]
    isd_df["LON"].convert_objects(convert_numeric=True)
    isd_df["LAT"].convert_objects(convert_numeric=True)
    import IPython
    IPython.embed()
    geometry = [Point(xy) for xy in zip(isd_df.LON, isd_df.LAT)]
    #isd_df = isd_df.drop(['LON', 'LAT'], axis=1)
    crs = {'init': 'epsg:4326'}
    gdf = GeoDataFrame(isd_df, crs=crs, geometry=geometry)
    print(gdf)

    gdf.to_file('va_ghcn_stations_viable.shp', driver='ESRI Shapefile')


if __name__ == "__main__":
    #get_viable_ghcn_stations()
    get_viable_isd_stations()

