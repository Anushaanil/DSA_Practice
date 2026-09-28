'''
 # @ Create Time: 2026-09-25 20:31:02
 # @ Modified time: 2026-09-27 23:58:57
 '''
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        ans = []
        queue = deque([root])
        
        while queue:
            nodes = len(queue)
            qsum = 0
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                qsum+=cur.val
            
            ans.append(qsum/nodes)
            
        return ans

root = TreeNode(3)
s1 = TreeNode(9)
root.left = s1

s2 = TreeNode(20)
root.right = s2

s3 = TreeNode(15)
s2.left = s3

s4 = TreeNode(7)
s2.right = s4

s = Solution()
# ans = s.sumNumbers(root)
ans = s.averageOfLevels(root)
print(ans)