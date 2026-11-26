
import os
import time
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))



def model_called_non_streaming(model, question):
    start = time.perf_counter()

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": question}],
        temperature=0.3,
        reasoning_effort="low",
        max_completion_tokens=400,
        stream=False
    )

    latency = time.perf_counter() - start

    print("Latency:", latency)
    print("Content:", response.choices[0].message.content)
    print("Usage:", response.usage.model_dump())

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

        full_content = ""
        usage = None
        finish_reason = None

        first_token_time = None
        chunk_count = 0
        
        for chunk in response:
            if chunk.choices:
                delta = chunk.choices[0].delta
                if delta.content:
                    if first_token_time is None:
                        first_token_time = time.perf_counter() - start

                    chunk_count += 1
                    print(delta.content, end="", flush=True)
                    full_content += delta.content

                if chunk.choices[0].finish_reason:
                    finish_reason = chunk.choices[0].finish_reason

            if chunk.x_groq and chunk.x_groq.usage:
                usage = chunk.x_groq.usage

        print("TTFT:", first_token_time)
        print("Chunks received:", chunk_count)

        latency = time.perf_counter() - start
        print("Latency:", latency)

        print("\n")

        if usage:
            print("Prompt tokens:", usage.prompt_tokens)
            print("Completion tokens:", usage.completion_tokens)
            print("Total tokens:", usage.total_tokens)
        else :
            print("Usage Unavailable")

        print("Content:", repr(full_content))
        print("Finish reason:", finish_reason)

openai_gpt_oss_120b = "openai/gpt-oss-120b"
question = "Answer to the question i will ask,should be 2 line or 3 ,not more than that.What is the difference between AI and machine learning?"
qwen_qwen3_8_27b = "qwen/qwen3.8-27b"

model_called(openai_gpt_oss_120b,question)
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




