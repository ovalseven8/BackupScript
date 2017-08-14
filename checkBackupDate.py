#!/usr/bin/env python3

import datetime
import subprocess
import sys
from config import BACKUP_DATE_FILE_PATH, NUMBER_OF_DAYS


def desktop_notification(message):
    subprocess.Popen(['notify-send', 'Backup script', message, '--icon=dialog-warning'])

today = datetime.date.today()

try:
    with open(BACKUP_DATE_FILE_PATH, "r") as date_file:
        backup_date = datetime.datetime.strptime(date_file.read(),
                                                 "%Y-%m-%d").date()
except (ValueError, FileNotFoundError, PermissionError):
    desktop_notification("Date of latest backup in " + BACKUP_DATE_FILE_PATH + " could not be read.")
    sys.exit()

diff_in_days = (today - backup_date).days

if diff_in_days >= NUMBER_OF_DAYS:
    desktop_notification("A new backup has not been created for " + str(diff_in_days) + " days!")