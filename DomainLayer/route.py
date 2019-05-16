from InfrastructureLayer.routeDAO import RouteDao

class Route:
	def __init__(self, data=None):
		self.route = {}

		if data:
			self.route['route_id'] = data['route_id']
			self.route['route_name'] = data['route_name']

	def factory(self, route_name):
		dao = RouteDao()

		route_id = dao.createRoute(route_name)
		data = dao.getRouteById(route_id)

		self.route['route_id'] = data['route_id']
		self.route['route_name'] = data['route_name']

	def getInfo(self):
		return self.route

class RouteRepository:
	def __init__(self):
		self.dao = RouteDao()

	def deleteRoute(self, route_id):
		route_id = self.dao.deleteRoute(route_id)

		return route_id

	def getAllRoutes(self):
		result = self.dao.getAllRoutes()
		routes = []

		if result:
			for row in result:
				route = Route(row)
				routes.append(route)

		return routes

	def getDriverById(self, user_id):
		result = self.dao.getDriverById(user_id)
		route = None

		if result:
			route = Route(result)

		return route

	def add_stop(self, route_id, stop_id):
		result = self.dao.add_stop(route_id, stop_id)

		return result

	def remove_stop(self, route_id, stop_id):
		result = self.dao.remove_stop(route_id, stop_id)

		return result

	def getStopsNotInRoute(self, route_id):
		result = self.dao.getStopsNotInRoute(route_id)
		stops = []

		if result:
			for row in result:
				stop = {}
				stop['stop_id'] = row['stop_id']
				stop['stop_name'] = row['stop_name']
				stop['latitude'] = row['latitude']
				stop['longitude'] = row['longitude']
				stops.append(stop)

		return stops

	def getRouteStops(self, route_id):
		result = self.dao.getRouteStops(route_id)
		stops = []

		if result:
			for row in result:
				stop = {}
				stop['stop_id'] = row['stop_id']
				stop['stop_name'] = row['stop_name']
				stop['latitude'] = row['latitude']
				stop['longitude'] = row['longitude']
				stops.append(stop)

		return stops