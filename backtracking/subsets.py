from typing import List
from copy import copy

def subsets(nums):
        def dfs(nums, res, cur_ind):
            if cur_ind == len(nums):
                ans.append(copy(res))
                return

            res.append(nums[cur_ind]) # include the cur ind
            dfs(nums, res, cur_ind+1)

            res.pop() # exclude the cur ind ### backtracking the choices imp step
            dfs(nums, res, cur_ind+1)

        ans = []
        dfs(nums, [], 0)
        return ans

def subsets_bit_manipulation(nums: List[int]) -> List[List[int]]:
        n_combinations = 2 ** len(nums)
        res = [[] for _ in range(n_combinations)]
        for i in range(0, n_combinations):
            for place in range(0, len(nums)):
                ((i >> place) & 1) and res[i].append(nums[place])

        return res

res1 = subsets([1,2,3,4])
print(res1)

res2 = subsets_bit_manipulation([1,2,3,4])
print(res2)
