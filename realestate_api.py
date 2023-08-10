import requests

class RealEstateAPI:
    def __init__(self):
        self.base_url = "http://api.realestate.co.nz"

    def fetch_all_data(self):
        # Fetch all the data from the API
        response = requests.get(f"{self.base_url}/all")
        data = response.json()
        return data
