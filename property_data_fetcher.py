import requests

class PropertyDataFetcher:
    def __init__(self):
        self.base_url = "http://api.realestate.co.nz/subscriber/"

    def get_all_properties(self):
        response = requests.get(self.base_url + "properties")
        return response.json()

    def get_property(self, id):
        response = requests.get(self.base_url + f"properties/{id}")
        return response.json()
