from crontab import CronTab
import os

cron = CronTab(os.environ['USER'])
job = cron.new(command='python run_reminder.py')
job.minute.every(1)

cron.write()