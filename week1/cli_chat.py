import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel, Field
from rich.traceback import install

install()

load_dotenv(Path(__file__).resolve().parent.parent / ".env")


def get_response(user_message: str):
    response = client.chat.completions.create(
        model=config.model,
        messages=[
            {"role": "user", "content": user_message}
        ],
        temperature=config.temperature,
        max_tokens=config.max_tokens
    )

    return response

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

while(True):
    question : str = input("Enter your question: \n")
    response = get_response(question)
    print(response.choices[0].message.content)
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
    




