from config.dbconfig import pg_config
import psycopg2
import psycopg2.extras

class TrolleyDao:
    def __init__(self):
        connection_url = "dbname=%s user=%s" % (pg_config['dbname'],
                                                pg_config['user'])

        self.conn = psycopg2._connect(connection_url)

    # Schema: trolley_id, plate, capacity, mileage

    def registerTrolley(self, plate, capacity, mileage):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "INSERT INTO Trolleys(plate, capacity, mileage) VALUES (%s, %s, %s) RETURNING trolley_id;"
        cursor.execute(query, (plate, capacity, mileage))
        trolley_id = cursor.fetchone()['trolley_id']
        self.conn.commit()
        cursor.close()

        return trolley_id

    def deleteTrolley(self, trolley_id):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "DELETE FROM Trolleys WHERE trolley_id=%s RETURNING trolley_id;"
        cursor.execute(query, (trolley_id,))
        result = cursor.fetchone()['trolley_id']
        self.conn.commit()
        cursor.close()

        return result

    def getAllTrolleys(self):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "select * from Trolleys;"
        cursor.execute(query)
        result = cursor.fetchall()

        return result

    def getTrolleyById(self, trolley_id):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "select * from Trolleys where trolley_id = %s;"
        cursor.execute(query, (trolley_id,))

        result = cursor.fetchone()

        return result