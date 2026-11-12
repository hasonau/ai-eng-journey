
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from rich.traceback import install

install(show_locals=False)

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

api_key = os.getenv("OPENAI_API_KEY")

print("Key loaded:", bool(api_key))
print("Key length:", len(api_key) if api_key else 0)

client = OpenAI(api_key=api_key)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.responses.create(
    model="gpt-5-mini",
    input="Explain what an API is in two sentences."
)

print(response)
print("Answer:", response.output_text)
print("Usage:", response.usage)