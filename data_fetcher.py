import requests

# API key and base URL as constants
API_KEY = "kfRa7vAQiOLK6A+Z5erqnQ==1BeNIqtXX7CBbUT2"
BASE_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name):
    """fetches animals data for given 'animal_name'.
    Args: animal_name (str): name of animal to fetch data for
    Return: list of dicts, where each dict contains data about an animal or an empty list, if no data is found"""

    # send request to API
    response = requests.get(BASE_URL, headers={'X-Api-Key': API_KEY}, params={'name': animal_name})

    if response.status_code == 200:
        data = response.json()
        # Return data if available, otherwise an empty list
        if data:
            return data
        else:
            return []

    else:
        print(f"Error: {response.status_code}")
        return []
