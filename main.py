from realestate_api import RealestateAPI
from database import Database
from property import Property

def get_all_properties(api, db):
    data = api.make_request('/properties')
    properties = api.parse_properties(data)
    for property in properties:
        query = f"INSERT INTO properties (id, title, price, location, listing_date, description) VALUES ({property.id}, '{property.title}', {property.price}, '{property.location}', '{property.listing_date}', '{property.description}')"
        db.execute_query(query)

def find_undervalued_properties(db):
    query = "SELECT * FROM properties WHERE price < (SELECT AVG(price) FROM properties)"
    db.execute_query(query)

def main():
    api = RealestateAPI('http://api.realestate.co.nz')
    db = Database('localhost', 'root', 'password', 'realestate')
    get_all_properties(api, db)
    find_undervalued_properties(db)
    db.close()

if __name__ == "__main__":
    main()
