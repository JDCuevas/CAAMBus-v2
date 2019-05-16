from flask import jsonify
from DomainLayer.itinerary import Itinerary, ItineraryRepository

class ItineraryHandler:
    # Schema: itinerary_id, date, start_time, end_time, driver_id, trolley_id, route_id

    repo = ItineraryRepository()

    def createItinerary(self, date, start_time, end_time, driver_id, trolley_id, route_id):
        itinerary = Itinerary()
        itinerary.factory(date, start_time, end_time, driver_id, trolley_id, route_id)
        return itinerary.itinerary

    def deleteItinerary(self, itinerary_id):
        itinerary_id = self.repo.deleteItinerary(itinerary_id)

        return itinerary_id

    def getAllItineraries(self):
        result = self.repo.getAllItineraries()
        itineraries = []

        if result:
            for row in result:
                itineraryInfo = row.getInfo()
                itineraries.append(itineraryInfo)

        return itineraries

    def getItinerariesByUserId(self, user_id):
        result = self.repo.getItinerariesByUserId(user_id)
        itineraries = []

        if result:
            for row in result:
                itineraryInfo = row.getInfo()
                itineraries.append(itineraryInfo)

        return itineraries