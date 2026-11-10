
import os
import time
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

model = "openai/gpt-oss-120b"
question = "Answer to the question i will ask,should be 2 line or 3 ,not more than that.What is the difference between AI and machine learning?"

for i in range(5):
    start = time.perf_counter()

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": question}],
        temperature=0
    )

    latency = time.perf_counter() - start
    usage = response.usage

    print(f"\n--- Response {i + 1} ---")
    print(response.choices[0].message.content)

    usage = response.usage

    if usage is not None:
        print(f"Prompt tokens: {usage.prompt_tokens}")
        print(f"Completion tokens: {usage.completion_tokens}")
        print(f"Total tokens: {usage.total_tokens}")
        print("Latency is : ",latency)
    else:
        print("Token usage information unavailable.")