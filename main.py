import speedtest
import pandas as pd
from datetime import datetime
import requests

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


# get current date and time
dt = datetime.now().strftime("%d/%m/%Y %H:%M:%S") # dd/mm/YY H:M:S

# get new speed test results
speeds = get_new_speeds()

#publish speed test results to Google Sheets
url='https://script.google.com/macros/s/AKfycbwJn9XQELECX6C62EPEIvhyA7aPdc1HtzId-B-6EZZH0WXwDnwFg6j4/exec'
payload = {'DeviceID':'PI', 'TimeStamp':dt,'UpSpeed':speeds[0],'DownSpeed':speeds[1],'Ping':speeds[2]}
response =  requests.get(url, params=payload)
print(response.url)
