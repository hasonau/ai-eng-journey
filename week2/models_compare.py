
import os
import time
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def model_called(model,question):
    for i in range(5):
        start = time.perf_counter()

        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": question}],
            temperature=0.3,
            reasoning_effort="low",
            max_completion_tokens=400,
        )

        latency = time.perf_counter() - start
        usage = response.usage

        print(f"\n--- Response {i + 1} ---")
        print(response.choices[0].message.content)


        if usage is not None:
            print(f"Prompt tokens: {usage.prompt_tokens}")
            print(f"Completion tokens: {usage.completion_tokens}")
            print(f"Total tokens: {usage.total_tokens}")
            print("Latency is : ",latency)
        else:
            print("Token usage information unavailable.")

        message = response.choices[0].message

        print("Content:", repr(message.content))
        print("Finish reason:", response.choices[0].finish_reason)

        print("Token details:")
        print(response.usage.model_dump())


openai_gpt_oss_20b = "openai/gpt-oss-120b"
question = "Answer to the question i will ask,should be 2 line or 3 ,not more than that.What is the difference between AI and machine learning?"
qwen_qwen3_8_27b = "qwen/qwen3.8-27b"

model_called(openai_gpt_oss_20b,question)
print("--------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------")
model_called(qwen_qwen3_8_27b,question)




