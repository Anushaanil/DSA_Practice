# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
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