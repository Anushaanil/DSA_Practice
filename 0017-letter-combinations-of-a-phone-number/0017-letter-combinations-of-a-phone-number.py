class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        def dfs(res, cur_ind):
            if cur_ind == len(digits):
                ans.append(''.join(res))
                return
            
            for char in digits_map[digits[cur_ind]]:
                res.append(char)
                dfs(res, cur_ind+1)
                res.pop()
                
        digits_map = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }
        ans = []
        dfs([], 0)
        return ans