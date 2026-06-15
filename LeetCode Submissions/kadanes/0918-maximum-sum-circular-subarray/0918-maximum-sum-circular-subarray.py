"""
A circular maximum subarray is:

Entire Circle - One Contiguous Segment

Never think:

Entire Circle - Some negative numbers

because you're not allowed to remove arbitrary elements.

You're only allowed to "cut out" one contiguous chunk.

That's why Kadane finds the minimum contiguous chunk, not all negative values.

Think Backwards

Instead of asking:

Which elements am I taking?

Ask:

Which elements am I NOT taking?

For:

[5,-3,5]

If I take:

[last 5] + [first 5]

I'm excluding:

[-3]
"""

from typing import List
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