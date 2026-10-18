# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        max_sum = float('-inf')

        def dfs(node):
            nonlocal max_sum

            if not node:
                return 0
            
            l_sum = dfs(node.left)
            r_sum = dfs(node.right)

            max_sum = max(max_sum, node.val + max(0, l_sum)+ max(0, r_sum))

            return node.val + max(l_sum, r_sum, 0)
        
        dfs(root)
        return max_sum

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
ans = s.maxPathSum(root)
print(ans)