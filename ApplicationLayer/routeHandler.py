from flask import jsonify
from DomainLayer.route import Route, RouteRepository

class RouteHandler:
	# Schema: route_id, license, user_id
	repo = RouteRepository()

	def createRoute(self, route_name):
		route = Route()
		route.factory(route_name)
		return route.route

	def deleteRoute(self, route_id):
		route_id = self.repo.deleteRoute(route_id)

		return route_id

	def getAllRoutes(self):
		result = self.repo.getAllRoutes()
		routes = []

		if result:
			for row in result:
				routeInfo = row.getInfo()
				routes.append(routeInfo)

		return routes

	def getRouteById(self, route_id):
		result = self.repo.getRouteById(route_id)
		route = None

		if result:
			route = result.getInfo()

		return route

	def add_stop(self, route_id, stop_id):
		result = self.repo.add_stop(route_id, stop_id)
		return result

	def remove_stop(self, route_id, stop_id):
		result = self.repo.remove_stop(route_id, stop_id)

		return result

	def getStopsNotInRoute(self, route_id):
		stops = self.repo.getStopsNotInRoute(route_id)

		return stops

	def getRouteStops(self, route_id):
		stops =  self.repo.getRouteStops(route_id)

		return stops