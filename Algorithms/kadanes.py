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
        max_sum = nums[0]
        cur_max = 0

        # Kadane for min subarray
        min_sum = nums[0]
        cur_min = 0

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