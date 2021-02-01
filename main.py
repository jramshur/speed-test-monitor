import speedtest
from datetime import datetime
import requests
import time

def get_new_speeds():
    speed_test = speedtest.Speedtest()
    speed_test.get_best_server()

    # Get ping (miliseconds)
    ping = speed_test.results.ping
    # Perform download and upload speed tests (bits per second)
    download = speed_test.download()
    upload = speed_test.upload()

    # Convert download and upload speeds to megabits per second
    download_mbs = round(download / (10**6), 2)
    upload_mbs = round(upload / (10**6), 2)

    return (upload_mbs, download_mbs, ping)

# wait 60 seconds to allow Pi to reboot fully before running speed test. This assumes this script will be run at boot.
time.sleep(60)
    
while True:
    # get current date and time
    dt = datetime.now().strftime("%m/%d/%Y %H:%M:%S") # mm/dd/YY H:M:S
    
    # get new speed test results
    print("Speed test started...")
    speeds = get_new_speeds()
    print("Speed Test Results: ",speeds)

    #publish speed test results to Google Sheets
    url='https://script.google.com/macros/s/AKfycbwJn9XQELECX6C62EPEIvhyA7aPdc1HtzId-B-6EZZH0WXwDnwFg6j4/exec'
    payload = {'DeviceID':'PI', 'TimeStamp':dt,'UpSpeed':speeds[0],'DownSpeed':speeds[1],'Ping':speeds[2]}
    response =  requests.get(url, params=payload) #Push speed test results
    print("Pushing Data: ", response.url)
    time.sleep(30*60) # wait 30 mintues between speed test
