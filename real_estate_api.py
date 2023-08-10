import requests
from property import Property

class RealEstateAPI:
    def __init__(self):
        self.base_url = 'http://api.realestate.co.nz/'

    def fetch_properties(self):
        response = requests.get(self.base_url + 'properties')
        data = response.json()
        return [Property(**property_data) for property_data in data]
