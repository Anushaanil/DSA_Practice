class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def dfs(res, cur_ind):
            if len(res) == k:
                ans.append(res.copy())
            
            for i in range(cur_ind, n+1):
                res.append(i)
                dfs(res, i+1)
                res.pop()

        ans = []
        dfs([], 1)
        return ans