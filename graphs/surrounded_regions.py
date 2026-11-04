from typing import List

class Solution:
    def dfs(self, i, j, board, m, n):
    
        if (i<0 or j<0 or i>=m or j>=n or board[i][j]!="O"):
            return
        
        board[i][j] = "T"

        # perform dfs over all 4 adjacent borders
        self.dfs(i-1, j, board, m, n) # top
        self.dfs(i, j+1, board, m, n) # right
        self.dfs(i+1, j, board, m, n) # bottom
        self.dfs(i, j-1, board, m, n) # left

    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j]=="O" and (i == 0 or j ==0 or i==m-1 or j==n-1):
                    self.dfs(i, j, board, m, n)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                    board[i][j] = "X"

                elif board[i][j]=="T":
                    board[i][j] = "O"
        print(board)

s = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
s.solve(board)