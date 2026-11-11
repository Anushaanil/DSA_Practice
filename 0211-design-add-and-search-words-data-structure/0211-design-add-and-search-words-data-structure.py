class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_end = True
        
    def dfs(self, cur, cur_ind, word):

        # Base condition
        if cur_ind == len(word):
            return cur.is_end

        char = word[cur_ind]

        # Case 1: Wildcard
        if char == ".":
            for child in cur.children.values():
                if self.dfs(child, cur_ind + 1, word):
                    return True
            return False

        # Case 2: Normal character
        else:
            if char not in cur.children:
                return False

            return self.dfs(cur.children[char], cur_ind + 1, word)
        
    def search(self, word: str) -> bool:
        return self.dfs(self.root, 0, word)