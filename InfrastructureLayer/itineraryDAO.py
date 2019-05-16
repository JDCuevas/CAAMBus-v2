from config.dbconfig import pg_config
import psycopg2
import psycopg2.extras

class ItineraryDao:
    def __init__(self):
        connection_url = "dbname=%s user=%s" % (pg_config['dbname'],
                                                pg_config['user'])

        self.conn = psycopg2._connect(connection_url)

    # Schema: itinerary_id, date, start_time, end_time, driver_id, trolley_id, route_id

    def createItinerary(self, date, start_time, end_time, driver_id, trolley_id, route_id):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "INSERT INTO Itineraries(date, start_time, end_time, driver_id, trolley_id, route_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING itinerary_id;"
        cursor.execute(query, (date, start_time, end_time, driver_id, trolley_id, route_id,))
        itinerary_id = cursor.fetchone()['itinerary_id']
        self.conn.commit()
        cursor.close()

        return itinerary_id

    def deleteItinerary(self, itinerary_id):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "DELETE FROM Itineraries WHERE itinerary_id=%s RETURNING itinerary_id;"
        cursor.execute(query, (itinerary_id,))
        result = cursor.fetchone()['itinerary_id']
        self.conn.commit()
        cursor.close()

        return result

    def getAllItineraries(self):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "select * from Itineraries natural inner join Drivers natural inner join Users natural inner join Routes natural inner join Trolleys;"
        cursor.execute(query)
        result = cursor.fetchall()

        return result

    def getItineraryById(self, itinerary_id):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "select * from Itineraries where itinerary_id = %s;"
        cursor.execute(query, (itinerary_id,))

        result = cursor.fetchone()

        return result

    def getItinerariesByUserId(self, user_id):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "select * from Itineraries natural inner join Drivers natural inner join Users natural inner join Routes natural inner join Trolleys where user_id=%s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchall()

        return result