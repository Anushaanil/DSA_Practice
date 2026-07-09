'''
 # @ Create Time: 2026-07-05 20:34:58
 # @ Modified time: 2026-07-05 20:54:23
 '''
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # l will increment only when r finds 0, r is an explorer
        max_length = 0
        l = 0

        for r in range(1, len(nums)):
            print(l, r)

            while nums[l] ==0 and nums[r] == 0:
                l+=1
                
            if nums[r] == 0:
                max_length = max(max_length, r-l)
                # l+=1

        return max_length
    
s = Solution()
print(s.longestSubarray([0,1,1,1,0,1,1,0,1]))
