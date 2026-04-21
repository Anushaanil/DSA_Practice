'''
Next Lexicographical Sequence
Medium
Given a string of lowercase English letters, rearrange the characters to form a new string representing the next immediate sequence in lexicographical (alphabetical) order. If the given string is already last in lexicographical order among all possible arrangements, return the arrangement that's first in lexicographical order.

Example 1:
Input: s = 'abcd'
Output: 'abdc'
Explanation: "abdc" is the next sequence in lexicographical order after rearranging "abcd".

Example 2:
Input: s = 'dcba'
Output: 'abcd'

'''

def next_lexicographical_sequence(s: str) -> str:
    letters = list(s)
    n = len(letters)
    pivot = n - 2 # start comparing last 2 elements

    while pivot>=0 and letters[pivot] >= letters[pivot+1]:
        # print(letters[pivot], letters[pivot+1])
        pivot-=1
    
    if pivot<0:
        return ''.join(letters[::-1])
    
    # find right most swap
    right_most_successor = n-1

    while letters[right_most_successor] <= letters[pivot]:
        right_most_successor-=1

    # swap them
    letters[pivot], letters[right_most_successor] = letters[right_most_successor], letters[pivot]

    if n - pivot > 1:
        # reverse the suffix
        letters[pivot+1:] = letters[pivot+1:][::-1]

    return ''.join(letters)


# print(next_lexicographical_sequence('dcba'))


def next_permutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    pivot = n-2

    # finding the right pivot
    while pivot>=0 and nums[pivot] >= nums[pivot+1]:
        pivot-=1

    # no pivot found
    if pivot == -1:
        nums.reverse()
        return

    # find the righmost successor to swap with
    right_most_successor = n-1
    while nums[right_most_successor] <= nums[pivot]:
        right_most_successor-=1

    # swap
    nums[pivot], nums[right_most_successor] = nums[right_most_successor], nums[pivot]

    # reverse suffix
    nums[pivot+1:] = nums[pivot+1:][::-1]

print(next_permutation([3,2,1]))