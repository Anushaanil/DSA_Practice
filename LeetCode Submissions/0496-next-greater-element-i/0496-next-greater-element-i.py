class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        stack = []
        nge_map = {}

        for i in range(len(nums2)-1, -1, -1):
            while stack and nums2[i] > stack[-1]:
                stack.pop()
            
            if not stack:
                nge_map[nums2[i]] = -1
            else:
                nge_map[nums2[i]] = stack[-1]
            
            stack.append(nums2[i])
        
        for num in nums1:
            res = nge_map.get(num, -1)
            result.append(res)
            
        return result