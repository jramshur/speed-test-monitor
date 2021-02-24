import speedtest
from datetime import datetime
import requests
import time

SHEETNAME = 'addYourSheetNameHere' # add the name of the sheet in which you want the data to be placed
DEVICEID = 'PI' # ID to use in case you want to have multiple devices publish to the same Google Sheets worksheet

def get_new_speeds():
    speed_test = speedtest.Speedtest()
    speed_test.get_best_server()

    # Get ping (miliseconds)
    ping = speed_test.results.ping
    # Perform download and upload speed tests, convert to Mbits per second, and round to 2 decimal points
    download = round(speed_test.download()/(10**6), 2)
    upload = round(speed_test.upload()/(10**6), 2)

    return (upload, download, ping)

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
    payload = {'SheetName':SHEETNAME,'DeviceID':DEVICEID, 'TimeStamp':dt,'UpSpeed':speeds[0],'DownSpeed':speeds[1],'Ping':speeds[2]}
    response =  requests.get(url, params=payload) #Push speed test results
    print("Pushing Data: ", response.url)
    time.sleep((30*60) - 30) # wait 30 mintues between speed test (30 min x 60 s/min - 30s offset) offset is to count for time for code to run.
