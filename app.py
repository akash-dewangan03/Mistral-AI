import os
import litellm
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("MISTRALAI_API_KEY")

if not api_key:
    raise ValueError("API Key Not Found")

response = litellm.completion(
    model="mistral-large-latest", 
    messages=[{"role": "user", "content": "Tell something about text generaation"}],
    api_key=api_key,
    api_base="https://api.mistral.ai/v1",
)

print(response["choices"][0]["message"]["content"])
