class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = p2 = 0
        k = 0
        n = len(nums)

        while p2<n:
            if nums[p2]==val:
                p2+=1
            else:
                temp=nums[p2]
                nums[p2]= nums[p1]
                nums[p1] = temp
                p1+=1
                p2+=1
                k+=1

        return k
        