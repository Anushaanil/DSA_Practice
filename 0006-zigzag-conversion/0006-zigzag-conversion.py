class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1 or numRows>=n:
            return s
            
        res = ["" for _ in range(numRows)]
        cycle_len = 2 * numRows - 2
        
        # find row 1 and n
        rows = [0, numRows - 1]
        for row in rows:
            for i in range(row, n, cycle_len):
                res[row]+=s[i]
        
        # find middle rows
        for r in range(1, numRows-1):
            for i in range(0, n, cycle_len):
                j1 = i + r
                j2 = i + cycle_len - r
                
                if j1 < n:
                    res[r]+=s[j1]
                    
                if j2 < n:
                    res[r]+=s[j2]
            
        return ''.join(res)