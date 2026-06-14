class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0
        
        jumps = fathest = current_end = 0

        for i in range(n-1):
            fathest = max(fathest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = fathest
        return jumps