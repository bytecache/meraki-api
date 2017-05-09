import os
import requests
import json

api_key = os.getenv('MERAKI_API_KEY')

url = 'https://dashboard.meraki.com/api/v0/organizations/'
headers = {'X-Cisco-Meraki-API-Key': api_key}

r = requests.get(url, headers=headers)

# Print response code
print("Response code: ", r)

# Print response content
print("Raw Response: ", r.content)

# Print formatted response
formatteded_response = str(r.content,'utf-8')
print("Formatted response: ")
print (json.dumps(r.content, sort_keys=True, indent=4))