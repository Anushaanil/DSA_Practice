'''
 # @ Create Time: 2025-07-22 09:42:17
 # @ Modified time: 2026-04-21 13:27:11
 '''


'''
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

'''
# def isValidSudoku(board):
#     rows = [set() for i in range(9)]
#     cols = [set() for i in range(9)]
#     box_indexes = [set() for i in range(9)]

#     for i in range(9):
#         for j in range(9):
#             val = board[i][j]

#             if val == ".":
#                 continue
            
#             box_index = i//3 * 3 + j//3
#             if val in rows[i] or val in cols[i] or val in box_indexes[box_index]:
#                 return False
            
#             rows[i].add(val)
#             cols[j].add(val)
#             box_indexes[box_index].add(val)
#     return True
        
def isValidSudoku(board):
    row_sets = [set() for _ in range(9)]
    col_sets = [set() for _ in range(9)]
    sub_grid_sets = [[set() for _ in range(3)] for _ in range(3)]
    
    for row in range(9):
        for col in range(9):
            val = board[row][col]

            if val == ".":
                continue

            if val in row_sets[row] or val in col_sets[col] or val in sub_grid_sets[row//3][col//3]:
                return False

            row_sets[row].add(val)
            col_sets[col].add(val)
            sub_grid_sets[row//3][col//3].add(val)

    return True

# board = [
#  ["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","3","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","6","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]

board = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","2","8",".",".",".",".","1","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","3","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))