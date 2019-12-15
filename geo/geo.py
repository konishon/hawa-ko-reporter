from geopy.geocoders import Nominatim
from geopy import distance
from constants import station_names, station_locations

from geopy.extra.rate_limiter import RateLimiter
import geopy


def get_nearest_station_name(point, stations):
    distances = []
    for station in stations:
        calc_distance = distance.distance(
            station, point).km

        distances.append(calc_distance)
    
    index = stations.index(min(stations))
    # print(distances)
    
    item_value = min(distances)
    # print(item_value)

    index  = distances.index(item_value)
    # print(index)
    print(station_names[index])

    return station_names[index]


def get_location_from_address(address):
    geopy.geocoders.options.default_timeout = 7
    geolocator = Nominatim(user_agent="hawa-ko-bot")
    location = geolocator.geocode(address)
    return location