import requests

# API key and basic url
api_key = "kfRa7vAQiOLK6A+Z5erqnQ==1BeNIqtXX7CBbUT2"
url = "https://api.api-ninjas.com/v1/animals"


# test animal name
animal_name = ("unicorn")

# send request
response = requests.get(url, headers={'X-Api-Key': api_key}, params={'name': animal_name})

if response.status_code == 200:
    data = response.json()

    if data: # if data available, print response
        print("Successful response:", data)
    else: # if list is empty (specified aninmal not found)
        print(f"No results found for the specified animal: {animal_name}.")
else:
    print(f"Error: {response.status_code}", response.json())

