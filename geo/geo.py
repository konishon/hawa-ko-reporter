from geopy.geocoders import Nominatim
from geopy import distance
from constants import station_names, station_locations

from geopy.extra.rate_limiter import RateLimiter


def get_nearest_station_name(point, stations):
    distances = []
    for station in stations:
        calc_distance = distance.distance(
            station, point).km

        distances.append(calc_distance)
    index = stations.index(min(stations))
    return station_names[index]


def get_location_from_address(address):
    geolocator = Nominatim(user_agent="hawa-ko-bot",
                           country_codes='np', timeout=6)
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    location = geolocator.geocode(address)
    return location
