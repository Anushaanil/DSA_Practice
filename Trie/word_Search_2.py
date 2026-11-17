class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def insert(self, word: str) -> None:
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_end = True


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # construct trie first
        root = TrieNode()
        for word in words:
            root.insert(word)

        # check across the board
        m = len(board)
        n = len(board[0])

        res, visit = set(), set()

        def dfs(r, c, cur_node, cur_word):
            if r < 0 or c < 0 or r == m or c == n or (r, c) in visit or board[r][c] not in cur_node.children:
                return
            
            visit.add((r,c))
            cur_node = cur_node.children[board[r][c]]
            cur_word += board[r][c]

            if cur_node.is_end:
                res.add(cur_word)
            
            dfs(r - 1, c, cur_node, cur_word)
            dfs(r + 1, c, cur_node, cur_word)
            dfs(r, c - 1, cur_node, cur_word)
            dfs(r, c + 1, cur_node, cur_word)
            
            visit.remove((r,c))

        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "")
        
        return list(res)


board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]

s = Solution()
ans = s.findWords(board, words)
print(ans)