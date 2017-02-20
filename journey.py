import datetime
import json

from collections import namedtuple

class Journey(namedtuple("Journey", ["service", "expected", "actual"])):

	__slots__ = ()

	@classmethod
	def from_bus_json(cls, json):
		service = json["line"]
		aimed_time = datetime.datetime.strptime(json["aimed_departure_time"], "%H:%M").time()
		aimed_time = datetime.datetime.combine(datetime.datetime.today(), aimed_time)

		expected_time = datetime.datetime.strptime(json["best_departure_estimate"], "%H:%M").time()
		expected_time = datetime.datetime.combine(datetime.datetime.today(), expected_time)
		
		return cls(service, aimed_time, expected_time)

	@classmethod
	def from_train_json(cls, json):
		service = "Train"
		aimed_time = datetime.datetime.strptime(json["aimed_departure_time"], "%H:%M").time()
		aimed_time = datetime.datetime.combine(datetime.datetime.today(), aimed_time)

		expected_time = datetime.datetime.strptime(json["expected_departure_time"], "%H:%M").time()
		expected_time = datetime.datetime.combine(datetime.datetime.today(), expected_time)
		return cls(service, aimed_time, expected_time)


	@property
	def json(self):
		return json.dumps(
			{
				"service": self.service,
				"time": {
					"expected": self.expected.isoformat(),
					"actual": self.actual.isoformat()
				}
			}
		)

	def mins_to_depart(self, timenow=datetime.datetime.now()):
		minutes = (self.actual - timenow).total_seconds()/60
		return int(minutes + 0.5)
	
	def is_late(self):
		return (self.actual - self.expected).total_seconds()/60

	def __str__(self):
		return "{} at {:%H:%M}".format(self.service, self.actual)

	def __lt__(self, other):
		return self.actual < other.actual

	def __le__(self, other):
		return self.actual <= other.actual

	def __eq__(self, other):
		return self.actual == other.actual

	def __ne__(self, other):
		return self.actual != other.actual

	def __gt__(self, other):
		return self.actual > other.actual

	def __ge__(self, other):
		return self.actual >= other.actual
