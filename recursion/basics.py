# 1. Print numbers from 1 to N
# print_numbers(5)

# 1
# 2
# 3
# 4
# 5

def print_numbers(n):
    if n == 0:
        return
    
    print_numbers(n-1)
    print(n)

# print_numbers(5)


# 2. Print numbers from N to 1
# print_numbers(5)

# 5
# 4
# 3
# 2
# 1

def print_numbers(n):
    if n == 0:
        return
    print(n)
    print_numbers(n-1)

# print_numbers(10)
    
# Sum of first N numbers
# sum(5)

# 15
    
def sum_of_numbers(n):
    if n==0:
        return 0
    
    return n + sum_of_numbers(n-1)

# print(sum_of_numbers(5))

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent-1)
# power(2,5)

# print(power(2,5))

# 6. Reverse a string recursively
# "hello"

# ↓

# "olleh"

def reverse_string(s):
    if len(s) == 0:
        return ''
    
    return s[-1] + reverse_string(s[0:-1])

# print(reverse_string("hello"))

# 7. Check palindrome recursively
# racecar

# ↓

# True

def is_palindrome(s):
    if len(s) == 0:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1]) 

# print(is_palindrome("racecar"))

# no slicing
def is_palindrome(s, i, n):
    if i >= (n//2):
        return True
    
    if s[i]!=s[n-i-1]:
        return False
    return is_palindrome(s, i+1, n)

s = "racear"
print(is_palindrome(s, 0, len(s)))

# 8. Count occurrences
# nums = [1,2,1,3,1]

# target = 1

# ↓

# 3
def count_occurence(nums, index, target):
    if index == len(nums):
        return 0
    
    if nums[index] == target:
        return 1 + count_occurence(nums, index+1, target)
    return count_occurence(nums, index+1, target)

nums = [1,2,1,3,1]
target = 1
# print(count_occurence(nums, 0, target))

# 9. Maximum element

# Without using

# max()


# 10. Sum of array

# Without loops.

# 11. Print names N times

def print_names(name, n):
    if n == 0: # if i > n
        return
    print(n, ' name is: ', name)
    # return print_names(name, i+1, n)
    return print_names(name, n-1)

# print_names('anusha', 5)

# 12. reverse array

def reverse_array(arr):
    if len(arr) == 0:
        return []
    
    return [arr[-1]] + reverse_array(arr[:-1])

# without slicing using 2 pointers
def reverse_array(arr, l, r):
    if l>r:
        return arr
    
    arr[l], arr[r] = arr[r], arr[l]
    return reverse_array(arr, l+1, r-1)

# only indices
def reverse_array(arr, i, n):
    if i>(n//2):
        return arr
    
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return reverse_array(arr, i+1, n)

arr = [1,2,3,5,6,7,10]
print(reverse_array(arr,0, len(arr)))