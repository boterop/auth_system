import psycopg2
import os


class Database():
    ALREADY_EXIST = "User already exist"
    REGISTERED = "User was registered"

    def __init__(self, database):
        try:
            connection = psycopg2.connect(database=database,
                                          user=os.getenv("POSTGRES_USER"),
                                          host=os.getenv("POSTGRES_HOST"),
                                          password=os.getenv(
                                              "POSTGRES_PASSWORD"),
                                          port=5432)

            self.connection = connection
            self.cursor = connection.cursor()
        except Exception as e:
            print("ERROR creating connection: {}".format(e))

    def escape(data):
        return data

    def verify_user(self, user, password):
        self.cursor.execute(
            "SELECT id FROM users WHERE name=%s AND password=%s;", (user, password))
        results = self.cursor.fetchall()
        self.connection.commit()
        self.connection.close()
        return len(results) > 0

    def register_user(self, user, password):
        self.cursor.execute("SELECT id FROM users WHERE name=%s;", (user,))
        users = self.cursor.fetchall()
        is_created = len(users) > 0
        if not is_created:
            self.cursor.execute(
                "INSERT INTO users (name, password) VALUES (%s, %s) RETURNING id;", (user, password))
            result = self.cursor.fetchall()
            self.connection.commit()
        else:
            result = self.ALREADY_EXIST
        self.connection.close()
        return result
