# Yes, you're starting the afternoon work now: **CLI chat with Pydantic configuration.**

# ### **1. What are you building?**

# A simple terminal-based chatbot, something like:

# ```
# AI Chat CLI

# Model: openai/gpt-oss-120b
# Temperature: 0.7
# Max tokens: 500

# You: What is AI?
# AI: AI is...

# Tokens used: 120
# Estimated cost: $0.000...
# ```

# You'll type questions in the terminal and receive responses from Groq.

# ### **2. What does Pydantic do here?**

# You'll create a configuration model using Pydantic:

# ```
# class ChatConfig(BaseModel):    model: str    temperature: float    max_tokens: int
# ```

# This ensures your configuration has valid values.

# For example:

# - `model` must be a string.
# - `temperature` must be a valid number.
# - `max_tokens` must be an integer.

# If someone supplies an invalid temperature or token limit, Pydantic catches it.

# ### **3. Is it harder than your LangChain exercise?**

# Likely easier

# | Component              | Difficulty                 |
# | ---------------------- | -------------------------- |
# | Groq API call          | Easy — you've done this    |
# | Pydantic configuration | Easy                       |
# | CLI input/output loop  | Easy                       |
# | Token usage logging    | Moderate                   |
# | Cost calculation       | Easy once pricing is known |

# The main new learning is connecting token usage to cost tracking.

# ### **4. First thing to do**

# Create a new file:

# `week1/cli_chat.py`

# Don't start coding everything at once.

# First, we'll build the Pydantic configuration, understand it, then integrate Groq, add the CLI loop, and finally implement token and cost logging.

# **Your target:** A working CLI chatbot that records token usage and estimated cost for every API call.


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
    




