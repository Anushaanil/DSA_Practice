class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # This is the sliding window derived ans from my understanding
        if len(t) > len(s):
            return ""
        
        if s == t:
            return t
        
        # have is whatever unique keys we have right now
        # need is the required amount of different keys

        l, r, have = 0, 0, 0
        t_items = {} # required
        cur_window = {} # cur present
        ans = ""

        for ch in t:
            t_items[ch] = t_items.get(ch, 0) + 1

        need = len(t_items) 

        while r < len(s):
            cur_window[s[r]] = 1 + cur_window.get(s[r], 0)
            
            if s[r] in t_items and cur_window[s[r]] == t_items[s[r]]:
                have+=1

            # window valid, so shrink the window by incrementing l
            # previous condition - all(t_items[key] <= cur_window.get(key,0) for key in t_items)
            while have == need and l <= r:
                
                if not ans or r-l+1 < len(ans):
                    ans = s[l:r+1]
                    
                if s[l] in t_items and cur_window[s[l]] == t_items[s[l]]:
                    have -= 1

                cur_window[s[l]]-=1

                if cur_window[s[l]] <=0:
                    cur_window.pop(s[l])
                l+=1
            r+=1
            
        return ans