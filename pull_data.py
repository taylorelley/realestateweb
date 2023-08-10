import requests
import json

def pull_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
    else:
        return json.loads(response.text)
