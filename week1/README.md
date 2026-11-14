# Week 1 — LLM Fundamentals & First API Projects

This folder contains the practical work completed during Week 1 of my AI Engineering roadmap (November 2–7, 2026).

The focus was understanding LLM fundamentals, working with tokens and API usage, experimenting with different models, and building a basic conversational CLI application.

## Projects & Experiments

### 1. Tokenization — `tokens.py`

- Used `tiktoken` to encode text and inspect token IDs.
- Compared token counts for English text, Python code, and numerical data.
- Examined the relationship between character count and token count.
- Experimented with model-specific encodings.

### 2. Python Concepts for AI Engineering

| File                 | What I practised                                                        |
| -------------------- | ----------------------------------------------------------------------- |
| `decorators.py`      | Function decorators, `*args`, `**kwargs`, and execution timing          |
| `context_manager.py` | Custom context managers, `__enter__`, `__exit__`, and `@contextmanager` |
| `async.py`           | `async`/`await`, `asyncio.gather()`, and concurrent execution           |

### 3. API Integration & Response Inspection

- Used the OpenAI SDK with Groq's OpenAI-compatible API endpoint.
- Experimented with the OpenAI and Anthropic SDKs.
- Inspected response objects rather than extracting only the generated text.
- Examined token usage, latency, finish reasons, and response metadata.
- Compared repeated responses to the same prompt.

Relevant files:

- `openai-sdk-to-groq.py`
- `test_openai_api.py`
- `test_anthropic_api_key.py`
- `api_comparison.md`

### 4. Model Comparison — GPT-OSS 20B vs 120B

Designed a small experiment containing 10 questions:

- 3 questions with known answers.
- 3 questions that the model could not reasonably know.
- 4 questions containing false premises.

Both models answered the known questions correctly and handled the unknowable questions appropriately.

| Metric                           | GPT-OSS 20B | GPT-OSS 120B |
| -------------------------------- | ----------: | -----------: |
| Average response time            |       0.94s |        1.37s |
| Blank responses                  |           2 |            0 |
| False premises handled correctly |   Not all 4 |          4/4 |

**Observation:** GPT-OSS 20B was approximately 31% faster in this experiment, while GPT-OSS 120B was more reliable at identifying false premises.

These results come from a small experiment, not a formal benchmark.

Results are stored in:

- `questions_gpt_oss_20b.csv`
- `questions_gpt_oss_120b.csv`

### 5. CLI Chat Application — `cli_chat.py`

Built a basic conversational application using Groq's API.

Features:

- Conversation history maintained across turns.
- Configurable model, temperature, and maximum tokens using Pydantic.
- Finish-reason inspection.
- Empty-response handling.
- Prompt, completion, and total token tracking.
- Estimated API cost per call.
- CSV logging of API usage and estimated cost.

The application records each API call in `calls.csv`.

### 6. Introductory LangChain Agent — `lanchain_quickstart_agent.py`

- Integrated Groq with LangChain's `ChatGroq`.
- Created an agent using `create_agent`.
- Registered a dummy weather function as a tool.
- Used an in-memory checkpointer to maintain conversation state across turns.

This was an introductory exercise in understanding how an agent can decide to call a tool.

## Running the Projects

The project uses Python and a virtual environment.

Install the required packages used by these exercises:

```bash
pip install groq openai anthropic python-dotenv pydantic tiktoken rich langchain langchain-groq langgraph
```

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
ANTHROPIC_MODEL=your_anthropic_model
```

Run an individual exercise from the project root:

```bash
python week1/tokens.py
python week1/cli_chat.py
python week1/lanchain_quickstart_agent.py
```

Other exercises can be run in the same way.

**Note:** The CLI's estimated cost uses the per-token rates configured in its source code. It is an estimate, not a live billing calculation.

## Key Takeaways

- Tokenization directly affects context usage and API cost.
- API response metadata provides information beyond the generated answer.
- Model size can involve trade-offs between latency and reliability.
- Conversation history must be explicitly maintained when building a multi-turn chat application.
- Tool calling introduces a way for an LLM to interact with external functions.
- Logging token usage, latency, and cost makes API behaviour measurable.

**Week 1 status: Completed.**
