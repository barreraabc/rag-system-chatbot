import os
from dotenv import load_dotenv
from mistralai import Mistral

load_dotenv()
api_key = os.getenv("API_KEY")
model = "mistral-embed"

client = Mistral(api_key=api_key)

embeddings_response = client.embeddings.create(
    model=model,
    inputs=["Embed this sentence.", "As well as this one."]
)

print(embeddings_response)