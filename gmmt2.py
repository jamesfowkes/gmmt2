""" gmmt2.py

Usage:
	gmmt2.py <app_id> <app_key>
"""

import docopt
import logging

import transportapi.bus
import transportapi.train

from journey import Journey

def get_journeys_to_town(credentials):
	hg_buses = transportapi.bus.get_live_json("3300BR0307", credentials)
	hg_buses = transportapi.bus.flatten_services(hg_buses)

	pr_buses = transportapi.bus.get_live_json("3300BR0270", credentials)
	pr_buses = transportapi.bus.flatten_services(pr_buses)
	
	trains = transportapi.train.get_timetable_json_now("BEE", credentials, {"calling_at":"NOT"})

	hg_journeys = [Journey.from_bus_json(json) for json in hg_buses["departures"]]
	pr_journeys = [Journey.from_bus_json(json) for json in pr_buses["departures"]]
	train_journeys = [Journey.from_train_json(json) for json in trains["departures"]["all"]]

	all_journeys = []
	
	all_journeys.extend(hg_journeys)
	all_journeys.extend(pr_journeys)
	all_journeys.extend(train_journeys)

	return sorted(all_journeys)

if __name__ == "__main__":

	logging.basicConfig(level=logging.INFO)

	args = docopt.docopt(__doc__)

	credentials = {
		"app_id": args["<app_id>"],
		"app_key": args["<app_key>"]
	}

	all_journeys = get_journeys_to_town(credentials)

	for j in sorted(all_journeys):
		print(j)
