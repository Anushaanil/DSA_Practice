"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

"""

from ast import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap - O(n)
        num_map = {}
        for i, num in enumerate(nums):
            complement = target-num
            if complement in num_map:
                return [num_map[complement],i]
            num_map[num] = i

        # 2 pointer with sorting
        indexed_nums = [(i, num) for i, num in enumerate(nums)]
        indexed_nums.sort(key=lambda x:x[1]) # sort by value only

        left = 0
        right = len(indexed_nums)-1

        while left<right:
            sum_of_2 = indexed_nums[left][1] + indexed_nums[right][1]
            if sum_of_2 == target:
                return [indexed_nums[left][0], indexed_nums[right][0]]
            elif sum_of_2 < target:
                left+=1
            else:
                right-=1
