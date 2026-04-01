class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, cur_sum = nums[0], 0

        # kadane's algorithm
        for num in nums:
            cur_sum = max(cur_sum, 0) + num
            max_sum = max(max_sum, cur_sum)

        return max_sum