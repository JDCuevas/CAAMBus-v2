from config.dbconfig import pg_config
import psycopg2
import psycopg2.extras

class RouteDao:
    def __init__(self):
        connection_url = "dbname=%s user=%s" % (pg_config['dbname'],
                                                pg_config['user'])

        self.conn = psycopg2._connect(connection_url)

    # Schema: route_id, route_name

    def createRoute(self, route_name):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "INSERT INTO Routes(route_name) VALUES (%s) RETURNING route_id;"
        cursor.execute(query, (route_name,))
        route_id = cursor.fetchone()['route_id']
        self.conn.commit()
        cursor.close()

        return route_id

    def deleteRoute(self, route_id):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "DELETE FROM Routes WHERE route_id=%s RETURNING route_id;"
        cursor.execute(query, (route_id,))
        result = cursor.fetchone()['route_id']
        self.conn.commit()
        cursor.close()

        return result

    def deleteRouteStops(self, route_id):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "DELETE FROM StopsInRoutes WHERE route_id=%s RETURNING route_id;"
        cursor.execute(query, (route_id,))
        self.conn.commit()
        cursor.close()

    def getAllRoutes(self):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "select * from Routes;"
        cursor.execute(query)
        result = cursor.fetchall()

        return result

    def getRouteById(self, route_id):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "select * from Routes where route_id = %s;"
        cursor.execute(query, (route_id,))

        result = cursor.fetchone()

        return result

    ##################### Stops #####################

    def add_stop(self, route_id, stop_id):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "INSERT INTO StopsInRoutes(route_id, stop_id) VALUES (%s, %s);"
        cursor.execute(query, (route_id, stop_id,))
        self.conn.commit()
        cursor.close()

        return stop_id

    def remove_stop(self, route_id, stop_id):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "DELETE FROM StopsInRoutes WHERE route_id=%s and stop_id=%s RETURNING stop_id;"
        cursor.execute(query, (route_id,stop_id,))

        result = cursor.fetchone()['stop_id']

        self.conn.commit()
        cursor.close()

        return result

    def getStopsNotInRoute(self, route_id):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "select * from Stops where stop_id not in (select stop_id from Stops natural inner join StopsInRoutes where route_id=%s);"
        cursor.execute(query, (route_id,))

        result = cursor.fetchall()

        return result

    def getRouteStops(self, route_id):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "select * from Routes natural inner join StopsInRoutes natural inner join Stops where route_id = %s;"
        cursor.execute(query, (route_id,))

        result = cursor.fetchall()

        return result