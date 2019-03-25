import json

import requests

from datetime import datetime

from playsound import playsound

tday=datetime.today().strftime('%Y-%m-%d')

yr=datetime.today().strftime('%Y')

mon=datetime.today().strftime('%m')

right_now=datetime.today().strftime('%I-%M-%p')

response = requests.get("https://www.londonprayertimes.com/api/times/?format=json&key=0239f686-4423-408e-9a0c-7968a403d197&year=yr&month=mon")

data=response.json()

times_access = data['times']

times_access = read_content['times']

dates_access = times_access[tday]

for key,value in dates_access.items():
    if value == tday:
#        print (key, "=>", value)
        if value == right_now:
            print('it is asr time')
    
    
    #playsound('/home/danish/Downloads/adan.mp3')