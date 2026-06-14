class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # p1 = p2 = 2
        
        # while p2<len(nums):
        #     if nums[p2] == nums[p1-2]:
        #         p2+=1
        #     else:
        #         nums[p1] = nums[p2]
        #         p1+=1
        #         p2+=1
        # return p1
        k = 2
        for i in range(2, len(nums)):
            if nums[i]!=nums[k-2]:
                nums[k]= nums[i]
                k+=1
        return k

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # p1 = p2 = 2
        
        # while p2<len(nums):
        #     if nums[p2] == nums[p1-2]:
        #         p2+=1
        #     else:
        #         nums[p1] = nums[p2]
        #         p1+=1
        #         p2+=1
        # return p1
        k = 2
        for i in range(2, len(nums)):
            if nums[i]!=nums[k-2]:
                nums[k]= nums[i]
                k+=1
        return k

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = p2 = 2

        while p2<len(nums):
            if nums[p2]!=nums[p1-2]:
                nums[p1] = nums[p2]
                p1+=1
            p2+=1
        return p1