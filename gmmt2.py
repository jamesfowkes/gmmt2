""" gmmt2.py

Usage:
	gmmt2.py <config_file> <app_id> <app_key>
"""

import docopt
import logging
import pprint

import yaml

import journey_factory

if __name__ == "__main__":

	logging.basicConfig(level=logging.INFO)

	args = docopt.docopt(__doc__)

	credentials = {
		"app_id": args["<app_id>"],
		"app_key": args["<app_key>"]
	}

	with open(args["<config_file>"], 'r') as f:
		config = yaml.load(f)

	all_journeys = journey_factory.get_journeys(config, credentials)

	for j in all_journeys:
		print(j)
