import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn

# Define the API URL and headers
API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
headers = {"Authorization": "Bearer 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"}

# Initialize the FastAPI app
app = FastAPI()

# Define the request model
class ParaphraseRequest(BaseModel):
    source_sentence: str
    sentences: List[str]

# Define the function to query the API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()

# Define the endpoint to get paraphrases
@app.post("/paraphrase/")
def get_paraphrases(request: ParaphraseRequest):
    output = query({
        "inputs": {
            "source_sentence": request.source_sentence,
            "sentences": request.sentences
        }
    })
    return output

# Add this block at the end of your file
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
