import logging

import transportapi.bus
import transportapi.train

from journey import Journey

def get_module_logger():
	return logging.getLogger(__name__)

def get_bus_journeys(config, credentials):
	buses = transportapi.bus.get_live_json(config["stop_id"], credentials)
	buses = transportapi.bus.flatten_services(buses)
	try:
		buses = [Journey.from_bus_json(json) for json in buses["departures"]]
	except:
		get_module_logger.warning("Exception parsing bus times JSON for {}".format(config["stop_id"]))
		buses = []

	return buses

def get_train_journeys(config, credentials):
	trains =  transportapi.train.get_live_json(config["station_code"], credentials, {"calling_at":config["calling_at"]})

	try:
		trains = [Journey.from_train_json(json) for json in trains["departures"]["all"]]
	except:
		get_module_logger.warning("Exception parsing train times JSON for {}".format(config["station_code"]))
		trains = []

	return trains

def flatten(list_of_lists):
	return [item for sublist in list_of_lists for item in sublist]

def get_journeys(config, credentials, limit=None):

	bus_journeys = flatten([get_bus_journeys(bus_cfg, credentials) for bus_cfg in config["buses"]])
	train_journeys = flatten([get_train_journeys(train_cfg, credentials) for train_cfg in config["trains"]])

	all_journeys = []
	for bus in bus_journeys:
		all_journeys.append(bus)
	
	for train in train_journeys:
		all_journeys.append(train)
	
	all_journeys = sorted(all_journeys)
	
	if limit:
		all_journeys = all_journeys[0:limit]

	return all_journeys
