"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def dfs(self, node, cloned):
        if not node:
            return None

        if node in cloned:
            return cloned[node]
        
        # create the new node
        new_node = Node(val=node.val)
        cloned[node] = new_node

        # map the neighbors using dfs
        for neighbor in node.neighbors:
            cloned_neighbor = self.dfs(neighbor, cloned)
            new_node.neighbors.append(cloned_neighbor)
            
        return new_node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.dfs(node, {})