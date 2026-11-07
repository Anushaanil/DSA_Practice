from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # build adj list
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[v].append(u)

        # involves topo and cycle detection
        visited, currPath = set(), set()

        def dfs(node):
            visited.add(node)
            currPath.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    if dfs(nei): return True

                elif nei in currPath:
                    return True
                
            currPath.remove(node)

            return False


        for node in range(numCourses):
            if node not in visited:
                if dfs(node):
                    return False
                
        return True


s = Solution()
numCourses = 2
prerequisites = [[1,0],[0,1]]
print(s.canFinish(numCourses, prerequisites))