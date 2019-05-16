from config.dbconfig import pg_config
import psycopg2
import psycopg2.extras

class DriverDao:
    def __init__(self):
        connection_url = "dbname=%s user=%s" % (pg_config['dbname'],
                                                pg_config['user'])

        self.conn = psycopg2._connect(connection_url)

    # Schema: driver_id, license, user_id

    def register(self, license, user_id):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "INSERT INTO drivers(license, user_id) VALUES (%s, %s) RETURNING driver_id;"
        cursor.execute(query, (license, user_id,))
        driver_id = cursor.fetchone()['driver_id']
        self.conn.commit()
        cursor.close()

        return driver_id

    def getAllDrivers(self):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "select * from Drivers natural inner join Users;"
        cursor.execute(query)
        result = cursor.fetchall()

        return result

    def getDriverById(self, driver_id):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "select * from Drivers where driver_id = %s;"
        cursor.execute(query, (driver_id,))

        result = cursor.fetchone()

        return result

    def getDriverByLicense(self, license):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "select * from Drivers where license = %s;"
        cursor.execute(query, (license,))

        result = cursor.fetchone()

        return result