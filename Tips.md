To automatically mount a drive at start-up, use the following command
(update drive details i.e. `/dev/sd??` using info from `lsblk` and mount localition)
```
/dev/<sda1> </media/mount_location> auto nosuid,nodev,nofail,x-gvfs-show 0 0
```





If file-explorer is not functional, first get the PID for 'nautilus'
```
ps -A | grep nautilus
```
which shows something like `  <PID> ?        00:00:10 nautilus`, then second, read the PID and kill the process
```
sudo kill -9 PID
```
