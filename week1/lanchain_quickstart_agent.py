
import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq
from langchain.agents import create_agent
from langchain_core.runnables import RunnableConfig
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import InMemorySaver
from rich.traceback import install

install(show_locals=True)
checkpointer = InMemorySaver()


load_dotenv(Path(__file__).resolve().parent.parent / ".env")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


model = ChatGroq(
    model="openai/gpt-oss-120b"
)

agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="You are a professional weather assistant. Always be polite and concise.",
    checkpointer=checkpointer
)

config : RunnableConfig = {
    "configurable": {
        "thread_id": "conversation-1"
    }
}

agent.invoke(
    {
        "messages": [
            {"role": "user", "content": "Hello ,my name is hasona"}
        ]
    },
    config = config
    
)
# Second message
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's my name?And also tell lahore weather?"}]},
    config=config
)
for message in result["messages"]:
    print(type(message).__name__, ":", message.content)


print(result["messages"][-1].content)