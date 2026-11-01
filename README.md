# AI Engineering Plan v4: 13 Weeks

Nov 1, 2026 to Jan 31, 2027. **AI engineering only.**
LeetCode, OOD, DDIA and other study are separate and not in this file.

Sources: CampusX 100-Day track (daily units) + full curriculum (L2, L4-L10, L15) + Cal Newport multiscale planning.

**This replaces v3.** Same content and order. Changes: AI-only time budget (3 hours/day), no LeetCode or OOD blocks, Depth is now expected, not optional.

---

## PART 1: HOW THE SYSTEM WORKS

### How much time: 3 hours of focus per day

**Recommendation: 3 hours focused, Mon-Sat. Cap at 4 hours total, never more.**

What the research says (thin, treat it as a starting point):

- Newport: novices about 1 hour of deep focus, experts up to about 4, "rarely more."
- Ericsson's deliberate-practice papers: about 3.5 hours. A critic calls the studies "criminally small," so don't treat 4 hours as proven.
- A review of work-hours studies points to roughly **3-5 hours/day** of deep work on one priority.
- Spaced learning: splitting study across days beats long marathons. Stop on time and come back tomorrow.

**So 3 hours is reasonable, not overkill.** 4+ hours of new, hard material has weak evidence behind it.

**Test it for 2 weeks.** If Block 2 output gets poor for 3 days in a row, drop to 2h30 (2 x 75 min).

### Daily schedule (about 3h15 on the clock)

- **Block 1, 90 min:** the day's Core unit. Learn it, then run its exercise. Phone away.
- **Break, 15 min:** away from the screen. Walk, water, stretch. No phone, no social media.
- **Block 2, 90 min:** Depth + build. Apply the topic to your repo, write the day's output.
- **Shutdown, 5 min:** write tomorrow's Block 1 and Block 2 tasks. Then stop.

Weekly exceptions:

- **Thursday, last 20 min of Block 2:** answer 3 track interview questions out loud.
- **Friday, Block 2:** buffer. Catch up on anything missed. Do Depth only if on track.
- **Saturday:** ship day. Finish the artifact, push it, post one LinkedIn update (10 min).
- **Sunday:** 45-min review + next week's plan + message Damian. No other work. (Day 1, Nov 1, is the one Sunday exception.)

**Overflow:** if a topic needs more time, extend Block 2 by up to 30 min. Total stays under 4 hours.

### Newport's three scales

1. **Quarter plan** (this file). Set once.
2. **Week plan:** written every Sunday, next week only.
3. **Day plan:** written at shutdown for tomorrow.

**Slip rule:** if the day breaks, re-write the blocks. Don't abandon the day.

### Proof map: each level's project, passed in this plan

- **L2 capstone** (W3): streaming tool-using assistant
- **L4 capstone** (W7): advanced RAG, deployed, with citations and abstention
- **L6 capstone** (W10): context-managed long-horizon agent vs naive baseline
- **L5 capstone, option B** (W11): MCP-powered agent (DDIA Knowledge Agent)
- **L8 capstone** (W11): red-team and secure the agentic RAG app
- **L9 capstone** (W12): AI system design document
- **L10 capstone-lite** (W13): CI eval gate, containers, monitoring, rollback, runbook
- **L15 capstone** (W13): full mock interview loop with Damian

### Three public portfolio pieces

1. **RAG project:** live link, eval suite, security tests
2. **DDIA Knowledge Agent:** LangGraph + memory + approval gate
3. **Published MCP server** over your RAG search

### Job timing (honest version)

- **Start applying after W7** (RAG live + eval suite + red-team report). Don't wait for W13.
- **Post a LinkedIn update every Saturday** with what you shipped and one number.
- Apply to remote AI backend or AI engineer roles in small batches (5 per week) from W8, and keep learning.
- No degree makes the early screening harder. Projects with live links and numbers are your counterweight. No promises on timing; hiring varies.

### Compression check (Nov 28)

You now have about 2x the hours the old plan assumed. At the **Nov 28 checkpoint**:

