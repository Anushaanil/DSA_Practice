"""
### Combination Sum — Basic Summary

Given an array and a target, find **all combinations of numbers that add up to the target**.

Key points:

* Each number can be used **multiple times**.
* At every number, we have **2 choices**:

  * Include it → stay at the same index.
  * Exclude it → move to the next index.
* Use **backtracking** to explore both choices.
* `append()` → make a choice.
* Recursive call → explore that choice.
* `pop()` → undo the choice and try another path.
* `remaining == 0` → valid combination found.
* `remaining < 0` → stop that branch.

**Mental model:**

```text
Take → Explore → Undo
       OR
Skip → Move forward
```

The main thing to recognize: **Combination Sum = backtracking + include/exclude + reuse allowed.**

"""
def combinationSum(nums, target):
    def dfs(nums, combo_sums, cur_ind, remaining):
        if remaining == 0:
            ans.append(combo_sums.copy())
            return
        
        if remaining < 0 or cur_ind == len(nums):
            return
        
        # include
        combo_sums.append(nums[cur_ind])
        dfs(nums, combo_sums, cur_ind, remaining-nums[cur_ind])

        # exclude
        combo_sums.pop()
        dfs(nums, combo_sums, cur_ind+1, remaining)

    ans = []
    dfs(nums, [], 0, target)
    return ans

nums = [2,5,6,9]
target = 16
print(combinationSum(nums, target))