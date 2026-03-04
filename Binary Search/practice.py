def binary_search(nums, target: int) -> int:
        left = 0
        right = len(nums)-1

        while left<=right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                left = mid+1
            else:
                right = mid-1

        return -1

nums = [1,2,3,4,5]
target = 3
# print(binary_search(nums, target))

def searchInsert(nums, target):
    left = 0
    right = len(nums)-1

    while left<=right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid]<target:
            left = mid+1
            
        else:
            right = mid-1

    return left

nums = [1,2,4,5,6]
target = 3
# print(searchInsert(nums, target))


def find_target_in_infinite_array(arr, target):
    # as arr can be infinite we donno the len, so we need to start from starting indices
    # use bottom up approach by doubling the search len and if target is found in the given 
    # range then apply binary search
    s = 0
    e = 1

    while target > arr[e]:
        temp = e + 1
        e = e + (e-s+1) * 2
        s = temp

    while s<=e:
        m = (s+e)//2
        print('here', m, arr[m])

        if arr[m] == target:
            return m
        elif arr[m] < target:
            s = m+1
        else:
            e = m-1

    return -1

arr = [2,3,4,5,6,7,8,10,11,12,15,20,23,50]
target = 15
# print(find_target_in_infinite_array(arr, target))


def nextGreatestLetter(letters, target):
    l = 0
    r = len(letters)-1

    while l<r:
        mid = (l+r)//2
        if letters[mid] > target:
            r = mid
        else:
            l = mid+1

    return letters[l] if letters[l]>target else letters[0]

letters = ["x","x","f","j"]
target = "z"
# print(nextGreatestLetter(letters, target))

     
def firstBadVersion(n):
    def isBadVersion(mid, bad=4):
        return mid >= bad
    
    l = 1
    r = n

    while l<r:
        mid = (l+r)//2
        print(l,r)

        if isBadVersion(mid):
            r = mid
        else:
                l = mid+1
            
    return l

# print(firstBadVersion(5))


class Solution:
    def find_1st_occurence(self, l, r, nums, target):
        # find 1st occurence
        # found = False
        while l<r:
            mid = (l+r)//2
            print(l, r, mid)
            if nums[mid] >= target:
                r = mid
            else:
                l = mid+1

        return l if nums[l] == target else -1
    
    def find_last_occurence(self, l, r, nums, target):
        # find last occurence
        if l == -1:
            return -1
        
        while l<r:
            mid = (l+r+1)//2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid-1

        return r if nums[r] == target else -1
    
    # 1st and last position of ele in array
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        
        first_occurence = self.find_1st_occurence(0, len(nums)-1, nums, target)
        last_occurence = self.find_last_occurence(first_occurence, len(nums)-1, nums, target)
        return [first_occurence, last_occurence]
    
# s = Solution()
# nums = [5, 6, 7, 7, 7, 8]
# target = 6
# print(s.searchRange(nums, target))


def search_in_rotated_sorted_array(nums, target):
    l = 0
    r = len(nums)-1
    # another approach find pivot i.e peak element
    # search in left side of peak
    # if not found then search in right side of peak
    while l<=r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[l]<=nums[mid]:
            if nums[l]<=target<nums[mid]:
                r=mid-1
            else:
                l=mid+1
        else:
            if nums[mid]<target<=nums[r]:
                l=mid+1
            else:
                r=mid-1

    return -1

# nums = [6,7,1,2,3,4,5]
# target = 6
# print(search_in_rotated_sorted_array(nums, target))


def min_in_rotated_sorted_array(nums):
    l = 0
    r = len(nums)-1

    while l<r:
        mid = (l+r)//2
        if nums[mid]<=nums[r]:
            r = mid
        else:
            l = mid+1

    return nums[l]

# nums = [11,15,20,23]
# print(min_in_rotated_sorted_array(nums))


def findPeakElement(nums) -> int:
        l = 0
        r = len(nums)-1

        while l<r:
            mid = (l+r)//2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid+1

        return l

nums = [1,2,3,4,5,3,1,0]
# print(findPeakElement(nums))


def mySqrt(x: int) -> int:
    l = 1
    r = x

    if x == 0:
        return 0

    while l<r:
        mid = (l+r+1)//2
        if mid * mid <= x:
            l = mid
        else:
            r = mid-1

    return l

# print(mySqrt(8))


import math
def minEatingSpeed(piles, h):
    l = 1
    r = max(piles)

    while l < r:
        mid = (l+r)//2
        # math.ceil(i/k)
        total_hours = sum((i+mid-1)//mid for i in piles)
        if total_hours <= h:
            r = mid
        else:
            l = mid+1
    return l

# piles = [30,11,23,4,20]
# h = 6
# print(minEatingSpeed(piles, h))


def shipWithinDays(weights, days):
    l = max(weights)
    r = sum(weights)

    while l<r:
        mid = (l+r)//2
        total_days = 1
        total_weight = 0

        for weight in weights:
            if total_weight + weight <= mid:
                total_weight+=weight
            else:
                total_days+=1
                total_weight = weight

        if total_days <=days:
            r = mid
        else:
            l = mid+1
    return l
    
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
# print(shipWithinDays(weights, days))


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
   def __init__(self, arr, target):
       self.mountainArr = arr
       self.target = target

   def get(self, index: int) -> int:
       return self.mountainArr[index]
   
   def length(self) -> int:
       return len(self.mountainArr)

class Solution:
    def findPeak(self, mountainArr):
        l = 0
        r = mountainArr.length() - 1

        while l<r:
            m = (l+r)//2
            if mountainArr.get(m) >= mountainArr.get(m+1):
                r = m
            else:
                l = m + 1
        return l

    def binarySearch(self, mountainArr, l, r, target, ans, is_asc):
        while l<=r:
            m = (l+r)//2
            if mountainArr.get(m) == target:
                ans = m
                return ans
            
            if is_asc:
                if mountainArr.get(m) > target:
                    r = m - 1
                else:
                    l = m + 1
            else:
                print(mountainArr.get(m), target)
                if mountainArr.get(m) > target:
                    l = m + 1
                else:
                    r = m - 1
        return ans

    def findInMountainArray(self, target: int, mountainArr):
        # find peak
        peak = self.findPeak(mountainArr)
        print('peak', peak)

        # search in left side of the peak
        default_ans = -1
        ans = self.binarySearch(mountainArr, 0, peak, target, default_ans, True)
        print('left side ans', 0, peak, ans)
        if ans==-1:
            ans = self.binarySearch(mountainArr, peak+1, mountainArr.length()-1, target, default_ans, False)
            print('right side ans', peak+1, mountainArr.length()-1, ans)
        return ans

arr = [1,2,3,4,5,3,1,0]
target = 8
m = MountainArray(arr, target)
s = Solution()
# print(s.findInMountainArray(m.target, m))


def find_rotation_count_in_rotated_sorted_array(arr):
    l = 0
    r = len(arr)-1

    while l<r:
        m = (l+r)//2
        print(l, m, r)
        if arr[m] < arr[r]:
            r = m
        else:
            l = m+1
    return l

# count of rotations = index of min element
arr = [1,2,3,4,5,6]
print(find_rotation_count_in_rotated_sorted_array(arr))
