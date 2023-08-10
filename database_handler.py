from pymongo import MongoClient

class DatabaseHandler:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['realestate']

    def store_data(self, data):
        # Store the data in the database
        self.db.properties.insert_many(data)
