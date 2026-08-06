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