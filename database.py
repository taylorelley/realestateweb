import pymysql

class Database:
    def __init__(self, host, user, password, db):
        self.connection = pymysql.connect(host=host, user=user, password=password, db=db)

    def execute_query(self, query):
        with self.connection.cursor() as cursor:
            cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()
