# Exercise 1 — Undirected graph
n = 4

edges = [
    [0, 1],
    [0, 2],
    [1, 3]
]

def build_undirected_graph(n, edges):
    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    print(graph)

# Exercise 2 — Directed graph
def build_directed_graph(n, edges):
    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        
    print(graph)

# Exercise 3 - BFS Traversal
from collections import deque

def graphs_bfs_traversal(graph, start):
    queue = deque([start])
    visited = {start}

    while queue:
        node = queue.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
# graph = [
#     [1, 2],    # 0
#     [0, 3],    # 1
#     [0, 3],    # 2
#     [1, 2, 4], # 3
#     [3]        # 4
# ]

graph = [
    [1,2],
    [0,3],
    [0,3],
    [1,2]
]
# graphs_bfs_traversal(graph, 0)
# print('\n')

def graphs_dfs_traversal_connected_graph(graph, start, res):
    def dfs(node):
        # print(node)
        res.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)

    visited = {start}
    dfs(start)
    print(res)

# graphs_dfs_traversal_connected_graph(graph, 0, [])

def graphs_dfs_traversal_disconnected_graph(graph, res):
    def dfs(node):
        res.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)

    visited = set()

    for i in range(len(graph)):
        if i not in visited:
            visited.add(i)
            dfs(i)

    print(res)

graph = [
    [1],
    [0],
    [3],
    [2]
] 
graphs_dfs_traversal_disconnected_graph(graph, [])