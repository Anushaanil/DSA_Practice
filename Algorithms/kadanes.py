'''
 # @ Create Time: 2026-06-14 17:10:17
 # @ Modified time: 2026-07-17 13:03:35
'''

"""
For a subarray ending at index i, is it better to extend the previous subarray or 
start fresh from here so that we get a maximum sum.

It's of no use to include the -ve number unless it gives larger sum, which it doesn't.

That single question leads directly to:

current_sum = max(nums[i], current_sum + nums[i])

and that is Kadane's Algorithm.

"""
def maxSubarraySumCircular(nums):
        # Tried this approach but it's not the right solution to this problem
        # max_sum = -float("inf")
        # cur_sum = 0
        # n = len(nums)
        # l, r = 0, 0

        # while r < n:
        #     if cur_sum < 0:
        #         cur_sum = 0
        #         l = r
            
        #     print(l)

        #     cur_sum += nums[r]
        #     max_sum = max(max_sum, cur_sum)

        #     if r == n-1 and cur_sum > 0:
        #         r = (r+1)%n

        #         while r < l:
        #             print(r, l)
        #             cur_sum = max(cur_sum, 0) + nums[r]
        #             max_sum = max(max_sum, cur_sum)
        #             r+=1
        #         return max_sum
            
        #     r+=1
        # return max_sum
    
        total_sum = sum(nums)

        # Kadane for max subarray
        max_sum = nums[0] # Best answer found so far
        cur_max = 0 # Maximum subarray ending at current index

        # Kadane for min subarray
        min_sum = nums[0] # Smallest subarray found so far
        cur_min = 0 # Minimum subarray ending at current index

        for num in nums:
            cur_max = max(cur_max + num, num)
            max_sum = max(max_sum, cur_max)

            cur_min = min(cur_min + num, num)
            min_sum = min(min_sum, cur_min)

        # Edge case: all negative
        if max_sum < 0:
            return max_sum

        return max(max_sum, total_sum - min_sum)

nums= [-2,4,-5,4,-5,9,4]
print(maxSubarraySumCircular(nums))