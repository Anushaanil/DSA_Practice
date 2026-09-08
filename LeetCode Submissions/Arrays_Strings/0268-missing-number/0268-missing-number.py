class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        current_total = sum(nums)
        n = len(nums)
        actual_total = (n*(n+1))//2
        
        return actual_total - current_total