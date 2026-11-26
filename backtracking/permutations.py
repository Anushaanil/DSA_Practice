class Solution:
    # - Combinations: Once you select an element, you only consider elements after it.
    # - Permutations: Once you select an element, you can select any remaining unused element.
    # - For permutations, you need to track which elements have already been selected.
    #              []
    #       /      |      \
    #     1        2        3
    #   /   \    /   \    /   \
    #  2     3  1     3  1     2
    #  |     |  |     |  |     |
    #  3     2  3     1  2     1

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


nums = [1, 2, 3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
s = Solution()
ans = s.permute(nums)
print(ans)