from flask import jsonify
from DomainLayer.trolley import Trolley, TrolleyRepository

class TrolleyHandler:
	# Schema: trolley_id, plate, capacity, mileage
	repo = TrolleyRepository()

	def registerTrolley(self, plate, capacity, mileage):
		trolley = Trolley()
		trolley.factory(plate, capacity, mileage)
		return trolley.trolley

	def deleteTrolley(self, trolley_id):
		trolley_id = self.repo.deleteTrolley(trolley_id)

		return trolley_id

	def getAllTrolleys(self):
		result = self.repo.getAllTrolleys()
		trolleys = []

		if result:
			for row in result:
				trolleyInfo = row.getInfo()
				trolleys.append(trolleyInfo)

		return trolleys

	def getTrolleyById(self, trolley_id):
		result = self.repo.getTrolleyById(trolley_id)
		trolley = None

		if result:
			trolley = result.getInfo()

		return trolley