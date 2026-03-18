import asyncio, time

async def async_task(task_id):
    await asyncio.sleep(2)
    return f"Task {task_id} Completed"

async def run_async_task(tasks=5):
    task_list = [async_task(i) for i in range(tasks)]
    results =  await asyncio.gather(*task_list)
    return results
    # print('results', results)

def find_duplicates(nums):
    duplicates_map = {}
    duplicates = []

    for num in nums:
        if num in duplicates_map:
            duplicates_map[num] +=1
        else:
            duplicates_map[num] = 1
    
    for key, value in duplicates_map.items():
        if value > 1:
            duplicates.append(key)
    return duplicates


if __name__=="__main__":

    nums = [1,1,2,3,4,4,5,6,6]
    duplicates = find_duplicates(nums)
    # print(duplicates)
    start = time.perf_counter()
    runs = asyncio.run(run_async_task(5))
    elapsed_time = time.perf_counter() - start

    for result in runs:
        print("result: ", result)

    print(f"Total execution time in {elapsed_time:.2f} seconds")