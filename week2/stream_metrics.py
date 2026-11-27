
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
    "Answer in 6 to 7 or max 10 lines, no more. "
    "What is the difference between AI and machine learning?"
)

TRIALS = 5
REQUEST_DELAY = 1
results = []


# METRICS HELPERS
def get_usage_metrics(usage):

    if not usage:
        return {}

    return {
        "prompt_tokens": getattr(usage, "prompt_tokens", None),
        "completion_tokens": getattr(usage, "completion_tokens", None),
        "total_tokens": getattr(usage, "total_tokens", None),
        "prompt_time": getattr(usage, "prompt_time", None),
        "completion_time": getattr(usage, "completion_time", None),
        "queue_time": getattr(usage, "queue_time", None),
        "total_time": getattr(usage, "total_time", None),
    }


def get_header_metrics(headers):

    return {
        "groq_region": headers.get("x-groq-region"),
        "cf_ray": headers.get("cf-ray"),
    }


def calculate_tps(metrics):

    tokens = metrics.get("completion_tokens")
    completion_time = metrics.get("completion_time")

    if tokens is not None and completion_time:
        return tokens / completion_time

    return None


# STREAMING
def model_called_streaming(model, question):

    for trial in range(1, TRIALS + 1):

        start = time.perf_counter()

        full_content = ""
        usage = None
        finish_reason = None
        first_content_time = None
        content_chunks = 0
        chunk_intervals = []
        previous_chunk_time = None
        interrupted = False
        headers = {}

        try:
            with client.chat.completions.with_streaming_response.create(
                model=model,
                messages=[{"role": "user", "content": question}],
                temperature=0.3,
                reasoning_effort="low",
                max_completion_tokens=1000,
                stream=True
            ) as raw_response:

                headers = get_header_metrics(raw_response.headers)

                for chunk in raw_response.parse():

                    if chunk.choices:

                        delta = chunk.choices[0].delta

                        if delta.content:

                            current_time = time.perf_counter()

                            if first_content_time is None:
                                first_content_time = current_time - start

                            if previous_chunk_time is not None:
                                chunk_intervals.append(
                                    current_time - previous_chunk_time
                                )

                            previous_chunk_time = current_time
                            content_chunks += 1
                            full_content += delta.content

                            print(delta.content, end="", flush=True)

                        if chunk.choices[0].finish_reason:
                            finish_reason = chunk.choices[0].finish_reason

                    if chunk.x_groq and chunk.x_groq.usage:
                        usage = chunk.x_groq.usage

        except KeyboardInterrupt:
            interrupted = True
            print("\n\nStreaming interrupted by Ctrl+C.")

        finally:

            latency = time.perf_counter() - start
            metrics = get_usage_metrics(usage)

            completion_time = metrics.get("completion_time")
            tps = calculate_tps(metrics)

            avg_chunk_latency = (
                statistics.mean(chunk_intervals) * 1000
                if chunk_intervals else None
            )

            result = {
                "model": model,
                "mode": "streaming",
                "trial": trial,
                "ttft": first_content_time,
                "latency": latency,
                "content_chunks": content_chunks,
                "avg_inter_chunk_latency_ms": avg_chunk_latency,

                "prompt_tokens": metrics.get("prompt_tokens"),
                "completion_tokens": metrics.get("completion_tokens"),
                "total_tokens": metrics.get("total_tokens"),

                "prompt_time": metrics.get("prompt_time"),
                "queue_time": metrics.get("queue_time"),
                "completion_time": completion_time,
                "server_total_time": metrics.get("total_time"),

                "tps": tps,
                "groq_region": headers.get("groq_region"),
                "cf_ray": headers.get("cf_ray"),

                "finish_reason": finish_reason,
                "interrupted": interrupted,
                "content": full_content
            }

            results.append(result)

            print("\n")
            print(f"Trial: {trial}")
            print(f"TTFT: {first_content_time}")
            print(f"Client latency: {latency:.4f}s")
            print(f"Content chunks: {content_chunks}")
            print(f"Average inter-chunk latency: {avg_chunk_latency} ms")
            print(f"Usage: {metrics}")
            print(f"Headers: {headers}")
            print(f"TPS: {tps}")
            print(f"Interrupted: {interrupted}")
            print("-" * 60)

        if interrupted:
            return False

        if trial < TRIALS:
            time.sleep(REQUEST_DELAY)

    return True


