class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def dfs(res, cur_ind):
            if len(res) == k:
                ans.append(res.copy())
                return
            
            
            for i in range(cur_ind, n+1):
                
                res.append(i)
                print(res)

                dfs(res, i+1)
                res.pop()

        ans = []
        dfs([], 1)
        print('op', ans)
        return ans

s = Solution()
n = 4
k = 2
s.combine(n, k)

[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]