class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D":500, "M":1000}
        total = 0
        numeral = 0

        while numeral<len(s):
            if numeral + 1 < len(s) and d[s[numeral]] < d[s[numeral + 1]]:
                total+=d[s[numeral+1]]-d[s[numeral]]
                numeral+=2
                
            else:
                total+=d[s[numeral]]
                numeral+=1
           
        return total