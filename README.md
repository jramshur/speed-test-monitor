

## Raspberry Pi Setup
Default Pi login: pi
Default Pi Password raspberry

### Update Pi
    sudo apt update
    sudo apt upgrade
    sudo apt full-upgrade #if want to upgrade os also

#### Enable SSH
    sudo systemctl enable ssh
    sudo systemctl start ssh

### Change Passord
    passwd

## Setup Remote Desktop
    sudo apt install xrdp
    hostname -I
Connect to Pi using Windows Remote Destop. Use username and password for Pi logins.

## Install speedtest-cli library
    sudo pip3 install speedtest-cli

## clone repo from GitHub
    git clone https://github.com/jramshur/speed-test-monitor.git
    cd /home/pi/speed-test-monitor
    python main.py

## Google Sheets
https://script.google.com/macros/s/AKfycbwJn9XQELECX6C62EPEIvhyA7aPdc1HtzId-B-6EZZH0WXwDnwFg6j4/exec?DeviceID=myid&TimeStamp=100&UpSpeed=100&DownSpeed=100&Ping=100