- If each week finished **Core + Depth by Friday,** start pulling Monday's unit from the next week forward and aim to finish **by Jan 17 (week 11)**.
- If not, keep 13 weeks and use the slack for quality.

Don't compress before W4. Evals, agents and deployment are new to you.

### Scoreboard (keep visible)

Per week: focus days done (of 6), artifact shipped Y/N, one thing explained in 2 minutes.

### Numbers sheet (start W4)

One page per project: quality scores, latency, tokens, cost per query, dataset size. Interviewers ask for numbers. Update every Saturday.

### Rules

1. **Test-out rule:** for RAG units you already built, do the exercise on your own code. Pass and explain = done.
2. **Write first, AI reviews after.** Never keep code you can't explain.
3. **Python gap list:** each Python surprise gets 3 lines. Review Sundays.
4. **Raw first, framework second.** Call the API raw, then rebuild in LangChain/LangGraph.
5. **Don't commit the DDIA PDF** to a public repo. Public demo = open-licensed corpus.
6. **Open source starts in February.**

---

## PART 2: DAY 1 (Sunday, Nov 1): DO THIS

Total: about 3h20. Goal: system live + Python gaps closed.

### Setup (20 min)

- [ ]  Notion page or paper sheet with the scoreboard
- [ ]  Public repo `ai-eng-journey` with this file as README
- [ ]  Message Damian your Week 1 plan (copy from Part 3)
- [ ]  Pick a daily start time. Write it down. Same time every day.

### Block 1: Python OOP (90 min)

Answers go in your **Python gap list**, in your own words.

**Compare with C++ (30 min)**

- [ ]  No access specifiers: what do `_x` and `__x` actually do?
- [ ]  No overloading: how do default args and `args` replace it?
- [ ]  `self` vs C++ `this`: why explicit?
- [ ]  Predict the output before running:
    
    ```python
    class A:    items = []a, b = A(), A()a.items.append(1)print(b.items)
    ```
    

**Build (60 min)**
Take one C++ class hierarchy you know. Write it three ways:

- [ ]  Plain classes: `__init__`, `__repr__`, `__eq__`
- [ ]  With `@dataclass`
- [ ]  With `ABC` + `@abstractmethod`
- [ ]  Add one `@property` and one `@classmethod` constructor
- [ ]  In 2 lines: composition vs inheritance here, and what `super()` does

### Break (15 min)

Away from the screen.

### Block 2: Type hints + Pydantic (75 min)

- [ ]  Add type hints to your Block 1 classes. Run `mypy` or `pyright` once.
- [ ]  Write a Pydantic `BaseModel` for a receipt (name, date, amount, category).
- [ ]  Feed it 3 bad inputs. Read the error messages.
- [ ]  Explain in 2 lines: dataclass vs Pydantic, and when you'd pick each.

### Shutdown (5 min)

- [ ]  Write Monday's Block 1 and Block 2 tasks
- [ ]  Rate today 1-5: was Block 1 undisturbed?

---

## PART 3: WEEK 1 (Nov 2-7)

**Focus:** Python gaps + Module 1 (LLM Fundamentals) + first API unit.
**Artifact:** folder `week1/`: token/cost estimator, 10-question model comparison, CLI chat that logs tokens and cost.

- **Mon:**
    - Block 1: generators (`yield`), context managers (`with`), decorators. Write one of each.
    - Block 2: `async`/`await`, `asyncio.gather`. Then Core 1.1 + 1.2: what an LLM does, tokens, context, latency. Same prompt 5 times, compare.
- **Tue:**
    - Block 1: Core 1.4 + 1.5: output controls, where LLMs fail. Write 10 questions (known, unknowable, false premise); record answers and confidence.
    - Block 2: Core 1.6 + 1.3: choose a model for your RAG by testing your own examples. Skim multimodal. Token-count English, code, numbers; estimate cost for 10,000 sends.
