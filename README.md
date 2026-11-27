# AI Engineering Journey

This repository documents my transition into AI Engineering through hands-on learning, experiments, and progressively larger projects.

I'm following a 13-week learning plan (November 2026 – January 2027), covering LLM fundamentals, APIs, RAG, agents, evaluation, and deployment.

The focus is on understanding how AI-powered applications are built in practice, not just following tutorials. I aim to implement concepts myself, experiment with different approaches, and document what I learn along the way.

## Roadmap

The roadmap is divided into four phases:

### Phase 1 — LLM APIs & Prompt Engineering

**Weeks 1–3**

- Python concepts relevant to AI engineering.
- LLM fundamentals: tokens, context windows, latency, and cost.
- Working with LLM APIs and open models.
- Streaming and structured outputs.
- Tool calling and multi-step workflows.
- Error handling, retries, and observability.

**Milestone:** A streaming assistant with conversation history, structured outputs, and multiple tools.

### Phase 2 — Retrieval-Augmented Generation (RAG)

**Weeks 4–7**

- Embeddings, vector databases, and retrieval.
- pgvector, metadata filtering, and approximate nearest-neighbour search.
- Advanced RAG: routing, iterative retrieval, and reranking.
- Evaluation datasets and retrieval/generation metrics.
- RAG security, prompt injection, and deployment.

**Milestone:** A deployed RAG application with citations, abstention, evaluation, and security testing.

### Phase 3 — AI Agents

**Weeks 8–11**

- Agent fundamentals and ReAct.
- Building agent loops and workflows.
- LangGraph, state management, and checkpoints.
- Human approval and MCP.
- Short-term and long-term memory.
- Context engineering, agent evaluation, and security.

**Milestone:** A DDIA Knowledge Agent and an MCP-powered agent with explicit state, recovery, and approval mechanisms.

### Phase 4 — System Design & Production

**Weeks 12–13**

- AI system design and architecture decisions.
- FastAPI services and streaming with SSE.
- React frontend integration.
- Docker and deployment.
- CI/CD with automated evaluation gates.
- Monitoring, tracing, cost optimization, and rollback.

**Milestone:** A deployed AI application with a design document, CI evaluation gate, monitoring, and operational documentation.

## Planned Portfolio Projects

The roadmap is designed to produce three main public portfolio pieces:

1. **Advanced RAG Application** — deployed, evaluated, secured, and supported by citations.
2. **DDIA Knowledge Agent** — a LangGraph-based agent with memory and human approval.
3. **MCP Server** — a published MCP server exposing the RAG search functionality.

Smaller weekly exercises and milestones will contribute to these larger projects.

## Weekly Progress

| Week        | Focus                                                    | Status      |
| ----------- | -------------------------------------------------------- | ----------- |
| Week 1      | Python foundations, LLM fundamentals, API experiments    | Completed   |
| Week 2      | Open models, streaming, structured outputs, tool calling | In progress |
| Week 3      | Prompt engineering and LLM application capstone          | Upcoming    |
| Weeks 4–7   | RAG, evaluation, security, deployment                    | Upcoming    |
| Weeks 8–11  | Agents, LangGraph, MCP, context engineering              | Upcoming    |
| Weeks 12–13 | System design, production, monitoring                    | Upcoming    |

## How I Learn

A few principles guide this journey:

- **Build, don't just watch:** Every major topic should involve hands-on implementation.
- **Raw first, framework second:** Understand the underlying API before using abstractions such as LangChain or LangGraph.
- **Write first, AI reviews after:** I should be able to explain the code I keep.
- **Measure what matters:** Track quality, latency, token usage, and cost where relevant.
- **Learn progressively:** Start with smaller experiments and gradually build more complete systems.

## Progress & Documentation

Each week's work is organized in its own directory, with a README documenting the experiments, implementations, and results.

- [Week 1 — Foundations & LLM Experiments](./week1/README.md)
- [Week 2 — LLM APIs, Open Models & Streaming](./week2/README.md)

More weekly documentation and projects will be added as the journey progresses.

---

_This repository is a work in progress. The roadmap is a learning plan, not a claim that all the listed technologies or projects have already been implemented._
