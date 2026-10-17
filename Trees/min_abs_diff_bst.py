# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def getMinimumDifferenceWithParam(self, root: Optional[TreeNode]) -> int:
        def inorder_traversal(node, prev, min_diff):
            if not node:
                return prev, min_diff
            
            prev, min_diff = inorder_traversal(node.left, prev, min_diff)

            if prev is not None:
                min_diff = min(min_diff, node.val-prev)
            
            prev = node.val

            prev, min_diff = inorder_traversal(node.right, prev, min_diff)
            
            return prev, min_diff

        _, min_diff = inorder_traversal(root, None, float('inf'))
        return min_diff
    
    def getMinimumDifferenceNoParam(self, root: Optional[TreeNode]) -> int:
        prev = float('-inf')
        min_diff = float('inf')
        
        def inorder_traversal(root):
            nonlocal prev, min_diff
            if not root:
                return
            
            if root.left:
                inorder_traversal(root.left)

            if (root.val - prev) < min_diff:
                min_diff = root.val - prev
            prev = root.val

            if root.right:
                inorder_traversal(root.right)
            
        inorder_traversal(root)
        return min_diff
    

# [4,2,6,1,3]
root = TreeNode(4)

l1 = TreeNode(2)
l2 = TreeNode(6)
l3 = TreeNode(1)
l4 = TreeNode(3)


root.left = l1
root.right = l2
l1.left = l3
l1.right = l4

s = Solution()
# ans = s.getMinimumDifferenceWithParam(root)
ans = s.getMinimumDifferenceNoParam(root)
print(ans)