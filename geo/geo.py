from geopy.geocoders import Nominatim
from geopy import distance
from constants import station_names, station_locations


def get_nearest_station_name(point, stations):
    distances = []
    for station in stations:
        calc_distance = distance.distance(
            station, point).km

        distances.append(calc_distance)
    index = stations.index(min(stations))
    return station_names[index]


def get_location_from_address(address):
    geolocator = Nominatim(user_agent="hawa-ko-bot")
    location = geolocator.geocode(address)
    return location
