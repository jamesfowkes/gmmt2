""" train.py
Usage:
	train.py <station_code> <app_id> <app_key> [--dest=<destination_filter>]
"""

import docopt
import pprint
import logging

import transportapi

def get_module_logger():
	return logging.getLogger()

def get_timetable_json_now(station_code, credentials, params={}):
	params.update(credentials)
	return transportapi.request("/uk/train/station/{}/timetable.json".format(station_code), params)

def get_live_json(station_code, credentials, params={}):
	params.update(credentials)
	return transportapi.request("/uk/train/station/{}/live.json".format(station_code), params)

if __name__ == "__main__":

	logging.basicConfig(level=logging.INFO)

	args = docopt.docopt(__doc__)

	station_code = args["<station_code>"]
	credentials = {
		"app_id": args["<app_id>"],
		"app_key": args["<app_key>"]
	}

	params = {}
	if args["--dest"]:
		params = {"calling_at":args["--dest"]}

	json = (get_timetable_json_now(station_code, credentials, params))

	pprint.pprint(json)
