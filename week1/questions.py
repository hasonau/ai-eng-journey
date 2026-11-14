
import os
import csv
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "openai/gpt-oss-120b"

questions = [
    # 3 Known-answer questions
    "What is the capital of France?",
    "How many sides does a hexagon have?",
    "Who wrote Romeo and Juliet?",

    # 3 Unknowable questions
    "What am I thinking about right now?",
    "What will the exact price of Bitcoin be on December 31, 2030?",
    "What did I eat for breakfast today?",

    # 4 False-premise questions
    "Why is the Sun a planet?",
    "When did humans first land on Mars?",
    "Why does the Earth have two moons?",
    "Which country won the 2022 FIFA World Cup: Brazil or Germany?",
]

with open("questions.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Question", "Answer", "Confidence (1-5)"])

    for question in questions:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "user", "content": question}
            ],
            temperature=0.5,
            max_tokens=500
        )

        answer = response.choices[0].message.content

        print("\nQuestion:", question)
        print("Answer:", answer)

        confidence = input("Your confidence in this answer (1-5): ")

        writer.writerow([question, answer, confidence])

print("\nAll questions completed. Results saved to questions.csv")
