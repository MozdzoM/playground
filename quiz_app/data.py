import requests

parameters = {
    "amount": 25,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

question_data = [result for result in data["results"]]
