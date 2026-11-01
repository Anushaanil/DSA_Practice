# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def constructTree(l, r):
            if l > r:
                return None
            
            m = (l+r)//2
            root = TreeNode(nums[m])

            root.left = constructTree(l, m-1)
            root.right = constructTree(m+1, r)

            return root
        
        return constructTree(0, len(nums)-1)