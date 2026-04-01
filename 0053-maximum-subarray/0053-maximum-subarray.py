class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, cur_sum = nums[0], 0

        # kadane's algorithm
        for num in nums:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)

        if max_sum < 0:
            return max_sum

        return max_sum