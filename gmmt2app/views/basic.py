import logging

from flask import render_template, current_app, jsonify
from gmmt2 import journeymaker
from gmmt2app.blueprints import basic_blueprint

@basic_blueprint.route("/")
def render_index():

	config = current_app.config["transport_api"]["config"]
	credentials = current_app.config["transport_api"]["credentials"]
	journeys = journeymaker.get_journeys(config, credentials, 10)		

	return render_template("index.html", journeys=journeys)


@basic_blueprint.route("/json")
def serve_json():

	config = current_app.config["transport_api"]["config"]
	credentials = current_app.config["transport_api"]["credentials"]
	journeys = journeymaker.get_journeys(config, credentials, 10)		

	return jsonify({"journeys": [journey.json for journey in journeys]})