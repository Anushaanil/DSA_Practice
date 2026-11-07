from collections import deque
class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        length = len(board)
        board.reverse()

        def intPosition(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2:
                c = length - 1 - c

            return [r, c]
        
        q, visited = deque([1, 0]), {1} # square, moves

        while q:
            square, moves = q.popleft()

            # roll dice
            for i in range(1, 7):
                nextsquare = square + i
                if nextsquare > length * length:
                    continue

                r, c = intPosition(nextsquare)
                if board[r][c]!=-1:
                    nextsquare = board[r][c]

                if nextsquare == length * length:
                    return moves + 1
                
                if nextsquare not in visited:
                    visited.add(nextsquare)
                    q.append([nextsquare, moves + 1])
        return -1
    
board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
s = Solution()
sol = s.snakesAndLadders(board)
print(sol)