# NON-STREAMING
def model_called_non_streaming(model, question):

    for trial in range(1, TRIALS + 1):

        start = time.perf_counter()

        raw_response = client.chat.completions.with_raw_response.create(
            model=model,
            messages=[{"role": "user", "content": question}],
            temperature=0.3,
            reasoning_effort="low",
            max_completion_tokens=400,
            stream=False
        )

        latency = time.perf_counter() - start

        headers = get_header_metrics(raw_response.headers)
        response = raw_response.parse()

        metrics = get_usage_metrics(response.usage)
        tps = calculate_tps(metrics)

        content = response.choices[0].message.content
        finish_reason = response.choices[0].finish_reason

        result = {
            "model": model,
            "mode": "non-streaming",
            "trial": trial,
            "ttft": None,
            "latency": latency,
            "content_chunks": None,
            "avg_inter_chunk_latency_ms": None,

            "prompt_tokens": metrics.get("prompt_tokens"),
            "completion_tokens": metrics.get("completion_tokens"),
            "total_tokens": metrics.get("total_tokens"),

            "prompt_time": metrics.get("prompt_time"),
            "queue_time": metrics.get("queue_time"),
            "completion_time": metrics.get("completion_time"),
            "server_total_time": metrics.get("total_time"),

            "tps": tps,
            "groq_region": headers.get("groq_region"),
            "cf_ray": headers.get("cf_ray"),

            "finish_reason": finish_reason,
            "interrupted": False,
            "content": content
        }

        results.append(result)

        print(f"\nTrial: {trial}")
        print(f"Client latency: {latency:.4f}s")
        print(f"Content: {content}")
        print(f"Usage: {metrics}")
        print(f"Headers: {headers}")
        print(f"TPS: {tps}")
        print("-" * 60)

        if trial < TRIALS:
            time.sleep(REQUEST_DELAY)


# SAVE RESULTS TO CSV
def save_results():

    output_path = Path(__file__).parent / "benchmark_results.csv"

    fields = [
        "model", "mode", "trial",
        "ttft", "latency",
        "content_chunks", "avg_inter_chunk_latency_ms",

        "prompt_tokens", "completion_tokens", "total_tokens",

        "prompt_time", "queue_time",
        "completion_time", "server_total_time",

        "tps", "groq_region", "cf_ray",

        "finish_reason", "interrupted", "content"
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

    metrics_to_average = [
        "ttft",
        "latency",
        "queue_time",
        "prompt_time",
        "completion_time",
        "server_total_time",
        "completion_tokens",
        "tps",
        "avg_inter_chunk_latency_ms"
    ]

    for model in MODELS:

        for mode in ["streaming", "non-streaming"]:

            trials = [
                r for r in results
                if r["model"] == model
                and r["mode"] == mode
                and not r["interrupted"]
            ]

            if not trials:
                continue

            print(f"\nModel: {model}")
            print(f"Mode: {mode}")

            for metric in metrics_to_average:

                values = [
                    r[metric] for r in trials
                    if r.get(metric) is not None
                ]

                if values:
                    print(
                        f"Average {metric}: "
                        f"{statistics.mean(values):.4f}"
                    )

            print(f"Completed trials: {len(trials)}")

    print("\n" + "=" * 75)


# EXECUTION
if __name__ == "__main__":

    try:

        # First: streaming for all models
        for model in MODELS:

            print(f"\n\nSTREAMING: {model}")

            completed = model_called_streaming(model, QUESTION)

            if not completed:
                break

            time.sleep(REQUEST_DELAY)

        else:

            # Second: non-streaming for all models
            for model in MODELS:

                print(f"\n\nNON-STREAMING: {model}")

                model_called_non_streaming(model, QUESTION)

                time.sleep(REQUEST_DELAY)

    except KeyboardInterrupt:
        print("\nBenchmark interrupted by Ctrl+C.")

    finally:

        if results:
            save_results()
            calculate_averages()
        else:
            print("No benchmark results to save.")
