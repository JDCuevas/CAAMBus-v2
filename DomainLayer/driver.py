from InfrastructureLayer.driverDAO import DriverDao

class Driver:
	def __init__(self, data=None):
		self.driver = {}

		if data:
			self.driver['driver_id'] = data['driver_id']
			self.driver['license'] = data['license']
			self.driver['user_id'] = data['user_id']

	def factory(self, license, user_id):
		dao = DriverDao()

		driver_id = dao.register(license, user_id)
		data = dao.getDriverById(driver_id)

		self.driver['driver_id'] = data['driver_id']
		self.driver['license'] = data['license']
		self.driver['user_id'] = data['user_id']

	def getInfo(self):
		return self.driver

class DriverRepository:
	def __init__(self):
		self.dao = DriverDao()

	def getAllDrivers(self):
		result = self.dao.getAllDrivers()
		drivers = []

		for row in result:
			driver = Driver(row)
			driver.driver['name'] = row['first_name'] + " " + row['last_name']
			driver.driver['phone'] = row['phone']
			drivers.append(driver)

		return drivers

	def getDriverById(self, user_id):
		result = self.dao.getDriverById(user_id)
		driver = None

		if result:
			driver = Driver(result)

		return driver