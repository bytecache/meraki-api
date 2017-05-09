import os
import requests
import json
import sys

api_key = os.getenv('MERAKI_API_KEY')

url = 'https://dashboard.meraki.com/api/v0/'
headers = {'X-Cisco-Meraki-API-Key': api_key}

r = requests.get(url, headers=headers)

# Print response code
#print("Response code: ", r)

# Print response content
#print("Raw Response: ", r.content)

# Print formatted response
#print("Formatted response: ")
#print (json.loads(str(r.content,'utf-8')))

# Json Response
#print("JSON Response: ")
#for r_item in r.json():
#	print('{} {}'.format(r_item['id'], r_item['name']))
#print (r.json())

# Check API call response call
def checkResponse (response):
	sys.exit()

# Pull organizations
def pullOrgs (baseURL, headers):
	full_url = baseURL + "organizations/"

	# Pull orgs
	resp = requests.get(full_url, headers=headers)

	# Check response
	if resp.status_code != 200:
		print("GET /organizations/ Error Code: {}".format(resp.status_code))
		sys.exit()

	# Print Organizations
	print("Your Meraki Organizations")
	for r_item in resp.json():
		print('{} \n\t Org ID: {}'.format(r_item['name'], r_item['id']))

    # Print raw response
	org_data = resp.json()
	print("\nRaw Response: ", org_data)

	# Test print value
	print(org_data[0]['id'])

# Pull the networks for an organization
def pullOrgNetworks (baseURL, headers, orgID):
	# Generate full API URL
	full_url = baseURL + "organizations/" + str(orgID) + "/networks/"

	# Pull org networks
	resp = requests.get(full_url, headers=headers)

	# Check response
	if resp.status_code != 200:
		print("GET /organizations/ Error Code: {}".format(resp.status_code))
		sys.exit()

	# Print raw response
	network_data = resp.json()
	#print("\nRaw Response: ", network_data)

	# Print org networks
	print("Meraki Networks for Org ID " + str(orgID))
	for network in resp.json():
		print('\t{}'.format(network['name']))

# Main function
def main ():
	#pullOrgs (url, headers)
	pullOrgNetworks(url,headers,618119048856601289)

main()