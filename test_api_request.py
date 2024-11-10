import requests


def fetch_animals_data(animal_name):
    # API key and basic url
    api_key = "kfRa7vAQiOLK6A+Z5erqnQ==1BeNIqtXX7CBbUT2"
    url = "https://api.api-ninjas.com/v1/animals"

    # send request
    response = requests.get(url, headers={'X-Api-Key': api_key}, params={'name': animal_name})

    if response.status_code == 200:
        data = response.json()
        if data:  # if data available
            return data
        else:  # return empty list, if animal not found
            return []
    else:
        print(f"Error: {response.status_code}")
        return []


animal_data = fetch_animals_data('animal_name')

