class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def dfs(res, incount, outcount):
            if incount+outcount == n*2:
                ans.append(''.join(res.copy()))
                return
            
            if incount < n:
                incount+=1
                res.append('(')
                dfs(res, incount, outcount)
                res.pop()
                incount-=1
            
            if outcount < incount:
                outcount +=1
                res.append(')')
                dfs(res, incount, outcount)
                res.pop()
                outcount-=1
        
        ans = []
        dfs("", 0, 0)
        return ans

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def dfsshort(s, incount, outcount):
            if len(s) == n*2:
                ans.append(s)
                return

            if incount < n:
                dfsshort(s+"(", incount+1, outcount)

            if outcount < incount:
                dfsshort(s+")", incount, outcount+1)

        ans = []
        dfsshort("", 0, 0)
        return ans


n = 3
s = Solution()
print(s.generateParenthesis(n))