import psycopg2

class PropertyDataStorage:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="realestate",
            user="postgres",
            password="secret",
            host="db",
            port="5432"
        )

    def store_property_data(self, data):
        # Implement logic to store data in the database

    def get_all_properties(self):
        # Implement logic to fetch all properties from the database

    def get_property_data(self, id):
        # Implement logic to fetch a specific property from the database
