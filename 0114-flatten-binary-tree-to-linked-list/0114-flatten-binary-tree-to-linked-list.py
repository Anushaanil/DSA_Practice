# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        stack = [root]
        prev = None

        while stack:

            # Take latest inserted node
            current = stack.pop()

            # Push right first
            if current.right:
                stack.append(current.right)

            # Push left later so it comes out first
            if current.left:
                stack.append(current.left)

            if not prev:
                prev = current
            else:
                prev.left = None
                prev.right = current
                prev = prev.right
                