def isBadVersion(mid, bad=4):
     return mid >= bad
     
def firstBadVersion(n):
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

nums = [11,15,20,23]
print(min_in_rotated_sorted_array(nums))