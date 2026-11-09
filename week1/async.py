import asyncio
import time


async def apiCall():
    # faking API calls with sleep
    await asyncio.sleep(1)
    return "data"

async def concurrent():
    
    task1 = apiCall()
    task2 = apiCall()
    task3 = apiCall()

    await asyncio.gather(task1,task2,task3)

async def fake_llm_call(prompt):
    
    task = apiCall()
    await task
    return f"answer to '{prompt}' is Paris"


async def sequential():

    task1 = apiCall()
    task2 = apiCall()
    task3 = apiCall()

    await task1
    await task2
    await task3

async def main():
    before = time.perf_counter()

    # await sequential()
    # await concurrent()
    query_results = await asyncio.gather(
    fake_llm_call("What is the capital of France?"),
    fake_llm_call("What is Python?"),
    fake_llm_call("What is RAG?"),
    fake_llm_call("What is an LLM?"),
    fake_llm_call("What is asyncio?")
    )
    
    after = time.perf_counter()

    print("Time taken = ",after - before)
    print(query_results)



asyncio.run(main())
