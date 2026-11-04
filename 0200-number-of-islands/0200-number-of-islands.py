class Solution:
    def dfs(self, i, j, grid, visited, m, n):
        if (i<0 or j<0 or i>=m or j>=n or (i,j) in visited or grid[i][j]!='1'):
            return
        
        visited.add((i, j))
        
        # perform dfs over all 4 adjacent borders
        self.dfs(i-1, j, grid, visited, m, n) # top
        self.dfs(i, j+1, grid, visited, m, n) # right
        self.dfs(i+1, j, grid, visited, m, n) # bottom
        self.dfs(i, j-1, grid, visited, m, n) # left

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        m = len(grid)
        n = len(grid[0])
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and (i,j) not in visited:
                    self.dfs(i, j, grid, visited, m, n)
                    islands+=1
        return islands