class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0]) if m else 0

        def dfs(r, c, cur_ind, visited):
            if r<0 or c<0 or r==m or c==n or (r,c) in visited:
                return False
            
            if word[cur_ind] != board[r][c]:
                return False
            
            elif cur_ind == len(word)-1:
                return True

            visited.add((r, c))

            if dfs(r - 1, c, cur_ind+1, visited):
                return True

            if dfs(r + 1, c, cur_ind+1, visited):
                return True
            
            if dfs(r, c - 1, cur_ind+1, visited):
                return True
            
            if dfs(r, c + 1, cur_ind+1, visited):
                return True
            
            visited.remove((r,c))

            return False
        
        for i in range(m):
            for j in range(n):
                res = dfs(i, j, 0, set())
                if res:
                    return True
        return False

board = [["A", "B", "C", "E"], ["S", "F", "D", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
s = Solution()
print(s.exist(board, word))