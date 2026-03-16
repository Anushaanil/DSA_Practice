import time, requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import asyncio

# ----- Sync tasks -----
def do_work(task_id : int, duration : float =0.1)->str:
    time.sleep(duration)
    return f"Task {task_id} Completed"


def run_sync(tasks:int = 5)->list[str]:
    results:list[str] = []

    for i in range(tasks):
        result = do_work(i, duration=0.1)
        results.append(result)
    return results

# ----- Multi Threading tasks - I/O bound tasks ----- 
def fetch_api_data(q: str)->str:
    response = requests.get("https://www.google.com/search?", params={"q": q})
    return f"API response: {response}"

def run_multi_threading(tasks:int = 5, q:str="python", max_workers:int = 5)->list[str]:
    results:list[str] = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(do_work, i, 0.1) for i in range(tasks)]

        for future in as_completed(futures):
            result = future.result()
            results.append(result)
    return results

# ----- Multi Processing Tasks - CPU Heavy ----- 
def do_cpu_work(task_id : int, iterations : int =10000000)->str:
    result = 0
    for i in range(iterations):
        result += i*i
    return f"Task {task_id} Completed {result}"

def run_multi_processing(tasks:int = 5, q:str="python", max_workers:int = 5)->list[str]:
    results:list[str] = []

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(do_cpu_work, i, 10000000) for i in range(tasks)]

        for future in as_completed(futures):
            result = future.result()
            results.append(result)
    return results

# Asyncio tasks - single threaded great for I/O bound tasks not for CPU bound tasks
async def do_async_work(task_id : int, duration : float =0.1)->str:
    await asyncio.sleep(duration)
    return f"Task {task_id} Completed"


async def run_async(tasks:int = 5)->list[str]:
    results:list[str] = []

    task_list = [do_async_work(i, duration=0.1) for i in range(tasks)]
    results = await asyncio.gather(*task_list)
    return results

if __name__ == "__main__":
    # start = time.perf_counter()
    # results = run_sync(tasks=5)

    # elapsed_time = time.perf_counter() - start

    # print("sync results - tasks ran one after another")
    # for result in results:
    #     print("result: ", result)

    start = time.perf_counter()

    # print("multi threading results - tasks ran along with another")
    # results = run_threading(tasks=5, q="python programming", max_workers=5)
    # results = run_multi_threading(tasks=5, max_workers=5)

    # print("multi processing results - tasks ran along with another in parallel using seperate process")
    # results = run_multi_processing(tasks=5, max_workers=5)

    print("asyncio results - tasks ran along with another in parallel using seperate process")
    results = asyncio.run(run_async(tasks=5))

    elapsed_time = time.perf_counter() - start

    for result in results:
        print("result: ", result)

    print(f"Total execution time in {elapsed_time:.2f} seconds")
    