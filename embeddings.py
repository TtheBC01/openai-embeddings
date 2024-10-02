import os
import requests
import numpy as np
from dotenv import load_dotenv

load_dotenv()

def get_embeddings(input_text):
    url = "https://api.openai.com/v1/embeddings"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv("OPENAI_API_KEY")}"
    }
    payload = {
        "input": input_text,
        "model": "text-embedding-3-small"
    }
    response = requests.post(url, headers=headers, json=payload)

    response_data = response.json()

    embedding = response_data['data'][0]['embedding']

    embedding_vector = np.array(embedding)

    tokens_used = response_data['usage']['total_tokens']

    return embedding_vector, tokens_used