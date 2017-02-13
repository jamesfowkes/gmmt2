import datetime
import json

from collections import namedtuple

class Journey(namedtuple("Journey", ["service", "time"])):

	__slots__ = ()

	@classmethod
	def from_bus_json(cls, json):
		service = json["line"]
		time = datetime.datetime.strptime(json["best_departure_estimate"], "%H:%M").time()
		time = datetime.datetime.combine(datetime.datetime.today(), time)
		return cls(service, time)

	@classmethod
	def from_train_json(cls, json):
		service = "Train"
		time = datetime.datetime.strptime(json["aimed_departure_time"], "%H:%M").time()
		time = datetime.datetime.combine(datetime.datetime.today(), time)
		return cls(service, time)

	def json(self):
		return json.dumps(
			{
				"service": self.service,
				"time": self.time
			}
		)

	def mins_to_depart(self, timenow=datetime.datetime.now()):
		minutes = (self.time - timenow).total_seconds()/60
		return int(minutes + 0.5)
		
	def __str__(self):
		return "{} at {:%H:%M}".format(self.service, self.time)

	def __lt__(self, other):
		return self.time < other.time

	def __le__(self, other):
		return self.time <= other.time

	def __eq__(self, other):
		return self.time == other.time

	def __ne__(self, other):
		return self.time != other.time

	def __gt__(self, other):
		return self.time > other.time

	def __ge__(self, other):
		return self.time >= other.time
