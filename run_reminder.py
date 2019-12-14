from reminder.job import *
from datetime import datetime
from forecaster.solveathon_forecaster import predict
from geopy.geocoders import Nominatim
from geopy import distance


days = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
}

station_names = [
    'Shankha Park, Kathmandu',
    'Ratna',
    'Bsainik',
    'Pulchowk',
    'Emb',
    'Bpati',
    'Phora',
]
station_locations = [
    (27.73457, 85.342576),
    (27.7,  85.31),
    (27.673762, 85.417528),
    (27.682581, 85.318841),
    (27.738703000000005, 85.336205),
    (27.653109999999998, 85.302252),
    (27.712463, 85.315704)
]


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

location = get_location_from_address("Balkumari")
station_name = get_nearest_station_name((location.latitude, location.longitude), station_locations)

day_of_the_week = datetime.today().weekday()

pred = predict([0, 11, days[day_of_the_week], station_name])
message = "It is {0} for {1}".format(pred,station_name)

messsage_viber_subscribers(message)

log = open('reminder_logs.txt', 'a')
log.write('\nSend on ' + str(datetime.now()))


print(location.latitude, location.longitude)
