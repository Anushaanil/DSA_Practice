# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def dfs_to_find_paths(root, current_path_sum):
            if root is None:
                return 0
            
            new_number = current_path_sum * 10 + root.val
            
            # leaf condition when both childs are at the end.
            if root.left is None and root.right is None:
                return new_number
            
            l_path = dfs_to_find_paths(root.left, new_number)
            r_path = dfs_to_find_paths(root.right, new_number)

            return l_path + r_path
        
        return dfs_to_find_paths(root, 0)