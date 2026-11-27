
import os
import time
import csv
import statistics
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq


# SETUP
load_dotenv(Path(__file__).resolve().parent.parent / ".env")
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODELS = [
    "openai/gpt-oss-120b",
    "qwen/qwen3.8-27b"
]

QUESTION = (
    "Answer in 2 or 3 lines, no more. "
    "What is the difference between AI and machine learning?"
)

TRIALS = 5
results = []


def get_usage_metrics(usage):
    """Safely extract usage metrics from Groq's usage object."""

    if not usage:
        return {}

    return {
        "prompt_tokens": getattr(usage, "prompt_tokens", None),
        "completion_tokens": getattr(usage, "completion_tokens", None),
        "total_tokens": getattr(usage, "total_tokens", None),
        "completion_time": getattr(usage, "completion_time", None)
    }


# STREAMING
def model_called_streaming(model, question):

    for trial in range(1, TRIALS + 1):

        start = time.perf_counter()

        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": question}],
            temperature=0.3,
            reasoning_effort="low",
            max_completion_tokens=400,
            stream=True
        )

        full_content = ""
        usage = None
        finish_reason = None
        first_token_time = None
        content_chunks = 0

        for chunk in response:

            if chunk.choices:

                delta = chunk.choices[0].delta

                if delta.content:

                    if first_token_time is None:
                        first_token_time = (
                            time.perf_counter() - start
                        )

                    content_chunks += 1
                    full_content += delta.content

                    print(delta.content, end="", flush=True)

                if chunk.choices[0].finish_reason:
                    finish_reason = chunk.choices[0].finish_reason

            if chunk.x_groq and chunk.x_groq.usage:
                usage = chunk.x_groq.usage

        latency = time.perf_counter() - start

        metrics = get_usage_metrics(usage)

        completion_time = metrics.get("completion_time")

        tps = (
            metrics["completion_tokens"] / completion_time
            if metrics.get("completion_tokens") and completion_time
            else None
        )

        result = {
            "model": model,
            "mode": "streaming",
            "trial": trial,
            "ttft": first_token_time,
            "latency": latency,
            "content_chunks": content_chunks,
            "prompt_tokens": metrics.get("prompt_tokens"),
            "completion_tokens": metrics.get("completion_tokens"),
            "total_tokens": metrics.get("total_tokens"),
            "completion_time": completion_time,
            "tps": tps,
            "finish_reason": finish_reason,
            "content": full_content
        }

        results.append(result)

        print("\n")
        print(f"Trial: {trial}")
        print(f"TTFT: {first_token_time}")
        print(f"Latency: {latency}")
        print(f"Chunks: {content_chunks}")
        print(f"Tokens: {metrics}")
        print(f"TPS: {tps}")
        print(f"Finish reason: {finish_reason}")
        print("-" * 60)


# NON-STREAMING
def model_called_non_streaming(model, question):

    for trial in range(1, TRIALS + 1):

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

        usage = response.usage
        metrics = get_usage_metrics(usage)

        completion_time = metrics.get("completion_time")

        tps = (
            metrics["completion_tokens"] / completion_time
            if metrics.get("completion_tokens") and completion_time
            else None
        )

        content = response.choices[0].message.content

        result = {
            "model": model,
            "mode": "non-streaming",
            "trial": trial,
            "ttft": None,
            "latency": latency,
            "content_chunks": None,
            "prompt_tokens": metrics.get("prompt_tokens"),
            "completion_tokens": metrics.get("completion_tokens"),
            "total_tokens": metrics.get("total_tokens"),
            "completion_time": completion_time,
            "tps": tps,
            "finish_reason": response.choices[0].finish_reason,
            "content": content
        }

        results.append(result)

        print(f"\nTrial: {trial}")
        print(f"Latency: {latency}")
        print(f"Content: {content}")
        print(f"Usage: {metrics}")
        print(f"TPS: {tps}")
        print("-" * 60)


# SAVE RESULTS TO CSV
def save_results():

    output_path = Path(__file__).parent / "benchmark_results.csv"

    fields = [
        "model", "mode", "trial", "ttft", "latency",
        "content_chunks", "prompt_tokens", "completion_tokens",
        "total_tokens", "completion_time", "tps",
        "finish_reason", "content"
    ]

    with open(output_path, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(results)

    print(f"\nResults saved to: {output_path}")


# CALCULATE AVERAGES
def calculate_averages():

    print("\n\nFINAL BENCHMARK SUMMARY")
    print("=" * 75)

    for model in MODELS:

        for mode in ["streaming", "non-streaming"]:

            trials = [
                r for r in results
                if r["model"] == model and r["mode"] == mode
            ]

            if not trials:
                continue

            print(f"\nModel: {model}")
            print(f"Mode: {mode}")

            metrics = [
                "ttft", "latency", "completion_tokens",
                "completion_time", "tps"
            ]

            for metric in metrics:

                values = [
                    r[metric] for r in trials
                    if r[metric] is not None
                ]

                if values:
                    print(
                        f"Average {metric}: "
                        f"{statistics.mean(values):.4f}"
                    )

            print(f"Trials: {len(trials)}")

    print("\n" + "=" * 75)


# EXECUTION
if __name__ == "__main__":

    for model in MODELS:

        print(f"\n\nSTREAMING: {model}")
        model_called_streaming(model, QUESTION)

        print(f"\n\nNON-STREAMING: {model}")
        model_called_non_streaming(model, QUESTION)

    save_results()
    calculate_averages()
