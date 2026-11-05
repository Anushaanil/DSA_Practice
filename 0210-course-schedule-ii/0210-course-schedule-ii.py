from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # cycle detection problem + Topological sort
        # Build Adj list first from prerequisites considering b first then a
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[v].append(u)
        
        def dfs(node):
            visited.add(node)
            curPath.add(node)

            for neighbor in adj[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in curPath:
                    return True

            curPath.remove(node)
            stack.append(node)
            return False

        visited, curPath, stack = set(), set(), []
        for node in range(numCourses):
            if node not in visited:
                if dfs(node):
                    return []
        return stack[::-1]