from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input="Hello world"
    )

    print("Success!")
    print(len(response.data[0].embedding))

except Exception as e:
    print(type(e).__name__)
    print(e)