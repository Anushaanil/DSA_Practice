class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1]*n
        stack = []

        # move from right to left
        for i in range(2*n-1, -1, -1):
            idx = i % n
            
            while stack and nums[idx] >= stack[-1]:
                stack.pop()
                
            result[idx] = stack[-1] if stack else -1
            
            stack.append(nums[idx])
        
        return result