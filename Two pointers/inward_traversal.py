'''
Pair Sum - Sorted
Easy
Given an array of integers sorted in ascending order and a target value, return the indexes of any pair of numbers in the array that sum to the target. The order of the indexes in the result doesn't matter. If no pair is found, return an empty array.

Example 1:
Input: nums = [-5, -2, 3, 4, 6], target = 7
Output: [2, 3]
Explanation: nums[2] + nums[3] = 3 + 4 = 7

Example 2:
Input: nums = [1, 1, 1], target = 2
Output: [0, 1]
Explanation: other valid outputs could be [1, 0], [0, 2], [2, 0], [1, 2] or [2, 1].

'''
from typing import List

def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    # Brute force
    # if len(nums) < 2:
    #     return []

    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i]+nums[j] == target:
    #             return [i, j]
    # return []

    # 2 pointers - Inward Traversal
    left, right = 0, len(nums)-1
    while left < right:
        if nums[left] + nums[right] == target:
            return [left, right]
        elif nums[left] + nums[right] < target:
            left+=1
        else:
            right-=1

    return []


'''
Valid Palindrome
Easy
Topics
Company Tags
Hints
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
'''

def isPalindrome(s: str) -> bool:
    # Python way
    # a=""
    # for i in s:
    #     if i.isalnum():
    #         a+=i.lower()
    # return a==a[::-1]

    # 2 pointers
    left = 0
    right = len(s) -1

    while left < right:
        while left< right and not s[left].isalnum():
            left+=1
            
        while left < right and not s[right].isalnum():
            right-=1

        if s[left].lower() != s[right].lower():
            return False

        left+=1
        right-=1

    return True


def threeSum(nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            # Optimization: as we sort the elements, 
            # elements > 0 and it's after elements could never produce 0
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1
            target = -(nums[i])

            while left < right:
                sum_ele = nums[left] + nums[right]

                if sum_ele == target:
                    
                    triplets.append([nums[i], nums[left], nums[right]])
                    
                    left+=1
                    
                    while left < right and nums[left] == nums[left-1]:
                        left+=1 # To avoid duplicate '[l, r]' pairs, skip 'l' if it’s the same as the # previous number.

                elif sum_ele > target:
                    right-=1

                else:
                    left+=1

        return triplets

nums=[-1,0,1,2,-1,-4] #[-4,-1,-1,0,1,2]
# print(threeSum(nums))
