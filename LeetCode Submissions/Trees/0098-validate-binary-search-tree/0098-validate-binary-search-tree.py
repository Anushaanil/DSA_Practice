# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def validate(node, lower, upper):
            # Think about the base case here.
            if not node:
                return True
            
            # What should happen if node.val <= lower
            # or node.val >= upper?
            if (node.val <= lower) or (node.val >= upper):
                return False

            # What boundaries should the left child receive?
            left = validate(node.left, lower, node.val)

            # What boundaries should the right child receive?
            right = validate(node.right, node.val, upper)

            return left and right
        
        return validate(root, float('-inf'), float('inf'))