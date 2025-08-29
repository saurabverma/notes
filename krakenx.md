# Setup KrakenX (colctl)

## Install

Run
```bash
sudo apt install python3-full pipx
pipx install krakenx
```

## Auto-start

Open service file
```bash
sudo nano /etc/systemd/system/krakenx-config.service
```
and add the following
```
[Unit]
Description=krakenx automatic configuration
After=multi-user.target

[Service]
Type=oneshot
ExecStart=/usr/bin/env colctl -m Breathing -as 0 -c 255,255,255 -c0 255,255,255 --fan_speed "(34,25),(35,50),(36,75),(37,90),(38,100)" --pump_speed "(34,60),(35,70),(36,80),(37,90),(38,100)"

[Install]
WantedBy=multi-user.target
```
Replace `/usr/bin/env colctl` with the output of `which colctl` to record the correct path to KrakenX driver.

## Use without sudo

Create a Udev Rule

```bash
sudo nano /etc/udev/rules.d/99-nzxt-kraken.rules
```
and add the following Rule
```
SUBSYSTEM=="usb", ATTR{idVendor}=="1e71", ATTR{idProduct}=="170e", MODE="0666"
```
Replace `1e71` and `170e` with actual device ID available via running `lsusb` and looking for something like `NZXT Kraken X`.

Now, reboot system to see the system working.
