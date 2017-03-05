#!/usr/bin/python3

""" runapp.py

Usage:
    runapp.py <config_file> <logfile> [--public] [--debug]
"""

import docopt
import os
import logging
import logging.handlers
import yaml

import flask

from gmmt2app import app

def get_logger():
    return logging.getLogger(__name__)

if __name__ == "__main__":

    args = docopt.docopt(__doc__)

    formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
    logging_handler = logging.handlers.RotatingFileHandler(args["<logfile>"], maxBytes=1024*1024, backupCount=3)
    logging_handler.setFormatter(formatter)
    
    debug = "--debug" in args

    if debug:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.DEBUG)

    get_logger().addHandler(logging_handler)

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
        app.run(host='0.0.0.0', debug=debug)
    else:
        app.run(debug=debug)
