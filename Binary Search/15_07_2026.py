from typing import List
def findMedianSortedArrays_linear(nums1: List[int], nums2: List[int]) -> float:
    sorted_arr = sorted(arr1+arr2)
    # even length
    n = len(sorted_arr)
    if n % 2 == 0:
        mid_index = n//2
        return (sorted_arr[mid_index-1] + sorted_arr[mid_index])/2
    return sorted_arr[n//2]


def findMedianSortedArrays_BS(nums1: List[int], nums2: List[int]) -> float:

    A, B = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
    
    total_length = len(nums1) + len(nums2)
    half = total_length // 2

    l, r = 0, len(A) - 1

    while True:
        i = (l+r)//2
        j = half - i - 2

        Aleft = A[i] if i >=0 else float('-inf')
        Aright = A[i+1] if i+1 < len(A) else float('inf')
        Bleft = B[j] if j >=0 else float('-inf')
        Bright = B[j+1] if j+1 < len(B) else float('inf')

        if Aleft <= Bright and Bleft <= Aright:
            if total_length%2:
                return min(Aright, Bright)
            return (max(Aleft,Bleft) + min(Aright, Bright))/2
            
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1

arr1 = [1,2,3,4,5]
arr2 = [1,2,3,4,5,6,7,8]

arr1=[1,3]
arr2=[2,7]
print(findMedianSortedArrays_linear(arr1, arr2))
print(findMedianSortedArrays_BS(arr1, arr2))