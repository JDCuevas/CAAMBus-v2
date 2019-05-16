from flask import jsonify
from DomainLayer.driver import Driver, DriverRepository

class DriverHandler:
	# Schema: driver_id, license, user_id
	repo = DriverRepository()

	def register(self, license, user_id):
		driver = Driver().factory(license, user_id)

	def getAllDrivers(self):
		result = self.repo.getAllDrivers()
		drivers = []

		if result:
			for row in result:
				driverInfo = row.getInfo()
				drivers.append(driverInfo)

		return drivers

	def getDriverById(self, driver_id):
		result = self.repo.getDriverById(driver_id)
		driver = None

		if result:
			driver = result.getInfo()

		return driver
