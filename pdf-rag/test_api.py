from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    response = client.models.list()
    print("API Key works!")
    print([m.id for m in response.data[:5]])
except Exception as e:
    print(e)