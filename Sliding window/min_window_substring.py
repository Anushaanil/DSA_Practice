def minWindowBruteForce(s: str, t: str) -> str:
    # This is the brute force solution I arrived by myself with a lot of attempts
    if len(t) > len(s):
        return ""
    
    if s == t:
        return t
    
    mapping = {}
    m = len(s)
    n = len(t)
    cur_len = 0
    cur_count = 0
    
    t_items = {}

    for ele in t:
        t_items[ele] = 1 + t_items.get(ele,0)
    
    r = 0

    for l in range(len(s)):
        r = l # learnt about reset with the starting letter we are considering always.
        cur_count=0 # count of letters from s which is in t
        cur_len = 0 # len of current word
        t_items_copy = t_items.copy() # used to avoid duplicates like B

        while r<m and cur_count < n:
            if s[r] in t and t_items_copy.get(s[r],0)!=0:
                t_items_copy[s[r]]-=1
                cur_count +=1
            cur_len+=1
            r+=1

        if cur_count == n:
            mapping[cur_len] = s[l:r]
     
    return mapping[min(mapping)]
        
# s = "ABOBECODEBANC"
# t = "ABC"
# print(minWindowBruteForce(s, t))

def minWindowSliding(s: str, t: str) -> str:
    # This is the sliding window optimal solution
    if len(t) > len(s):
        return ""
    
    if s == t:
        return t
    
    # have is whatever unique keys we have right now
    # need is the required amount of different keys

    l, r, have = 0, 0, 0
    # need = len(set(t)) 
    t_items = {} # required
    cur_window = {} # cur present
    ans = ""

    for ch in t:
        t_items[ch] = t_items.get(ch, 0) + 1
    
    need = len(t_items)

    while r < len(s):
        print('coming here', r, s[r])
        cur_window[s[r]] = 1 + cur_window.get(s[r], 0)
        
        if s[r] in t_items and cur_window[s[r]] == t_items[s[r]]:
            have+=1

        print(have, need, cur_window)

        # window valid, so shrink the window by incrementing l
        # previous condition - all(t_items[key] <= cur_window.get(key,0) for key in t_items)
        while have == need and l <= r:
            
            if not ans or r-l+1 < len(ans):
                ans = s[l:r+1]
                print('ANSWER', ans, l, r)

            print('here', l, s[l])
            if s[l] in t_items and cur_window[s[l]] == t_items[s[l]]:
                have -= 1

            cur_window[s[l]]-=1

            if cur_window[s[l]] <=0:
                cur_window.pop(s[l])

            l+=1
        r+=1

    return ans

s = "ABOBECODEBANC"
t = "ABC"
# s = "ab"
# t = "a"

print(minWindowSliding(s, t))