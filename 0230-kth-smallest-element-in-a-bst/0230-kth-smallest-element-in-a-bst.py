# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        # inorder traversal in BST gives sorted order, 
        # add them to list and return it's kth element as soon as found.
        ans = None
        elements = []
        
        def inorder_traversal(node, k):
            nonlocal ans, elements

            if not node:
                return
            
            # left node first

            if node.left: 
                inorder_traversal(node.left, k)
                
            elements.append(node.val)

            if len(elements) == k:
                ans = elements[-1]
                return

            if node.right: 
                inorder_traversal(node.right, k)

        inorder_traversal(root, k)
        return ans