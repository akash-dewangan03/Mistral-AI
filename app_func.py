import os
import litellm
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("MISTRALAI_API_KEY")

if not api_key:
    raise ValueError("API Key Not Found")

def get_mistral_response(prompt: str) -> str:
    try:
        response = litellm.completion(
            model="mistral-large-latest",
            messages=[{"role": "user", "content": prompt}],
            api_key=api_key,
            api_base="https://api.mistral.ai/v1",
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"

result = get_mistral_response("Tell something about text generation")
print(result)
