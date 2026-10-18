# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        max_sum = float('-inf') # to handle -ve tree

        def dfs(node):
            nonlocal max_sum

            if not node:
                return 0
            
            l_sum = dfs(node.left)
            r_sum = dfs(node.right)

            max_sum = max(max_sum, node.val + max(0, l_sum) + max(0, r_sum))

            return node.val + max(0, l_sum, r_sum)

        dfs(root)
        return max_sum