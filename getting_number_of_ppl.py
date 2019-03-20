import json
import requests

# Get the response from the API endpoint.
response = requests.get("http://api.open-notify.org/astros.json")
print(type(response.content))
print(response.content)

data = json.loads(response.content)
print(type(data))

print(data["number"])
