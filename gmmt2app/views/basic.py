import logging

from flask import render_template, current_app, jsonify
from gmmt2 import journey_factory
from gmmt2app.blueprints import basic_blueprint

@basic_blueprint.route("/")
def render_index():

	config = current_app.config["gmmt2"]["journeys"]
	credentials = current_app.config["transport_api"]["credentials"]
	journeys = journey_factory.get_journeys(config, credentials, 10, current_app.config["gmmt2"]["settings"]["discard_journeys_sooner_than"])

	return render_template("index.html", journeys=journeys)


@basic_blueprint.route("/json")
def serve_json():

	config = current_app.config["gmmt2"]
	credentials = current_app.config["transport_api"]["credentials"]
	journeys = journey_factory.get_journeys(config, credentials, 10)		

	return jsonify({"journeys": [journey.json for journey in journeys]})
