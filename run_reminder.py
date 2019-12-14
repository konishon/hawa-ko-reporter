from reminder.job import *
from datetime import datetime

messsage_viber_subscribers()

log = open('reminder_logs.txt', 'a') 
log.write('\nSend on ' + str(datetime.now()))