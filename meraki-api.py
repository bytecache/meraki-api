import os
import sys
import requests
import json
import tabulate

################################################
# What's Next
################################################
# pullOrg - Ask what ORG to work on
# pullOrg - Return ORG ID based on selection
# Pass ORG ID into other fucntions
################################################

# Pull the API key from an Environment variable
api_key = os.getenv('MERAKI_API_KEY')

# Set Base URL
base_url = 'https://dashboard.meraki.com/api/v0/'

# Configure header to be sent with API requests
headers = {'X-Cisco-Meraki-API-Key': api_key}

#r = requests.get(url, headers=headers)

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
def pullOrgs (baseURL, headers, debugValue):
	#Clear screen
	os.system('cls' if os.name == 'nt' else 'clear')

	full_url = baseURL + "organizations/"

	# Pull orgs
	resp = requests.get(full_url, headers=headers)

	# Check response
	if resp.status_code != 200:
		print("GET " + full_url + " Error Code: {}".format(resp.status_code))
		sys.exit()

	# Generate Org Data as dictionary
	org_data = resp.json()

	# Print Organizations in table form
	print("YOUR MERAKI ORGANIZATIONS\n")
	print(tabulate.tabulate(org_data, headers="keys"))

	

# Pull the networks for an organization
def pullOrgNetworks (baseURL, headers, debugValue):
	#Clear screen
	os.system('cls' if os.name == 'nt' else 'clear')

	# Print Orgs & ask user to select org ID
	pullOrgs (base_url, headers, debugValue)
	orgID = input("\nEnter Org ID from the above list: ")
	print("Fetching Meraki organization networks...")

	# Generate full API URL
	full_url = baseURL + "organizations/" + str(orgID) + "/networks/"

	# Pull org networks
	resp = requests.get(full_url, headers=headers)
	network_data = resp.json()

	# Check response
	if resp.status_code != 200:
		print("\t ERROR: GET " + full_url + " Error Code: {}".format(resp.status_code))
		sys.exit()

	# Print raw response
	#print("\nRaw Response: ", network_data)

	# Print org networks in table form
	print("MERAKI NETWORKS\n")
	print(tabulate.tabulate(network_data, headers="keys"))

# Main function
def main (debugValue):
	#pullOrgs (base_url, headers)
	pullOrgNetworks(base_url,headers,debugValue)

main(0)