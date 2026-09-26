'''
 # @ Create Time: 2026-09-24 23:41:19
 # @ Modified time: 2026-09-25 20:24:07
 '''

class Solution:
    def find_offsets(self, board, current_cordinates, row_size, col_size):
        print('current co', current_cordinates)
        alive_neighbors = 0
        offsets = [(-1,-1), (-1,0), (-1, 1), (0,-1), (0,1), (1,-1), (1,1),(1,0)]
        
        for offset in offsets:
            row = current_cordinates[0] + offset[0]
            col = current_cordinates[1] + offset[1]
            print(row, col)
            
            if 0 <= row < row_size and 0<= col < col_size and board[row][col] in [1,3]:
                alive_neighbors+=1

        return alive_neighbors

    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_size = len(board)
        col_size = len(board[0])
        
        # Key map to remember
        # Original  -- New -- Key State
        # 0            0      0
        # 1            0      1
        # 0            1      2
        # 1            1      3

        for row in range(row_size):
            for col in range(col_size):
                alive = self.find_offsets(board, [row, col], row_size, col_size)
                if board[row][col] == 1:
                    if alive in [2,3]:
                        board[row][col] = 3
                else:
                    if alive == 3:
                        board[row][col] = 2
        
        # rearrange the board
        for row in range(row_size):
            for col in range(col_size):
                if board[row][col] == 1:
                    board[row][col] = 0
                elif board[row][col] in [2, 3]:
                    board[row][col] = 1

class Solution:
    def find_offsets(self, board, r, c, row_size, col_size):
        alive_neighbors = 0
        offsets = [(-1,-1), (-1,0), (-1, 1), (0,-1), (0,1), (1,-1), (1,1),(1,0)]
        for offset in offsets:
            row = r - offset[0]
            col = c - offset[1]
            if row < 0 or row >= row_size or col < 0 or col >= col_size or (row == r and col == c):
                continue

            if board[row][col] in [1, 3]:
                alive_neighbors+=1

        return alive_neighbors

    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_size = len(board)
        col_size = len(board[0])

        # Key map to remember
        # Original  -- New -- Key State
        # 0            0      0
        # 1            0      1
        # 0            1      2
        # 1            1      3

        for row in range(row_size):
            for col in range(col_size):
                alive = self.find_offsets(board, row, col, row_size, col_size)

                if board[row][col] == 1:
                    if alive in [2, 3]:
                        board[row][col] = 3
                else:
                    if alive == 3:
                        board[row][col] = 2

        for row in range(row_size):
            for col in range(col_size):
                if board[row][col] == 1:
                    board[row][col] = 0

                elif board[row][col] in [2, 3]:
                    board[row][col] = 1
                    
s = Solution()
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
s.gameOfLife(board)
print(board)
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
