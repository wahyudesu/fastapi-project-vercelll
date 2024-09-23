import requests

url = "http://127.0.0.1:8000/paraphrase/"
data = {
    "source_sentence": "That is a happy person",
    "sentences": [
        "That is a happy dog",
        "That is a very happy person",
        "Today is a sunny day"
    ]
}

response = requests.post(url, json=data)

print(response.json())