# Exercise Set A — Pointer Movement Only (No Conditions)
# Exercise 1: Reverse an array

def reverse_array(arr):
    l = 0 
    r = len(arr)-1

    while l<r:
        arr[l], arr[r] = arr[r], arr[l]
        l+=1
        r-=1
    print(arr)
    return arr

# arr = [1,2,3,7, 4,5]
# reverse_array(arr)

# Exercise 2: Reverse only vowels in a string

def reverse_vowels_in_string(string):
    l = 0
    r = len(string)-1
    arr = list(string) # using array as string is immutable in python
    vowels = set('aeiouAEIOU') # using set as it takes O(1) for lookup

    print(arr)

    while l<r:
        if arr[l] in vowels and arr[r] in vowels:
            arr[l], arr[r] = arr[r], arr[l]
            l+=1
            r-=1

        elif arr[l] not in vowels:
            l+=1

        else:
            r-=1
        
    print(''.join(arr))
    return ''.join(arr)

# string = "helilorap"
# reverse_vowels_in_string(string)


# Exercise Set B — Decision-Based Movement (Core Two-Pointer Thinking)
# Exercise 3: Check if string is palindrome
def is_palindrome(s):
    l, r = 0, len(s)-1
    while l<r:
        if s[l] == s[r]:
            l+=1
            r-=1
        else:
            return False
    return True

# s = "radecar"
# print(is_palindrome(s))


# Exercise 4: Palindrome ignoring non-alphanumerics
def is_palindrome_non_alphanumeric(s):
    l, r = 0, len(s)-1

    while l<r:
        print(l, ' -> ', r)
        print(s[l], " == ", s[r])

        if s[l].lower() == s[r].lower():
            l+=1
            r-=1
        elif not s[l].isalnum():
            l+=1
        elif not s[r].isalnum():
            r-=1
        else:
            return False

    return True

# s = "A man, a plan, a canal: Panama"
# print(is_palindrome_non_alphanumeric(s))


# Exercise Set C — Same Direction (Slow–Fast)

# Exercise 5: Remove duplicates (sorted array)
def remove_duplicates(arr):
    s, f = 0, 1
    while f < len(arr):
        if arr[s] == arr[f]:
            f+=1
        else:
            s+=1
            arr[s] = arr[f]
            f+=1
    print(arr[:s+1])
    return arr[:s+1]

# arr = [1,1,2,2,3,4,5]
# remove_duplicates(arr)

# Exercise 6: Move zeroes to end
# using while loop -> I tried this
# def move_zeros_to_end(arr):
#     s, f = 0, 1
#     while f < len(arr):
#         if arr[s] == 0 and arr[f] == 0:
#             f+=1
#         elif arr[s] == 0 and arr[f] != 0:
#             arr[s], arr[f] = arr[f], arr[s]
#             s+=1
#             f+=1
#         else:
#             s+=1
#             f+=1
#     print(arr)
#     return arr

# simple logic using for loop
def move_zeros_to_end(arr):
    s = 0
    for f in range(len(arr)):
        print('s -> ', s, ' f', f)
        print('as -> ' , arr[s], 'af -> ', arr[f])
        if arr[f]!=0:
            arr[s], arr[f] = arr[f], arr[s]
            s+=1
    print(arr)
    return arr

arr = [1,2,3,0,1,2,5,0,3]
# move_zeros_to_end(arr)

# Exercise Set D — Window Intuition (Very Light)
# Exercise 7: Is s a subsequence of t?
def is_sub_sequence(s, t):
    slow = 0
    for fast in range(len(t)):
        if slow == len(s):
            return True
        
        if s[slow] == t[fast]:
            slow += 1

    return slow == len(s)

s = "xyz"
t = "ahbgdc"
# print(is_sub_sequence(s,t))


def maxArea(height):
    l, r = 0, len(height)-1
    max_area = 0

    while l<r:
        max_area = max(max_area, min(height[l], height[r]) * (r-l))
        if height[l] <= height[r]:
            l+=1
        else:
            r-=1
    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))