from config.dbconfig import pg_config
import psycopg2
import psycopg2.extras

class UserDao:
    def __init__(self):
        connection_url = "dbname=%s user=%s" % (pg_config['dbname'],
                                                pg_config['user'])

        self.conn = psycopg2._connect(connection_url)

    # Schema: user_id, username, password, first_name, last_name, phone, admin

    def register(self, username, password, first_name, last_name, phone, admin):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "INSERT INTO users(username, password, first_name, last_name, phone, admin) VALUES (%s, %s, %s, %s, %s, %s) RETURNING user_id;"
        cursor.execute(query, (username, password, first_name, last_name, phone, admin))
        user_id = cursor.fetchone()['user_id']
        self.conn.commit()
        cursor.close()

        return user_id

    def getAllUsers(self):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "select * from Users;"
        cursor.execute(query)
        result = cursor.fetchall()

        return result

    def getUserById(self, user_id):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "select * from Users where user_id = %s;"
        cursor.execute(query, (user_id,))

        result = cursor.fetchone()

        return result

    def getUserByUsername(self, username):
        cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        query = "select * from Users where username = %s;"
        cursor.execute(query, (username,))

        result = cursor.fetchone()

        return result