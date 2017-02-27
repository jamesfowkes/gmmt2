""" runapp.py

Usage:
	runapp.py <config_file> [--public] [--debug]
"""

import docopt
import os
import logging
import yaml

import flask

from gmmt2app import app

if __name__ == "__main__":

	args = docopt.docopt(__doc__)

	if args["--debug"]:
		logging.basicConfig(level=logging.INFO)

	with open(args["<config_file>"], 'r') as f:
		config = yaml.load(f)

	app.config["transport_api"] = {
		"credentials":
		{
			"app_id": os.getenv("TRANSPORT_API_ID"),
			"app_key": os.getenv("TRANSPORT_API_KEY")
		},
	}

	app.config["gmmt2"] = config

	if args['--public']:
		app.run(host='0.0.0.0')
	else:
		app.run()
