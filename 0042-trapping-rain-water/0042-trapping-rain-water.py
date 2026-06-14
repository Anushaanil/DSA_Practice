class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        trap_water = 0
        leftMax = 0
        rightMax = [0]*n
        
        rightMax[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])
        
        for i in range(1, len(height)-1):
            leftMax = max(leftMax, height[i-1])
            
            if min(leftMax, rightMax[i]) > height[i]:
                trap_water += min(leftMax, rightMax[i]) - height[i]

        return trap_water