from InfrastructureLayer.trolleyDAO import TrolleyDao

class Trolley:
	def __init__(self, data=None):
		self.trolley = {}

		if data:
			self.trolley['trolley_id'] = data['trolley_id']
			self.trolley['plate'] = data['plate']
			self.trolley['capacity'] = data['capacity']
			self.trolley['mileage'] = data['mileage']

	def factory(self, plate, capacity, mileage):
		dao = TrolleyDao()

		trolley_id = dao.registerTrolley(plate, capacity, mileage)
		data = dao.getTrolleyById(trolley_id)

		self.trolley['trolley_id'] = data['trolley_id']
		self.trolley['plate'] = data['plate']
		self.trolley['capacity'] = data['capacity']
		self.trolley['mileage'] = data['mileage']

	def getInfo(self):
		return self.trolley

class TrolleyRepository:
	def __init__(self):
		self.dao = TrolleyDao()

	def deleteTrolley(self, trolley_id):
		trolley_id = self.dao.deleteTrolley(trolley_id)

		return trolley_id

	def getAllTrolleys(self):
		result = self.dao.getAllTrolleys()
		trolleys = []

		if result:
			for row in result:
				trolley = Trolley(row)
				trolleys.append(trolley)

		return trolleys

	def getTrolleyById(self, trolley_id):
		result = self.dao.getTrolleyById(trolley_id)
		trolley = None

		if result:
			trolley = Trolley(result)

		return trolley