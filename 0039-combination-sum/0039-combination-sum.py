class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def dfs(res, cur_ind, cur_sum):
            if cur_sum == target:
                ans.append(res.copy())
                return
            
            if cur_ind == len(candidates) or cur_sum > target:
                return

            # Include: reuse the same candidate
            res.append(candidates[cur_ind])
            dfs(res, cur_ind, cur_sum+candidates[cur_ind])

            # Exclude: move to the next candidate
            res.pop()
            dfs(res, cur_ind+1, cur_sum)
        
        ans = []
        dfs([], 0, 0)
        return ans