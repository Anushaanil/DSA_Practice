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
# graphs_dfs_traversal_disconnected_graph(graph, [])

def detect_cycle_unidrected_graph_dfs(graph):
    def dfs(node, parent):
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                if dfs(nei, node):
                    return True
            # Main condition where neighbor is not immediate parent and still visited.
            elif nei !=parent:
                return True
        return False

    
    visited = set()
    # To handle disconnected components
    for node in range(len(graph)):
        if node not in visited:
            if dfs(0, None): return True
    return False

graph = [
    [1, 2],
    [0, 3],
    [0, 4],
    [1],
    [2]
]

graph = [[0]]

# print(detect_cycle_unidrected_graph_dfs(graph))

def detect_cycle_undirected_graph_bfs(graph):
    visited, q = set(), deque()

    def bfs(node):
        q.append((node, -1))
        visited.add(node)
        
        while q:
            n, parent = q.popleft()
            for nei in graph[n]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, n))
                    
                elif nei!= parent:
                    return True
        return False


    for node in range(len(graph)):
        if node not in visited:
            if bfs(node): return True

    return False

graph = [[0]]
graph = [
    [1, 2],
    [0, 3],
    [0, 4],
    [1],
    [2]
]

# print(detect_cycle_undirected_graph_bfs(graph))


def detect_cycle_directed_graph_dfs(graph):
    def dfs(node, recurPath):
        visited.add(node)
        recurPath.add(node)

        for nei in graph[node]:
            if nei not in visited:
                if dfs(nei, recurPath):
                    return True
            # Main condition where neighbor is in recurPath and visited.
            elif nei in recurPath:
                return True
            
        recurPath.remove(node)

        return False

    
    visited = set()
    recurPath = set()
    # To handle disconnected components
    for node in range(len(graph)):
        if node not in visited:
            if dfs(node, recurPath): return True
    return False

graph = [
    [1],
    [2],
    []
]

# print(detect_cycle_directed_graph_dfs(graph))

def topological_sorting_directed_graph_dfs(graph):
    def dfs(node, stack):
        visited.add(node)

        for nei in graph[node]:
            if nei not in visited:
                dfs(nei, stack)

        stack.append(node)

    
    visited = set()
    stack = []

    # To handle disconnected components
    for node in range(len(graph)):
        if node not in visited:
            dfs(node, stack)
    
    print(stack)
    while stack:
        print(stack.pop())

graph = [
    [],
    [],
    [3],
    [1],
    [0, 1],
    [0, 2]
]
topological_sorting_directed_graph_dfs(graph)
