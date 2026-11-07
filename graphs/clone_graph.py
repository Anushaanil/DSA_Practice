'''
adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
'''


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def dfs(self, node, cloned):
        if not node:
            return None
        
        if node in cloned:
            return cloned[node]
        
        new_node = Node(val = node.val)
        cloned[node]=new_node
        
        for neighbor in node.neighbors:
            cloned_neighbor = self.dfs(neighbor, cloned)
            new_node.neighbors.append(cloned_neighbor)

        return new_node


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.dfs(node, {})


# 1. Form Graph from Adjacency list.
adjList = [[2,4],[1,3],[2,4],[1,3]]
nodes = {}

# 2. First create nodes and store it on hashmap

'''
There is a problem here: you can overwrite previously created nodes.
for u, v in adjList:
    nodes[u] = Node(val=u)
    nodes[v] = Node(val=v)
'''
# 2. use this approach to create nodes
for i in range(1, len(adjList)+1):
    nodes[i] = Node(val=i)

print(nodes)

# 3. Connect the nodes with it's neighbors
# for u, v in adjList:
#     unode = nodes[u]
#     vnode = nodes[v]

#     unode.neighbors.append(vnode)
#     vnode.neighbors.append(unode)

for i, neighbors in enumerate(adjList, start=1):
    for neighbor in neighbors:
        nodes[i].neighbors.append(nodes[neighbor])

s = Solution()
print(s.cloneGraph(next(iter(nodes.values()))))