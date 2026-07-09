class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # l will increment only when window is invalid i.e when it has more than 1 zero, 
        # r is an explorer

        l, zero_count, max_length = 0, 0, 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zero_count+=1
            
            while zero_count > 1:
                if nums[l] == 0:
                    zero_count -=1
                l+=1

            max_length = max(max_length, r-l)
            
        return max_length
