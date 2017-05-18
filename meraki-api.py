import os
import sys
import requests
import json
import sys
import argparse
import tabulate

################################################
# What's Next
################################################
# Print raw response when debug is 1
################################################

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

	# Generate Org data as dictionary
	org_data = resp.json()

	# Check response
	if resp.status_code != 200:
		print("GET " + full_url + " Error Code: {}".format(resp.status_code))
		sys.exit()

	# Check debug level & print raw response
	if debugValue == 1:
		print("\nRaw Response: ", org_data)

	# Print Organizations in table form
	print("YOUR MERAKI ORGANIZATIONS\n")
	print(tabulate.tabulate(org_data, headers="keys", tablefmt="rst"))

# Pull the networks for an organization
def pullOrgNetworks (baseURL, headers, debugValue):
	#Clear screen
	os.system('cls' if os.name == 'nt' else 'clear')

	# Print Orgs & ask user to select org ID
	pullOrgs (baseURL, headers, debugValue)
	orgID = input("\nEnter Org ID from the above list: ")
	print("Fetching Meraki organization networks...")

	# Generate full API URL
	full_url = baseURL + "organizations/" + str(orgID) + "/networks/"

	# Pull org networks
	resp = requests.get(full_url, headers=headers)

	# Generate network data as dictionary
	network_data = resp.json()

	# Check response
	if resp.status_code != 200:
		print("\t ERROR: GET " + full_url + " Error Code: {}".format(resp.status_code))
		sys.exit()

	# Check debug level & print raw response
	if debugValue == 1:
		print("\nRaw Response: ", network_data)

	# Print org networks in table form
	print("MERAKI NETWORKS\n")
	print(tabulate.tabulate(network_data, headers="keys"))

# Pull the administrators for an organization
def pullOrgAdmins (baseURL, headers, debugValue):
	#Clear screen
	os.system('cls' if os.name == 'nt' else 'clear')

	# Print Orgs & ask user to select org ID
	pullOrgs (baseURL, headers, debugValue)
	orgID = input("\nEnter Org ID from the above list: ")
	print("Fetching Meraki organization networks...")

	# Generate full API URL
	full_url = baseURL + "organizations/" + str(orgID) + "/admins/"

	# Pull org networks
	resp = requests.get(full_url, headers=headers)

	# Generate admin data as dictionary
	admin_data = resp.json()

	# Check response
	if resp.status_code != 200:
		print("\t ERROR: GET " + full_url + " Error Code: {}".format(resp.status_code))
		sys.exit()

	# Check debug level & print raw response
	if debugValue == 1:
		print("\nRaw Response: ", admin_data)

	# Print org admins in table form
	print("Meraki admins for Org ID orgID\n")
	print(tabulate.tabulate(admin_data, headers="keys"))

# Main function
def main (debugValue):
	# Check if the script is running as standalone
	if __name__ == "__main__":
		# Setup argument parser
		parser = argparse.ArgumentParser(description='Pull information from the Meraki dashboard via API.')
		parser.add_argument('--list-orgs', action='store_true', help='List Meraki organizations')
		parser.add_argument('--list-networks', action='store_true', help='List Meraki networks associated with an organization')
		parser.add_argument('--list-admins', action='store_true', help='List administrators associated with a Meraki organization')
		args = parser.parse_args()

		# Check if no arguments are passed
		if len(sys.argv) == 1:
			parser.print_help()
			parser.exit()

		# Check is environment variable with API key is set
		if 'MERAKI_API_KEY' in os.environ:
			api_key = os.getenv('MERAKI_API_KEY')
		else:
			print("ERROR: MERAKI_API_KEY environment variable required")
			sys.exit()

		# Set base URL & headers for API call
		base_url = 'https://dashboard.meraki.com/api/v0/'
		headers = {'X-Cisco-Meraki-API-Key': api_key}

		# Check arguments
		if args.list_orgs is True:
			pullOrgs(base_url, headers, debugValue)
		if args.list_networks is True:
			pullOrgNetworks(base_url, headers, debugValue)
		if args.list_admins is True:
			pullOrgAdmins(base_url, headers, debugValue)

# Call the main function - Set debugValue to 1 or enable debug info
main(0)