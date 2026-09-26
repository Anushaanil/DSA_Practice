class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # This is the sliding window optimal solution
        if len(t) > len(s):
            return ""
        
        if s == t:
            return t
        
        l, r = 0, 0
        t_items = {} # required
        cur_window = {} # cur present
        ans = ""

        for ele in t:
            t_items[ele] = 1 + t_items.get(ele,0)

        while r < len(s):
            cur_window[s[r]] = 1 + cur_window.get(s[r], 0)
            
            # window valid, so shrink the window by incrementing l
            while all(t_items[key] <= cur_window.get(key,0) for key in t_items):
                if not ans or r-l+1 < len(ans):
                    ans = s[l:r+1]
                    
                cur_window[s[l]]-=1
                if cur_window[s[l]] <=0:
                    cur_window.pop(s[l])
                l+=1
            r+=1

        return ans