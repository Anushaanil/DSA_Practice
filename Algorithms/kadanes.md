# Maximum Sum Circular Subarray (LC 918)

## Pattern
- Kadane's Algorithm

## Main Logic
There are only **2 possible answers**:
1. Normal maximum subarray → Kadane (`max_sum`)
2. Circular maximum subarray → `total_sum - min_sum`

Return:
```python
max(max_sum, total_sum - min_sum)
```

## Main Hook ⭐
A circular subarray = **Entire array − Minimum contiguous subarray**.

Instead of finding the wrapped subarray, find the **minimum subarray to exclude**.

## Why Kadane Twice?
- `max_sum` → Best normal subarray.
- `min_sum` → Worst subarray to remove for the circular case.

## Edge Case
```python
if max_sum < 0:
    return max_sum
```

If all numbers are negative, `total_sum - min_sum = 0`, which is **not a valid subarray**.

## Complexity
### Time: O(n)
**Why?**
- One traversal computes both maximum and minimum Kadane simultaneously.
- Every element is processed exactly once.

### Space: O(1)
**Why?**
- Only a few variables (`max_sum`, `min_sum`, `cur_max`, `cur_min`, `total_sum`) are used.
- No extra array, stack, queue, or recursion.

## Memory Hook 🧠
> **Normal Answer = Kadane Max**  
> **Circular Answer = Total Sum − Kadane Min**  
> **Final = max(Normal, Circular)**