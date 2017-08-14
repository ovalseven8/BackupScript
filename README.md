# BorgBackup script

Script to do daily backups to a Samba share using `BorgBackup`.

## Instructions

#### Requirements
Python 3.6+<br />
BorgBackup 1.1.0+<br />
OS supporting `notify-send` command<br />
cifs-utils

### Install dependencies
Make sure that `cifs-utils` and `borg` (>= 1.1.0) is installed:
```
sudo apt-get install cifs-utils
```
```
sudo apt-get install borg
```

### Samba share
1. Create new file `~/.smbcredentials` with the following content to have
access to the Samba share
```
username=(username)
password=(password)
```
2. Create mount point for NAS
```
sudo mkdir /media/nas
```

### Set up script
1. Download this repository and put it into a directory of your choice (e.g. `~/scripts`):
```
mkdir ~/scripts
cd ~/scripts
git clone https://github.com/ovalseven8/BackupScript
```
2. Open `config.py` and fill the configs.
3. Make sure that all two scripts are executable!

### Do daily backups! :)
1. Create symbolic link to the backup script
```
sudo ln -s /path/to/backupScript /etc/cron.daily
```
2. The script `checkBackupDate.py` is for checking if regular backups are
created. If there have not been new backups for n days it shows a popup. Add
`checkBackupDate.py` to autostart (depends on operating system).

Please be aware that if you change the location of the three files you should
also change the symbolic link and maybe adjust autostart!
