import requests
from fastapi import FastAPI, Depends

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

sentences = [
	"That is a happy dog",
	"That is a very happy person",
	"Today is a sunny day"
]

kalimat = str(input())

# "That is a happy person"

output = query({
	"inputs": {"source_sentence": kalimat,"sentences": sentences},
})

print(output)