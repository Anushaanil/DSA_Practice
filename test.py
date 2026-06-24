from typing import List

def selection_sort(arr):
    # find smallest and move it to the left
    n = len(arr)
    
    for pass_num in range(n-1):
        smallest = pass_num
        # smallest = pass_num
        for j in range(pass_num, n):
            if arr[smallest] > arr[j]:
                smallest = j
        arr[smallest], arr[pass_num] = arr[pass_num], arr[smallest]
    print(arr)

# selection_sort([7,2,4,6,1,9])


def bubble_sort(arr):
    flag = True
    while flag:
        flag = False
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                flag = True
                arr[i-1], arr[i] = arr[i], arr[i-1]
    return arr


# print(bubble_sort([7,2,4,6,1,9]))

def insertion_sort(arr):
    # compare btn sorted, unsorted parts of array
    # use i for comparing with new value, j for swapping till the left side of array is sorted
    i = 1
    j = 1

    while i < len(arr):
        while j > 0:
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j-=1
            else:
                break
        i+=1
        j=i
    return arr

# print(insertion_sort([7,2,4,6,1,9]))

def find_1st_occurence(arr, target):
    
    '''
    my initial solution

        while l < r:
            m = (l+r)//2

            if arr[m] == target:
                r = m
                while r>0 and arr[r] == arr[r-1]:
                    r-=1

            elif arr[m] < target:
                l = m+1
            else:
                r = m

        return r if arr[r] == target else -1
    '''
    l = 0
    r = len(arr) - 1

    while l < r:
        m = (l+r)//2
        if arr[m] >= target:
            r = m
        else:
            l = m + 1
    return l if arr[l] == target else -1


nums = [3,5,6,7,7,7,8]
target = 7

# print(find_1st_occurence(nums, target))

def find_last_occurence(arr, target):
    l = 0
    r = len(arr) -1

    while l < r:
        m = (l+r+1)//2 

        if arr[m] <= target:
            l = m
        else:
            r = m-1

    return r if arr[r] == target else -1

nums = [3,5,6,7,7,7,8]
target = 7
# print(find_last_occurence(nums, target))

def search_in_rotated_sorted_array(arr, target):
    l = 0
    r = len(arr) - 1

    while l <= r:
        m = (l+r)//2
        
        if arr[m] == target:
            return m
        
        # left side sorted
        if arr[l] <= arr[m]:
            if arr[l] <= target <= arr[m]:
                r = m - 1
            else:
                l = m + 1

        # right side is sorted
        else:
            if arr[m] <= target <= arr[r]:
                l = m + 1
            else:
                r = m - 1

    return l

nums = [6,7,1,2,3,4,5]
target = 3
# print(search_in_rotated_sorted_array(nums, target))

def find_min_rotated_array(arr):
    l = 0
    r = len(arr) - 1
    ans = float('inf')

    while l <=r:
        m = (l+r)//2

        # optimization: search space is already sorted
        # then always arr[low] will be the ans in that search space

        if arr[l] <= arr[r]:
            ans = min(ans, arr[l])
            break

        if arr[l] <= arr[m]:
            ans = min(ans, arr[l])
            l = m + 1
        else:
            ans = min(ans, arr[m])
            r = m - 1

    return ans

nums = [1,2,3,4,5, 6,7]
# print(find_min_rotated_array(nums))

def findPeakElement(nums):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l+r)//2

        if nums[mid] >= nums[mid+1]:
            r = mid - 1
        else:
            l = mid + 1
    return nums[l]

nums = [1,2,3,4,5,3,1,0]
# print(findPeakElement(nums))

matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=60

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    for row in range(len(matrix)):
        l = 0
        r = len(matrix[0]) - 1

        print(row, l, r)

        if matrix[row][l] <= target <= matrix[row][r]:
            while l <=r:
                m = (l+r)//2
                if matrix[row][m] == target:
                    print(row, m)

                    return True
                elif matrix[row][m] < target:
                    l = m + 1
                else:
                    r = m - 1
    return False

# print(searchMatrix(matrix, target))

import math

def minEatingSpeed(piles: List[int], h: int) -> int:
    l = 1
    r = max(piles)

    # print(l, r)

    while l <r:
        m = (l+r)//2

        

        eating_speed = sum(math.ceil(i/m) for i in piles)
        # print(eating_speed)

        if eating_speed <= h:
            r = m
        else:
            l = m + 1

    for i in piles:
        print(i, math.ceil(i/m))

    return r

piles = [25,10,23,4]
h = 9
print(minEatingSpeed(piles, h))