""" runapp.py

Usage:
	runapp.py <config_file>
"""

import docopt
import os
import logging
import yaml

import flask

from gmmt2app import app

if __name__ == "__main__":

	if app.debug:
		logging.basicConfig(level=logging.INFO)

	args = docopt.docopt(__doc__)

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

	app.run()
