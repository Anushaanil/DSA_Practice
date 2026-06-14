class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n != 0:
            nums1[-n:] = nums2[:]
            # print(nums1)
            nums1.sort()