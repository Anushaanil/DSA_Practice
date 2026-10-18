# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        queue = deque([root])
        level = 0
        outer_nodes = []

        while queue:
            level+=1
            qsize= len(queue)
            inner_nodes = []

            for _ in range(qsize):
                cur = queue.popleft()
                inner_nodes.append(cur.val)

                if cur.left:queue.append(cur.left)
                if cur.right:queue.append(cur.right)
            
            if level % 2==0:
                inner_nodes.reverse()
            outer_nodes.append(inner_nodes)
            
        return outer_nodes