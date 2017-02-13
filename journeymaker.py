import transportapi.bus
import transportapi.train

from journey import Journey

def get_bus_journeys(config, credentials):
	buses = transportapi.bus.get_live_json(config["stop_id"], credentials)
	buses = transportapi.bus.flatten_services(buses)
	buses = [Journey.from_bus_json(json) for json in buses["departures"]]
	return buses

def get_train_journeys(config, credentials):
	trains = transportapi.train.get_timetable_json_now(config["station_code"], credentials, {"calling_at":config["calling_at"]})
	return [Journey.from_train_json(json) for json in trains["departures"]["all"]]

def flatten(list_of_lists):
	return [item for sublist in list_of_lists for item in sublist]

def get_journeys(config, credentials):

	bus_journeys = flatten([get_bus_journeys(bus_cfg, credentials) for bus_cfg in config["buses"]])
	train_journeys = flatten([get_train_journeys(train_cfg, credentials) for train_cfg in config["trains"]])

	all_journeys = []
	for bus in bus_journeys:
		all_journeys.append(bus)
	
	for train in train_journeys:
		all_journeys.append(train)
	
	return sorted(all_journeys)
