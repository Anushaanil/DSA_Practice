from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build adj list with node-> [[neighbor, weight]] mappings
        adj = defaultdict(list)

        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1/values[i]])
        
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1.0

            q, visit = deque(), set()
            q.append([src, 1.0]) # assign default weight of 1
            visit.add(src)

            while q:
                node, w = q.popleft()
                if node == target:
                    return w

                for nei, weight in adj[node]:
                    if nei not in visit:
                        q.append([nei, w * weight])
                        visit.add(nei)
                        
            return -1.0
        # call the bfs for each query to calculate weights
        return [bfs(q1, q2) for q1, q2 in queries]