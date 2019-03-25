import json

import requests

from datetime import datetime

from playsound import playsound

tday=datetime.today().strftime('%Y-%m-%d')

right_now=datetime.today().strftime('%I-%M-%p')

response = requests.get("https://www.londonprayertimes.com/api/times/?format=json&key=0239f686-4423-408e-9a0c-7968a403d197&year=&month=")

data=response.json()

for key,value in data.items():
    if value >= '03:30' and value < '06:00':
            print('It is asr time')
    
    
    #playsound('/home/danish/Downloads/adan.mp3')