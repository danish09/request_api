#Getting JSON from an API request

import requests

# Make the same request we did earlier, but with the coordinates of San Francisco instead.
parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a python object.  Verify that it's a dictionary.
data = response.json()
print(type(data))
print(data)

print(response.content)

# Headers is a dictionary
#print(response.headers)

# Get the content-type from the dictionary.
#print(response.headers["content-type"])
