class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        j = c = 0

        for i in range(len(haystack)):
            if j<len(needle):
                c+=1
                j = 0 if haystack[i] != needle[j] else j+1
                
                if j==1 and haystack[i:i+len(needle)] != needle:
                    j=0
                  
        if j == len(needle):
            return c-j
            
        return -1