from typing import List

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
                    print(i, j, grid[i][j])
                    self.dfs(i, j, grid, visited, m, n)
                    islands+=1
        return islands

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]

s = Solution()
print(s.numIslands(grid))


################ NOTES ##########################
### Number of Islands – DFS (Grid Traversal)

# **1. Why check 4 directions?**
# - Land cells are connected only horizontally and vertically.
# - From current cell `(i, j)`, explore its 4 neighbours.

# | Direction | Coordinate |
# |---|---|
# | Top | `(i-1, j)` |
# | Bottom | `(i+1, j)` |
# | Left | `(i, j-1)` |
# | Right | `(i, j+1)` |

# **2. Why not diagonally?**
# - Diagonal connections don't count as connected.
# - If diagonal connectivity were allowed, we would check 8 directions instead of 4.

# **3. DFS logic**
# 1. Traverse every cell in the grid.
# 2. If cell is `"1"` (land) and unvisited → increment island count.
# 3. Call DFS to explore all connected land cells.
# 4. Mark visited cells to avoid revisiting.
# 5. Continue scanning for another unvisited land cell.

# **4. Direction array trick**

# ```python
# directions = [
#     (-1, 0),  # Top
#     (1, 0),   # Bottom
#     (0, -1),  # Left
#     (0, 1)    # Right
# ]
# ```

# **Key takeaway:** One DFS call explores an entire connected island. 
# We increment the island count only when we discover a new, unvisited land cell during the grid traversal.