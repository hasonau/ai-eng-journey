# Week 2 — Model Benchmarking: Streaming vs Non-Streaming

## Objective

Compare the performance of two Groq-hosted models under streaming and non-streaming response modes:

- `openai/gpt-oss-120b`
- `qwen/qwen3.8-27b`

The objective was to understand response latency, token generation speed, streaming behavior, and consistency across repeated API requests.

## Experimental Setup

| Setting                | Value                                    |
| ---------------------- | ---------------------------------------- |
| Provider               | Groq                                     |
| Models                 | GPT-OSS 120B, Qwen 3.8 27B               |
| Trials                 | 5 per model per mode                     |
| Modes                  | Streaming and non-streaming              |
| Temperature            | 0.3                                      |
| Reasoning effort       | Low                                      |
| Delay between requests | 1 second                                 |
| Prompt                 | Explain the difference between AI and ML |

Both models were tested in both modes using repeated requests. A one-second pause was added between API requests to reduce the possibility of consecutive requests influencing the results.

## Metrics Measured

| Metric                      | Meaning                                                               |
| --------------------------- | --------------------------------------------------------------------- |
| TTFT                        | Time until the first non-empty content chunk arrives. Streaming only. |
| Client latency              | Total time observed by the client for the request.                    |
| Content chunks              | Number of non-empty content chunks received.                          |
| Average inter-chunk latency | Average time between consecutive content chunks.                      |
| Prompt tokens               | Number of input tokens.                                               |
| Completion tokens           | Number of generated output tokens.                                    |
| Total tokens                | Prompt tokens + completion tokens.                                    |
| Prompt time                 | Time Groq reports spending processing the prompt.                     |
| Queue time                  | Time Groq reports the request spent waiting in its queue.             |
| Completion time             | Time Groq reports spending generating the completion.                 |
| Server total time           | Provider-reported total processing time.                              |
| TPS                         | Completion tokens divided by provider-reported completion time.       |
| Groq region                 | Region reported in the response headers.                              |
| CF-Ray                      | Cloudflare request identifier from the response headers.              |

**Important:** Client latency and provider-reported server processing time are different measurements. TPS here represents provider-side generation throughput, not end-to-end client throughput.

## Results

### Average Latency

| Model        | Mode          | Average latency | Average TTFT |
| ------------ | ------------- | --------------: | -----------: |
| GPT-OSS 120B | Streaming     |         0.886 s |      0.646 s |
| Qwen 3.8 27B | Streaming     |     **0.473 s** |  **0.246 s** |
| GPT-OSS 120B | Non-streaming |         1.066 s |          N/A |
| Qwen 3.8 27B | Non-streaming |         2.615 s |          N/A |

### Key Observations

**1. Qwen was significantly faster in streaming mode.**

- Qwen average streaming latency: 0.473 seconds.
- GPT-OSS average streaming latency: 0.886 seconds.
- Qwen also had a considerably lower average TTFT.

**2. Qwen non-streaming had unpredictable latency.**

Its five client latency measurements were:

- Trial 1: 0.652 s
- Trial 2: 0.454 s
- Trial 3: 0.411 s
- Trial 4: 1.686 s
- Trial 5: 9.871 s

The 9.871-second outlier significantly increased its average latency. Its median latency was only 0.652 seconds, demonstrating why averages alone can be misleading when benchmarking systems with occasional latency spikes.

**3. The one-second delay did not eliminate latency spikes.**

Even after introducing a one-second pause between requests, Qwen non-streaming still experienced a request taking almost 10 seconds.

**4. Provider-reported processing time did not explain the largest Qwen delay.**

Qwen non-streaming trial 5:

| Metric            |  Result |
| ----------------- | ------: |
| Client latency    | 9.871 s |
| Queue time        | 0.004 s |
| Prompt time       | 0.005 s |
| Completion time   | 0.311 s |
| Server total time | 0.315 s |

The provider reported approximately 0.315 seconds of total processing, while the client observed 9.871 seconds.

This suggests that the delay occurred outside the provider-reported processing interval. The experiment does not establish its exact cause.

**5. GPT-OSS also experienced queue delays.**

Its non-streaming third trial had:

- Client latency: 1.867 s
- Queue time: 1.289 s
- Server total time: 0.343 s

This demonstrates that queue time can contribute significantly to observed latency.

## Final Conclusions

1. Qwen 3.8 27B was the fastest model in this experiment, particularly in streaming mode.
2. GPT-OSS 120B showed more consistent non-streaming latency in this run.
3. Qwen non-streaming experienced occasional extreme latency spikes.
4. A one-second delay between requests did not resolve those spikes.
5. Provider-reported processing metrics helped distinguish server processing time from total client-observed latency.
6. Repeated trials and metrics beyond average latency are essential for meaningful model benchmarking.

## Limitations

- Only five trials were performed per model per mode.
- Results represent one benchmarking session and may vary with provider load, network conditions, and infrastructure.
- The experiment does not establish the root cause of Qwen's non-streaming latency spikes.
- Output quality was not evaluated using a formal benchmark.
- Average inter-chunk latency measures chunk arrival intervals, not individual token generation intervals.

**Overall takeaway:** Model benchmarking is not simply about measuring which model generates tokens faster. Real-world performance also depends on queueing, response delivery, streaming behavior, and consistency.
