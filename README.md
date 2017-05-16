#Meraki API Interface

##Requirements
* Environment variable named MERAKI_API_KEY with your API key
* See requirements.txt for more details

##Description
I wrote this script to accomplish some fairly simple tasks via the Meraki API. Mostly to pull data/information about networks.

##Usage
~~~~
usage: meraki-api.py [-h] [--list-orgs] [--list-networks]

Pull information from the Meraki dashboard via API.

optional arguments:
  -h, --help       show this help message and exit
  --list-orgs      List Meraki organizations
  --list-networks  List Meraki networks associated with an organization
~~~~