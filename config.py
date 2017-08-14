#!/usr/bin/env python3

import logging

# Mount point of the Samba share.
# Example: "/media/nas"
MOUNT_POINT = ""

# Address of Samba share.
# Example: "192.168.178.1/FRITZ.NAS"
SHARE_ADDRESS = ""

# Path to the '.smbcredentials' file.
# Example: "/home/user/.smbcredentials"
SMB_CREDENTIALS_FILE = ""

# The full path to the backup directory. If the directory does not exist yet,
# the script tries to create the directory. Script needs read and write access.
# Example: "/media/nas/backup"
REPOSITORY_LOCATION = ""

# The passphrase for the backup. All backups are encrypted by default.
PASSPHRASE = ""

# Location of the log file. If the file does not exist yet, the script tries
# to create the file. Script needs read and write access.
# Example: "/var/log/nas-backup"
LOGFILE_PATH = ""

# Display a warning popup after n days without a backup.
# Example: 2
NUMBER_OF_DAYS = 2

# Location of file that contains date of latest backup. If the file does not
# exist yet, the script tries to create the file. Script needs read and write access.
# Example: "/home/user/.config/latest-backup"
BACKUP_DATE_FILE_PATH = ""

# Specify logging level (DEBUG/INFO/WARNING/ERROR/CRITICAL).
# Example: logging.INFO
LOGGING_LEVEL = logging.INFO

KEEP_DAILY = "7"
KEEP_WEEKLY = "4"
KEEP_MONTHLY = "12"

# The directory to backup.
# Example: "/home/user"
DIRECTORY_TO_BACKUP = ""

# List of directories/files (within directory to backup) that should be excluded.
# Please use absolute paths.
EXCLUDED_DIRECTORIES = [
    "",
    "",
    "",
    "",
    "",
    ""
]