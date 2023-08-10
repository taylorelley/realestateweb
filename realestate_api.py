import requests
import json

class RealestateAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def make_request(self, endpoint):
        url = self.base_url + endpoint
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Request to {url} failed with status code {response.status_code}")
        return response.json()

    def parse_properties(self, data):
        properties = []
        for item in data['listings']:
            properties.append(Property(item))
        return properties
