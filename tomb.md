# Tomb Usage

Tomb is an open-source and versatile file data encryption tool.
The following are most common commands to be used with Tomb.

## Install

```bash
sudo apt update
sudo apt install -y tomb
```

## Create

Switch off swap (necessary for key generation).
```bash
sudo swapoff -a
```

Create tomb file (of size say, 100 MB) and key.

```bash
sudo tomb dig -s 100 data.tomb
sudo tomb forge data.tomb.key
```

## Lock (one-time after creation)

Lock the tomb files using respective key.

```bash
sudo tomb lock data.tomb -k data.tomb.key
```

# Open

Prior to working with the tomb file, we must open and mount it as follows.

```bash
sudo tomb open data.tomb -k data.tomb.key
```

NOTE: Opening a tomb also mentions the mounting location which is required for copying data in-out the tomb file.
Ubuntu users may also use `Disk Usage Analyzer` app to find out the mount location, once the file is open.
An alternate approach is the following which lists all available tomb files, along with essential details.

## List (optional)

```bash
sudo tomb list
```

## Copy data

Copy data inside and outside the virtual drive represented by the tomb file (mounted at say, `/media/data/`).
NOTE: The tomb file must be big enough to hold the data, otherwise copy may fail.

```bash
sudo cp -rv data/* -t /media/data/
```

## Close

```bash
sudo tomb close
sudo tomb close all
```

## Forced close

In case a process is ongoing but user needs to close the file, apply forced close command as follows.

```bash
sudo tomb slam
sudo tomb slam all
```

## Resize

```bash
sudo tomb dig -s 1000000 data.tomb
```
