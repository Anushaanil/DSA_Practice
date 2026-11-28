class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0]) if board else 0

        def dfs(r, c, cur_ind, visited):
            if r < 0 or c < 0 or r == m or c == n or (r, c) in visited:
                return False
            
            # If it does not match, return False immediately.
            if word[cur_ind] != board[r][c]:
                return False
            
            # If it matches and is the last char, return True immediately.
            elif cur_ind == len(word) - 1:
                return True

            visited.add((r, c)) # mark the index visited

            if dfs(r-1, c, cur_ind+1, visited): # top
                return True
            
            if dfs(r+1, c, cur_ind+1, visited): # bottom
                return True
            
            if dfs(r, c-1, cur_ind+1, visited): # left
                return True
            
            if dfs(r, c+1, cur_ind+1, visited): # right
                return True
            
            visited.remove((r,c)) # remove index after exploring

            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0, set()):
                    return True
        return False