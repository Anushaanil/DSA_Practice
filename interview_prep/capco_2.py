nums = [2, 6, 5, -3, 10, 0, -4, 1]

# sort in ascending order
# [2, 5, -3, 6, 0, -4, 1, 10]

# [2, -3, 5, 0, -4, 1, 6, 10]

# [-3, 2, 0, -4, 1, 5, 6, 10]

# [-3, 0, -4, 1, 2, 5, 6, 10]

# [-3, -4, 0, 1, 2, 5, 6, 10]

# [-4, -3, 0, 1, 2, 5, 6, 10]

def sort_nums(nums):
    start = 0
    end = 1
    
    while end < len(nums):
        if nums[start] > nums[end]:
            # swapping
            nums[start], nums[end] = nums[end], nums[start]
            
        start+=1
        end+=1
        
    return nums

print(sort_nums(nums))
            