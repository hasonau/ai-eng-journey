
import os
from pathlib import Path

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")


client = Anthropic(
    api_key=os.environ["ANTHROPIC_API_KEY"]
)

response = client.messages.create(
    model=os.environ["ANTHROPIC_MODEL"],
    max_tokens=200,
    system="You are a concise assistant.",
    messages=[
        {"role": "user", "content": "Explain what an API is in two sentences."}
    ],
)

print(response)
print("Answer:", response.content)
print("Stop reason:", response.stop_reason)
print("Usage:", response.usage)