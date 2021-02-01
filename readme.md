https://script.google.com/macros/s/AKfycbwJn9XQELECX6C62EPEIvhyA7aPdc1HtzId-B-6EZZH0WXwDnwFg6j4/exec?DeviceID=myid&TimeStamp=100&UpSpeed=100&DownSpeed=100&Ping=100

#DEFAULT LOGIN: pi   DEFAULT PASSWORD: raspberry

#Update Pi
sudo apt update
sudo apt upgrade
sudo apt full-upgrade #if want to upgrade os also

#Enable SSH
sudo systemctl enable ssh
sudo systemctl start ssh

#Change Passord
passwd

#Setup Remote Desktop
sudo apt install xrdp
hostname -I
#connect to Pi using Windows Remote Destop. Use username and password for Pi logins.

#Install speedtest-cli library
sudo pip3 install speedtest-cli

