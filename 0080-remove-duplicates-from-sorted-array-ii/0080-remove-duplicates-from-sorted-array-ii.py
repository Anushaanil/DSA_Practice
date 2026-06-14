class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = p2 = 2
        
        while p2<len(nums):
            if nums[p2] == nums[p1-2]:
                p2+=1
            else:
                nums[p1] = nums[p2]
                p1+=1
                p2+=1
        return p1