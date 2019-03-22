import requests
import json


#from pprint import pprint

#setting the parameters

parameters = {"address": '14 Plympton Place, London, NW8 8AD, United Kingdom', "method": 12, "month": '04', "year": 2019}

#calling the API with params

response = requests.get("http://api.aladhan.com/v1/calendarByAddress", params=parameters)
#jsonresponse = json.dumps(requests.get("http://api.aladhan.com/v1/calendarByAddress", params=parameters).json())

# Headers is a dictionary
#print(response.headers)

#printing the string
#print(response.content)

# Get the response data as a python object.  Verify that it's a dictionary.
data = response.json()

#printing the type of data returned
#print(type(data))

#printing the json converted data
#print(data)

print(data['data']['timings']['Fajr'])


#pprint(data)
#print(response.content)

import json
with open('/home/siddiq08/python-scripts/prayertimes') as json_file:
    read_content = json.load(json_file)

read_content
question_access = read_content['data']
question_access[0]
for question_data in question_acess:
    print(question_data)
type(question_data)
replies_access = question_data['timings']
replies_access