- **Wed:**
    - Block 1: Core 2.1 (Day 7) + L2-M2.1: call the API raw with the OpenAI-style SDK (Groq) and the Anthropic SDK. Inspect the full response (stop reason, usage). Keys in `.env`.
    - Block 2: same chat in LangChain. Exercise: 3-turn chat, drop history on call 3, see what it forgets.
- **Thu:**
    - Block 1: build the CLI chat with Pydantic config: model name, temperature, max tokens.
    - Block 2: log tokens and cost per call; compare two models on your 10 questions. Last 20 min: interview Qs 1-3 out loud.
- **Fri:** buffer. Fix anything unfinished; polish the CLI. Review the Python gap list.
- **Sat:** ship artifact, push, LinkedIn post (10 min).
- **Sun:** review, plan Week 2, message Damian.

---

## PART 4: WEEKS 2-13 (expand each one the Sunday before)

**Reading the weeks:**

- **Core** = 100-day units (Block 1). **Depth** = full-curriculum modules (Block 2), tagged like L7-M7.8.
- Rough day pattern: Block 1 learn + exercise, Block 2 depth + build.
- Friday Block 2 = buffer. Thursday last 20 min = interview Qs.

### PHASE 1: LLM APIs + prompts (W2-W3)

**W2 (Nov 9-14): Module 2, part 1**

- **Mon:** *Core* 2.2 open/local models (Groq open models, Ollama optional). *Depth* L2-M2.1: raw SDK + response inspection.
- **Tue:** *Core* 2.3 streaming. *Depth* L2-M2.2: cancellations, interrupted streams, time to first token.
- **Wed-Thu:** *Core* 2.4 structured outputs (10 messy receipts: valid vs valid-but-wrong). *Depth* L2-M2.4: provider-native vs LangChain; generate, validate, retry/repair/reject.
- **Fri-Sat:** *Core* 2.5 tool calling (weather + currency). *Depth* L2-M2.5/2.6: parallel and dependent calls, tool-call IDs, validate model-written arguments, tool descriptions are prompts.
- **Artifact:** receipt extractor + 2-tool assistant (raw SDK version, then LangChain). Interview Qs 13-22 across Thursdays.

**W3 (Nov 16-21): Module 2, part 2 + prompts (L2 capstone)**

- **Mon:** *Core* 2.6 chaining. *Depth* L2-M2.7: build the workflow by hand, then with LangChain.
- **Tue:** *Core* 2.7 failures. *Depth* L2-M2.9: backoff + jitter, what to retry vs fail fast, fallback models.
- **Wed:** *Core* 2.8 scale. *Depth* L2-M2.8: bounded concurrency (`asyncio.Semaphore`), batch APIs.
- **Thu:** *Core* 2.9 cost, logging, tracing. *Depth* L2-M2.10: one trace per question (LangSmith or Langfuse).
- **Fri:** *Core* Module 3 skim (3.1-3.4, 20 min each), then 3.5 testing prompts in depth. *Depth* L2-M2.11: 30-min skim of LangGraph, LlamaIndex, DSPy. (Friday buffer is used up this week; shift the skim to Saturday if behind.)
- **Sat:** *Core* 3.7 + 3.8 (versions, caching, injection basics). Assemble the capstone.
- **Artifact (L2 capstone):** streaming assistant with history, system prompt, 2-3 real tools (sequential or parallel), validated args, structured outputs, retries and timeouts, logged tokens/latency/cost. Main build in LangChain; you can explain the raw calls under it. No RAG, no agents.

### PHASE 2: RAG, closing your gaps (W4-W7)

**W4 (Nov 23-28): test-out + pgvector**

