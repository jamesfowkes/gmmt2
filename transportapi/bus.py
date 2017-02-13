""" bus.py
Usage:
	bus.py <atcocode> <app_id> <app_key>
"""

import docopt
import pprint
import logging

import transportapi

def get_live_json(atcocode, credentials):
	return transportapi.request("/uk/bus/stop/{}/live.json".format(atcocode), credentials)

def flatten_services(json):
	all_departures = []

	for departures in json["departures"].values():
		for departure in departures:
			all_departures.append(departure)

	json["departures"] = all_departures

	return json
	
if __name__ == "__main__":

	args = docopt.docopt(__doc__)

	atcocode = args["<atcocode>"]
	credentials = {
		"app_id": args["<app_id>"],
		"app_key": args["<app_key>"]
	}

	pprint.pprint(get_live_json(atcocode, credentials))