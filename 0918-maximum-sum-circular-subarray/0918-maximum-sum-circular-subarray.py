class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum, min_sum = nums[0], nums[0]
        cur_max, cur_min = 0, 0
        total = sum(nums)

        # kadane's algo for max and min sub array
        for num in nums:
            cur_max = max(cur_max + num, num)
            cur_min = min(cur_min + num, num)

            max_sum = max(max_sum, cur_max)
            min_sum = min(min_sum, cur_min)
        
        if max_sum < 0:
            return max_sum

        return max(max_sum, total - min_sum)