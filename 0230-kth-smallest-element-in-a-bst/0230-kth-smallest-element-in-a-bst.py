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
        count = k
        
        def inorder_traversal(node):
            nonlocal ans, count

            if not node:
                return
            
            # left node first
            inorder_traversal(node.left)
            count-=1

            # process the current node root
            if count == 0:
                ans = node.val
                return

            # move to the right
            inorder_traversal(node.right)

        inorder_traversal(root)
        return ans