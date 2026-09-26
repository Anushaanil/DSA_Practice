"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        q = deque([root])

        while q:
            cur_level_nodes = len(q)

            for i in range(len(q)):
                cur_node = q.popleft()
                
                if i+1!= cur_level_nodes:
                    cur_node.next = q[0]

                if cur_node.left:
                    q.append(cur_node.left)
                    
                if cur_node.right:
                    q.append(cur_node.right)
        return root


        