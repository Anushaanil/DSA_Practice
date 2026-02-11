'''
 # @ Create Time: 2025-07-22 09:42:17
 # @ Modified time: 2025-11-17 00:39:19
 '''


'''
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

'''
def isValidSudoku(board):
    rows = [set() for i in range(9)]
    cols = [set() for i in range(9)]
    box_indexes = [set() for i in range(9)]

    for i in range(9):
        for j in range(9):
            val = board[i][j]

            if val == ".":
                continue
            
            box_index = i//3 * 3 + j//3
            if val in rows[i] or val in cols[i] or val in box_indexes[box_index]:
                return False
            
            rows[i].add(val)
            cols[j].add(val)
            box_indexes[box_index].add(val)
    return True
        


board = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","3","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","6","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))