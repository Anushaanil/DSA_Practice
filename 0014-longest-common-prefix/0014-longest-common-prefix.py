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