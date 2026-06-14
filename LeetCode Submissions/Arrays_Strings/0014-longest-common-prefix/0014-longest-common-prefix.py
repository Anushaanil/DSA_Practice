class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_str = ""
    
        if not strs:
            return longest_str

        first_word = strs[0]
        
        for i, char in enumerate(first_word):
            for word in strs[1:]:
                if i >= len(word) or word[i] != char:
                    return longest_str
                
            longest_str+=char

        return longest_str
    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix

        