class Solution:
    def reverseWords(self, s: str) -> str:
        split_s = s.strip().split()

        return ' '.join(reversed(split_s))