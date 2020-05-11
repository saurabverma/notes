1. To automatically mount a drive at start-up, use the following command
(update drive details i.e. `/dev/sd??` using info from `lsblk` and mount localition)
```
/dev/<sda1> </media/mount_location> auto nosuid,nodev,nofail,x-gvfs-show 0 0
```





2. If file-explorer is not functional, first get the PID for 'nautilus'
```
ps -A | grep nautilus
```
which shows something like `  <PID> ?        00:00:10 nautilus`, then second, read the PID and kill the process
```
sudo kill -9 PID
```





3. For installation of gtsam, typically usage of system eigen is preferred over regular `cmake ..`
```
cmake -DGTSAM_USE_SYSTEM_EIGEN=ON ..
```



3. `chmod` with Letters
```
Usage: chmod {options} filename
```
| Options | Definition |
|---|---|
| u | owner |
| g | group |
| o | other |
| a | all (same as ugo) |
| x | execute |
| w | write |
| r | read |
| + | add permission |
| - | remove permission |
| = | set permission |
