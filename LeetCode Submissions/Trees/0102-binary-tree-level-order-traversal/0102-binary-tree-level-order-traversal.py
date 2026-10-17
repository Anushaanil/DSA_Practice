# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        queue = deque([root])
        output_nodes = []

        while queue:
            qsize = len(queue)
            inner_nodes = []
            for i in range(qsize):
                cur = queue.popleft()
                if cur:
                    inner_nodes.append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)

            if inner_nodes: output_nodes.append(inner_nodes)
        return output_nodes