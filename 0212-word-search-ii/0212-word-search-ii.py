class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def insert(self, word):
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_end = True

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        m, n = len(board), len(board[0])
        res, visit = set(), set()

        # construct Trie node first
        root = TrieNode()
        for word in words:
            root.insert(word)
        
        # dfs function
        def dfs(r, c, cur_node, cur_word):
            if (r < 0 or c< 0 or r == m or c == n or (r, c) in visit or board[r][c] not in cur_node.children):
                return
            
            # add the r and c to visit
            visit.add((r, c))
            cur_node = cur_node.children[board[r][c]]
            cur_word += board[r][c]

            if cur_node.is_end:
                res.add(cur_word)
            
            dfs(r-1, c, cur_node, cur_word)
            dfs(r+1, c, cur_node, cur_word)
            dfs(r, c-1, cur_node, cur_word)
            dfs(r, c+1, cur_node, cur_word)

            # remove the r and c from visit
            visit.remove((r, c))
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "")

        return list(res)