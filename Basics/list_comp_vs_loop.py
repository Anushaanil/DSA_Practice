import time

def m1(nums):
    results = []
    for x in nums:
        results.append(x * 2)
    return results

def m2(nums):
    results = [x*2 for x in nums]
    return results

nums = list(range(10_000_000))

start = time.perf_counter()
print('start m1', )
for _ in range(10):
    m1(nums)
now = time.perf_counter()
print('end m1', now-start)

start = time.perf_counter()
print('start m2', )
for _ in range(10):
    m2(nums)
now = time.perf_counter()
print('end m2', now-start)