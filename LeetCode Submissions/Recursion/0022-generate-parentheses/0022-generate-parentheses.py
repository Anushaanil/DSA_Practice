class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def dfs(res, incount, outcount):
            if (incount + outcount) == n*2:
                ans.append(''.join(res.copy()))
                return
            
            if incount < n:
                res.append('(')
                incount+=1
                dfs(res, incount, outcount)
                res.pop()
                incount-=1
            
            if outcount < incount:
                res.append(')')
                outcount+=1
                dfs(res, incount, outcount)
                res.pop()
                outcount-=1

        ans = []
        dfs([], 0, 0)
        return ans