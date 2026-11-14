
import csv
import os
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel, Field
from rich.traceback import install

install()

load_dotenv(Path(__file__).resolve().parent.parent / ".env")


def get_response(user_message: str):
    messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model=config.model,
        messages=messages,
        temperature=config.temperature,
        max_tokens=config.max_tokens
    )
    print("Finish reason:", response.choices[0].finish_reason)
    return response


def log_call(response):
    with open(csv_path, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow([
                "Timestamp", "Model", "Prompt Tokens",
                "Completion Tokens", "Total Tokens", "Estimated Cost"
            ])

        if response.usage is not None:
            input_cost = (response.usage.prompt_tokens / 1_000_000) * 0.15
            output_cost = (response.usage.completion_tokens / 1_000_000) * 0.60
            total_cost = input_cost + output_cost

            writer.writerow([
                datetime.now().isoformat(),
                config.model,
                response.usage.prompt_tokens,
                response.usage.completion_tokens,
                response.usage.total_tokens,
                round(total_cost, 8)
            ])

class ChatConfig(BaseModel):
    model: str 
    temperature: float = Field(ge=0.0,le=2.0)
    max_tokens: int =  Field(ge=1)

config = ChatConfig(
    model = "openai/gpt-oss-120b",
    temperature = 0.5,
    max_tokens = 500
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages = []   
csv_path = Path(__file__).resolve().parent / "calls.csv"

while(True):
    question : str = input("Enter your question: \n")
    response = get_response(question)
    log_call(response)

    answer = response.choices[0].message.content
    if answer:
        messages.append({
            "role": "assistant",
            "content": answer
        })
        print(answer)
    else:
        print("The model returned an empty response.")

    
    if response.usage is not None:
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Completion tokens: {response.usage.completion_tokens}")
        print(f"Total tokens: {response.usage.total_tokens}")


        input_cost = (response.usage.prompt_tokens / 1_000_000) * 0.15
        output_cost = (response.usage.completion_tokens / 1_000_000) * 0.60

        total_cost = input_cost + output_cost
        print(f"Estimated cost: ${total_cost:.8f}")


    print("Do you want to keep asking more questions?")
    keep_asking = input("Continue? (y/n): ").strip().lower()

    if keep_asking == 'n':
        break
    print("Continuing ...")
    print("---------------")
    




