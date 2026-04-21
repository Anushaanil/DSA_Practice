class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot = n-2

        # finding the right pivot
        while pivot>=0 and nums[pivot] >= nums[pivot+1]:
            pivot-=1

        # no pivot found
        if pivot == -1:
            nums.reverse()
            return

        # find the righmost successor to swap with
        right_most_successor = n-1
        while nums[right_most_successor] <= nums[pivot]:
            right_most_successor-=1

        # swap
        nums[pivot], nums[right_most_successor] = nums[right_most_successor], nums[pivot]

        # reverse suffix
        nums[pivot+1:] = reversed(nums[pivot+1:])
