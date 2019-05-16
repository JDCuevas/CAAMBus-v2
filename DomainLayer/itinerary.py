from InfrastructureLayer.itineraryDAO import ItineraryDao

class Itinerary:
	# Schema: itinerary_id, date, start_time, end_time, driver_id, trolley_id, route_id
	
	def __init__(self, data=None):
		self.itinerary = {}

		if data:
			self.itinerary['itinerary_id'] = data['itinerary_id']
			self.itinerary['date'] = data['date']
			self.itinerary['start_time'] = data['start_time']
			self.itinerary['end_time'] = data['end_time']
			self.itinerary['driver_id'] = data['driver_id']
			self.itinerary['trolley_id'] = data['trolley_id']
			self.itinerary['route_id'] = data['route_id']

	def factory(self, date, start_time, end_time, driver_id, trolley_id, route_id):
		dao = ItineraryDao()

		itinerary_id = dao.createItinerary(date, start_time, end_time, driver_id, trolley_id, route_id)
		data = dao.getItineraryById(itinerary_id)

		self.itinerary['itinerary_id'] = data['itinerary_id']
		self.itinerary['date'] = data['date']
		self.itinerary['start_time'] = data['start_time']
		self.itinerary['end_time'] = data['end_time']
		self.itinerary['driver_id'] = data['driver_id']
		self.itinerary['trolley_id'] = data['trolley_id']
		self.itinerary['route_id'] = data['route_id']

	def getInfo(self):
		return self.itinerary

class ItineraryRepository:
	def __init__(self):
		self.dao = ItineraryDao()

	def getAllItineraries(self):
		result = self.dao.getAllItineraries()
		itineraries = []

		for row in result:
			itinerary = Itinerary(row)
			itinerary.itinerary['driver'] = row['first_name'] + " " + row['last_name']
			itinerary.itinerary['trolley_plate'] = row['plate']
			itinerary.itinerary['route'] = row['route_name']
			itineraries.append(itinerary)

		return itineraries

	def deleteItinerary(self, itinerary_id):
		itinerary_id = self.dao.deleteItinerary(itinerary_id)

		return itinerary_id

	def getItinerariesByUserId(self, user_id):
		result = self.dao.getItinerariesByUserId(user_id)
		itineraries = []

		for row in result:
			itinerary = Itinerary(row)
			itinerary.itinerary['driver'] = row['first_name'] + " " + row['last_name']
			itinerary.itinerary['trolley_plate'] = row['plate']
			itinerary.itinerary['route'] = row['route_name']
			itineraries.append(itinerary)

		return itineraries