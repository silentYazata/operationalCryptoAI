import psycopg2
from psycopg2 import sql

class DatabaseConfig:
    def __init__(self, db_name, user, password, host='localhost', port='5432'):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        """Establish a database connection."""
        try:
            self.connection = psycopg2.connect(
                dbname=self.db_name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Database connection established.")
        except Exception as e:
            print(f"Error connecting to database: {e}")

    def disconnect(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

    def execute_query(self, query, params=None):
        """Execute a single query."""
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            self.connection.commit()

    def fetch_query(self, query, params=None):
        """Fetch results from a query."""
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()