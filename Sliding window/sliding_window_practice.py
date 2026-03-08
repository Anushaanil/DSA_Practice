'''
1️⃣ Maximum Sum Subarray of Size K
Given an array of integers and a number k, find the maximum sum of any contiguous subarray of size k.
'''

def max_sum_sub_array(arr, k):
    current_sum = sum(arr[:k])
    print(current_sum)
    l, r = 1, k
    max_sum = 0

    while r<len(arr):
        print(l, '->', r)
        print(current_sum, arr[r],arr[l-1])
        current_sum += (arr[r]-arr[l-1])
        print(current_sum)

        max_sum = max(max_sum, current_sum)
        print(max_sum)

        l+=1
        r+=1
    return max_sum

# arr = [2, 1, 5, 1, 3, 2]
# k = 3
# print(max_sum_sub_array(arr, k))

def avg_subarray_k(arr, k):
    window_sum = 0
    averages = []

    for i in range(len(arr)):
        window_sum += arr[i]

        if i>=k-1:
            averages.append(window_sum/k)
            window_sum -= arr[i-k+1]
            print(window_sum)
            
    return averages

# arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
# k = 5
# print(avg_subarray_k(arr, k))

def max_ones_after_replacing_zeros(arr, k):
    l, r, c, max_ones = 0, 0, 0, 0

    while r<len(arr):
        print(l, '->>', r)
        if arr[r]==0:
            c+=1

        while c>k:
            if arr[l]==0:
                c-=1
            l+=1

        max_ones = max(max_ones, r-l+1)
        r+=1
                
    return max_ones

# arr = [0,1,1,0,0,1,1,0,1]
# k = 2
# print(max_ones_after_replacing_zeros(arr, k))

def long_subarray_sum_lte_k(arr, k):
    l, r, cur_sum, max_len = 0, 0, 0, 0

    while r < len(arr):
        cur_sum+=arr[r]
        
        while cur_sum > k:
            cur_sum-=arr[l]
            l+=1
        
        max_len = max(max_len, r-l+1)
        r+=1

    return max_len


arr = [4,1,1,1,2,3,5]
k = 5
# print(long_subarray_sum_lte_k(arr, k))

def smallest_subarray_sum_gte_k(arr, k):
    l, cur_sum, min_len = 0, 0, float('inf')

    for r in range(len(arr)):
        cur_sum+=arr[r]

        while cur_sum >= k:
            print(l, ' --> ', r)
            min_len = min(min_len, r-l+1)
            cur_sum-=arr[l]
            l+=1
    return 0 if min_len == float('inf') else min_len

arr = [2,1,5,2,3,2]
k = 7
# print(smallest_subarray_sum_gte_k(arr, k))

from collections import defaultdict
#Longest Substring with At Most k Distinct Characters
def long_substring_atmost_k_chars(s, k):
    l = 0
    d = defaultdict(int)
    max_len = 0

    for r in range(len(s)):
        d[s[r]]+=1

        while len(d) > k:
            d[s[l]]-=1
            if d[s[l]] < 1:
                d.pop(s[l])
            l+=1

        print(d)
        max_len = max(max_len, r-l+1)
    return max_len

s = "ccaabbb"
k = 2
# print(long_substring_atmost_k_chars(s, k))

# Longest Substring Without Repeating Characters
def long_substring_no_repeat(s):
    l, max_len = 0, 0
    distinct_elements = set()

    for r in range(len(s)):
        print(l, r)

        while s[r] in distinct_elements:
            distinct_elements.remove(s[l])
            l+=1

        distinct_elements.add(s[r])
        max_len = max(max_len, r-l+1)
    return max_len
        
# s = "abcabcbb"
# print(long_substring_no_repeat(s))


def long_substring_with_repeat(s, k):
    l, max_len, max_freq = 0, 0, 0
    d = defaultdict(int)

    for r in range(len(s)):
        d[s[r]] += 1
        max_freq = max(max_freq, d[s[r]])

        while (r-l+1) - max_freq > k:
            d[s[l]] -= 1
            l += 1
        
        max_len = max(max_len, r-l+1)
    return max_len

s = "ABBABBA"
k=1
# print(long_substring_with_repeat(s, k))


def is_subsequence(s, t):
    l = 0
    for r in t:
        if l<len(s) and s[l] == r:
            l+=1

        if len(s) == l:
            return True

    return len(s) == l

s = "abc"
t = "achbged"
print(is_subsequence(s, t))