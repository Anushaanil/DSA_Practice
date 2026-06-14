class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

        max_val = len(nums)//2
        
        for k,v in d.items():
            if v > max_val:
                return k