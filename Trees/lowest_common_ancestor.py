# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base case
        if not root:
            return root
        
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # result
        if not left:
            return right
        elif not right:
            return left
        else:
            return root

       

root = TreeNode(1)

l1 = TreeNode(2)
l2 = TreeNode(4)
l3 = TreeNode(5)
l4 = TreeNode(7)

r1 = TreeNode(3)
r2 = TreeNode(6)
r3 = TreeNode(8)
r4 = TreeNode(9)

root.left = l1
root.right = r1
l1.left = l2
r1.left = l3
r1.right = r2
r2.left = l4
r2.right = r3
r3.right = r4

s = Solution()
p = l3
q = r3
ans = s.lowestCommonAncestor(root, p, q)
print(ans.val)