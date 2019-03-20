import requests

#setting the parameters

parameters = {"address": '14 Plympton Place, London, United Kingdom', "method": 12, "month": 04, "year": 2019}

#calling the API with params

response = requests.get("http://api.aladhan.com/v1/calendarByAddress", params=parameters)

# Headers is a dictionary
#print(response.headers)

#printing the string
#print(response.content)

# Get the response data as a python object.  Verify that it's a dictionary.
data = response.json()

#printing the type of data returned
#print(type(data))

#printing the json converted data
print(data)

#print(response.content)
