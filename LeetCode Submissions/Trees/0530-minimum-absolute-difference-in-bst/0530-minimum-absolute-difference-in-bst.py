# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev, min_diff = float('-inf'), float('inf')
        
        def inorder_traversal(node):
            nonlocal prev, min_diff
            if not node:
                return
            
            if node.left: inorder_traversal(node.left)

            if (node.val-prev) < min_diff:
                min_diff = node.val-prev
            
            prev = node.val

            if node.right: inorder_traversal(node.right)

        inorder_traversal(root)
        return min_diff