- **Mon:** *Core* 4.1-4.5 test-out on your code. *Depth* L4-M4.4: explain cosine vs dot vs Euclidean, and where semantic search fails (names, IDs).
- **Tue-Wed:** *Core* 4.6 vector DB. Move Chroma to **pgvector** with filters. *Depth* L4-M4.5: why ANN exists, HNSW vs IVF trade-offs, updates and deletes.
- **Thu:** *Core* 4.7-4.8. *Depth* L4-M4.9/M4.12: baseline without a framework; a citation only counts if the source supports the claim.
- **Fri:** *Core* 4.9-4.12 exercises on your pipeline. *Depth* L4-M4.14: rebuild retrieval + generation in LangChain or LlamaIndex. Write what you gained and lost vs hand-built.
- **Sat:** build the DDIA corpus (local). *Core* 4.3 parsing, 4.4 chunking for a book.
- **Artifact:** RAG v2 on pgvector + framework comparison note. Start the numbers sheet.
- **Nov 28 checkpoint:** run the compression check (Part 1).

**W5 (Nov 30-Dec 5): advanced RAG + start evals**

- **Mon:** *Core* 4.13 routing. *Depth* L4-M4.13: adaptive and iterative RAG.
- **Tue:** *Core* 4.14 self-correcting. *Depth* Self-RAG, CRAG, multi-hop.
- **Wed:** *Core* 4.15 text-to-SQL (optional). If skipped, start the golden set.
- **Thu:** *Core* 4.16 pick patterns by failure mode (Graph RAG: read only).
- **Fri:** *Core* 4.17 read 20-30 answers, group failures. *Depth* L7-M7.1/7.2: why vibe testing fails; programmatic vs human vs LLM judge; reference-based vs reference-free.
- **Sat:** golden set v1 (40+ questions; hand-written plus LLM-assisted, verified by you). *Depth* L7-M7.3: read offline vs online evals.
- **Artifact:** failure groups + golden set. Interview Qs 31-40.

**W6 (Dec 7-12): evals, written by you**

- **Mon-Tue:** *Core* 4.18 test sets, judge, validate the judge against your own 20 scores. *Depth* L7-M7.8 component level: retriever alone (Contextual Recall/Precision, Recall@k, MRR), generator with known-good context.
- **Wed:** *Core* 4.19 retrieval metrics. Ablate semantic vs BM25 vs hybrid vs rerank. *Depth* L10-M3: log each run in **MLflow**.
- **Thu-Fri:** *Core* 4.20. *Depth* L7-M7.8 pipeline level: RAG Triad (contextual relevancy, faithfulness, answer relevance) with **DeepEval and RAGAS**; locate failure in retrieval, context, or generation. Application level: completeness, citations, latency, tokens, cost.
- **Sat:** *Core* 4.21 one command that fails below baseline. *Depth* L7-M7.7: version test cases, configs, prompts, results.
- **Artifact:** `evaluation/` written by you + ablation table + BM25 `session_id` fix with a test.

**W7 (Dec 14-19): RAG security + deploy (L4 capstone)**

- **Mon:** *Core* 4.22. *Depth* L8-M8.1 threat model, trust boundaries.
- **Tue:** *Core* 4.23. *Depth* L8-M8.2 direct vs indirect injection; why "ignore bad instructions" fails.
- **Wed:** *Core* 4.24 permissions as search filters. *Depth* L8-M8.5 cross-tenant leaks, provenance.
- **Thu:** *Core* 4.25 PII and secrets. *Depth* L8-M8.6 redaction, no PII in logs/traces/test sets.
- **Fri:** *Core* 4.26 red-team (15 attacks). *Depth* L8-M8.7 attack-success rate as a metric.
- **Sat:** deploy v1 (Railway). README, demo video.
- **Artifact (L4 capstone):** live RAG with citations, abstention, one real improvement, latency/token/cost tracking. Plus the red-team report. Interview Qs 41-50.
- **Job step:** after this week, start applying (5 per week).

### PHASE 3: Agents (W8-W11)

**W8 (Dec 21-26): agent basics**

- **Mon:** *Core* 5.1 + start 5.2. *Depth* L5-M5.1: workflow vs agent, who decides the next step.
- **Tue:** *Core* 5.2 loop from scratch with stop conditions. *Depth* L5-M5.2: ReAct, plan-first vs step-by-step.
- **Wed-Thu:** *Core* 5.3 LangGraph. *Depth* L5-M5.7: state, nodes, conditional edges, checkpoints, state inspection.
- **Fri:** *Core* 5.4 your RAG as a tool. *Depth* L5-M5.3: read-only vs consequential tools.
- **Sat:** *Core* 5.5 planning and reflection (use only where it helps). Ship.
- **Artifact:** 3-tool agent, plain loop + LangGraph version, with a stop-on-impossible-task test.

