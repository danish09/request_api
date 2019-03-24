import json

from datetime import datetime

from playsound import playsound

tday=datetime.today().strftime('%Y-%m-%d')

with open('/home/danish/repo/hub/request_api/iccuk_prayertimes') as json_file:
    read_content = json.load(json_file)

times_access = read_content['times']

dates_access = times_access[tday]

for key,value in dates_access.items():
    print (key, "=>", value)
    #playsound('/home/danish/Downloads/adan.mp3')