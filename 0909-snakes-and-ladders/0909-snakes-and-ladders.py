from collections import deque
class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        board.reverse()

        length = len(board)
        q, visited = deque(), set()
        q.append([1, 0]) # [square, moves]

        def board_position(square):
            r = (square - 1) // length
            c = (square - 1) % length

            if r % 2:
                c = length - 1 - c

            return r, c

        while q:
            square, moves = q.popleft()
            # roll dice
            for i in range(1, 7):
                nextsquare = square + i
                r, c = board_position(nextsquare)

                if board[r][c]!=-1:
                    nextsquare = board[r][c]

                if nextsquare == length * length:
                    return moves + 1
                
                if nextsquare not in visited:
                    visited.add(nextsquare)
                    q.append([nextsquare, moves + 1])
        return -1