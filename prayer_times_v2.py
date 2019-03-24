import json

with open('/home/danish/repo/hub/request_api/iccuk_prayertimes') as json_file:
    read_content = json.load(json_file)


read_content

times_access = read_content['times']

times_access

dates_access = times_access['2019-03-31']

dates_access

type(dates_access)

for key,value in dates_access.items():
    print (key, "=>", value)