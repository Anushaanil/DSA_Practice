from typing import List
from collections import defaultdict, deque


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list) # list of values a -> [[b, weight], [1/b, weight]]
        for i, eq in enumerate(equations):
            a, b = eq
            adjList[a].append([b, values[i]])
            adjList[b].append([a, 1/values[i]])
        
        print(adjList)

        # perform bfs over this
        def bfs(src, target):
            if src not in adjList or target not in adjList:
                return -1.0
            
            q, visit = deque(), set()
            q.append([src, 1])
            visit.add(src)

            while q:
                node, w = q.popleft()
                if node == target:
                    return w
                
                for nei, weight in adjList[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append([nei, w * weight])

            return -1.0
            
        return [bfs(q1, q2) for q1, q2 in queries]



equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]

s = Solution()
print(s.calcEquation(equations, values, queries))