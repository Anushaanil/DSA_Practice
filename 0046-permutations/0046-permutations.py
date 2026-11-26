class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def dfs(res, used):
            if len(res) == len(nums):
                ans.append(res.copy())
                return
            
            for num in range(len(nums)):
                if num in used:
                    continue
                
                res.append(nums[num])
                used.add(num)

                dfs(res, used)

                res.pop()
                used.remove(num)
                
        ans = []
        dfs([], set())
        return ans