**W9 (Dec 28-Jan 2): approval, MCP, memory**

- **Mon:** *Core* 5.6 checkpoints + approval gate. *Depth* L5-M5.7 resume and human-in-the-loop interrupts.
- **Tue:** *Core* 5.7 MCP basics. *Depth* L5-M5.4 host/client/server roles; untrusted servers.
- **Wed-Thu:** *Core* 5.8 build your MCP server over your RAG search (2 tools + 1 resource). *Depth* L5-M5.4 transports, auth, client.
- **Fri-Sat:** *Core* 5.9 memory. *Depth* L5-M5.5 write, retrieve, update, forget.
- **Artifact:** published MCP server. Interview Qs 51-60.

**W10 (Jan 4-9): context engineering (L6 capstone)**

- **Mon:** *Core* 5.10. *Depth* L6-M6.1/6.2 context as a budget; context rot; lost-in-the-middle.
- **Tue-Wed:** *Core* 5.11. *Depth* L6-M6.3 to M6.6: compaction, scratchpads, tool-output trimming, only relevant tools.
- **Thu:** *Core* 5.12 harness. *Depth* L6-M6.8: progress file, task list, self-verify before "done", step and token limits.
- **Fri:** *Core* 5.13 + 5.14 multi-agent (compact: supervisor + 2 specialists vs single agent).
- **Sat:** L6-M6.9 measure naive "keep everything" vs managed on coherence, tokens, latency, cost.
- **Artifact (L6 capstone):** DDIA Knowledge Agent v1 + before/after table.

**W11 (Jan 11-16): agent evals + security (L5 and L8 capstones)**
Heaviest week. Mon-Fri are 2 units a day.

- **Mon:** *Core* 5.15 reliability, 5.16 why agent evals differ. *Depth* L5-M5.9 budgets, idempotent actions, progress and cancel.
- **Tue:** *Core* 5.17 tool-use evals (15 tasks). *Depth* L7-M7.9 trajectories, loops, redundant calls.
- **Wed:** *Core* 5.18 recovery, memory, efficiency tests. *Depth* L7-M7.9 fault injection.
- **Thu:** *Core* 5.19 least privilege, 5.20 sandbox + approvals. *Depth* L8-M8.4 and M8.3 jailbreaks and guardrails (one layer is never enough).
- **Fri:** *Core* 5.21 MCP security, 5.22 red-team. *Depth* L8-M8.9 attack, then harden.
- **Sat:** buffer; finish the agent.
- **Artifact:** L5 capstone (option B: MCP-powered agent, 3+ tools, explicit state, stop rules, recovery, logs, approval point) + L8 capstone (red-team report and permanent regression tests). Interview Qs 61-70.

### PHASE 4: Ship it (W12-W13)

**W12 (Jan 18-23): design, service, deploy**

- **Mon:** *Core* 6.1 design doc. *Depth* L9-M9.1/9.2/9.10: requirements, baseline first, knowledge architecture, rejected alternatives, cost and latency budget, model routing, reliability.
- **Tue:** *Core* 6.2 API service. *Depth* L10-M6: FastAPI streaming (SSE), health and readiness checks, timeouts, stop spending tokens when the client disconnects, per-user isolation.
- **Wed:** *Core* 6.3 frontend (React, your stack): streaming, citations, approval prompt, feedback.
- **Thu-Fri:** *Core* 6.4 Docker Compose (backend, frontend, pgvector), secrets at runtime, deploy test + production.
- **Sat:** *Core* 6.5 + L10-M4/M7: GitHub Actions runs unit tests, then **eval gate**, then image build. Push a worse prompt, confirm it is blocked.
- **Artifact (L9 capstone):** design doc + deployed agent + CI gate. Interview Qs 71-85.

