from reminder.job import *
from datetime import datetime
from forecaster.solveathon_forecaster import predict

days = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
}

day_of_the_week = datetime.today().weekday()

pred = predict([0, 11, days[day_of_the_week], 'Ratna'])
message = "It is {0} outside".format(pred)

messsage_viber_subscribers(message)

log = open('reminder_logs.txt', 'a')
log.write('\nSend on ' + str(datetime.now()))