**W13 (Jan 25-30): release, monitor, portfolio (L10-lite, L15)**

- **Mon:** *Core* 6.6 canary, rollback. *Depth* L10-M3: Langfuse prompt registry with staging and production labels.
- **Tue-Wed:** *Core* 6.7 monitoring. *Depth* L10-M9: Langfuse traces (per-step cost and latency), online evals on sampled traffic, one working alert. Grafana optional.
- **Thu:** *Core* 6.8 cost and speed. *Depth* L9-M9.5: exact, prompt, retrieval, semantic caches; measure hit rate.
- **Fri:** *Core* 6.14 runbooks + 6.15 whole-app security review. *Depth* L10-M10: runbook for provider outage and quality drop.
- **Sat:** **Mock loop with Damian (L15 capstone):**
    - Round 1, scenarios (30 min): RAG accuracy drops, agent loops, latency doubles
    - Round 2, system design (45 min): clarify, baseline, architecture, trade-offs
    - Round 3, project defense (30 min): problem, requirements, baseline, architecture, decisions, failures, evals, numbers
    - Also: polish 3 READMEs, record demos.
- **Stretch (only if ahead, else February):** deploy on AWS EC2 with Docker and Secrets Manager (L10-M8).
- **Sun Jan 31:** final review. Plan February: pick 3 OSS repos.

---

## PART 5: TEMPLATES

### Sunday week plan (45 min)

1. Last week: focus days __/6, artifact shipped Y/N
2. Next week's Core units, then Depth
3. Schedule constraints
4. Saturday artifact
5. Risk: what could make me miss it?

### Daily blocks (write at shutdown)

- Start: **:** (same every day)
- Block 1, 90 min: Core unit __ (first 10 min: write what "done" looks like)
- Break, 15 min
- Block 2, 90 min: Depth/build task __
- Shutdown, 5 min

### Message to Damian (Sunday)

1. **Plan for next week:** units + artifact
2. **Last week:** what I shipped, what I didn't
3. **One thing I learned** I can explain in 2 minutes
4. **One blocker**

### Project defense (write once per project, L15-M15.8)

Problem, requirements, baseline, architecture, 3 decisions + why, trade-offs, what failed, eval results, numbers (quality, latency, cost). Be ready for: "Why not fine-tune?", "Why an agent?", "What breaks at 100x traffic?", "How do you cut cost 50%?"

---

## PART 6: WHAT I LEFT OUT, AND RISKS

### Left out on purpose

- **L0, most of L1, L3:** you have backend experience; only 3.5 and 3.8 matter.
- **L5-M5.10** (ADK, CrewAI, Agno, OpenAI Agents SDK): read the comparison criteria only; LangGraph is enough.
- **L7-M7.4/7.5** (public benchmarks): skim if curious.
- **L8-M8.8** (governance, EU AI Act, DPDP): 30-minute read in W13.
- **L9-M9.3/9.4** (gateways, inference optimization): read, don't build.
- **L11-L14** and **6.10-6.13** (self-hosting, fine-tuning).
- **AWS (L10-M8):** stretch only.

### Honest risks

- **Evals, agents and deployment are new to you.** Expect W6, W8 and W11 to run long. Friday buffer and Sunday exist for this.
- **3 hours/day is a bet, not a proven number.** Judge it by output quality in Block 2.
- **If behind:** drop Depth first, then 5.14 multi-agent, then the W3 prompt skim. Never cut W6 evals or W7 deploy.
- **L4's page has no retrieval metrics.** They come from L7-M7.8, which is why W6 uses both.
- **L7 doesn't teach judge calibration.** The 100-day unit 4.18 does: score 20 answers yourself, then compare with the judge.
- **Streamlit in L10:** use React instead; you already know it.
- **Judge each week by its artifact,** not by hours or notes.

### Sources for the time guidance

- How Long Can People Usefully Work?
- Epistemic spot check: deliberate practice
- Break length overview (low-evidence source)
