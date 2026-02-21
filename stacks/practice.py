'''
 # @ Create Time: 2026-02-17 21:45:14
 # @ Modified time: 2026-02-22 00:18:51
 '''


def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    return reversed_str

# s = "hello"
# result = reverse_string(s)
# print(result)

def valid_paranthesis(s):
    stack = []

    paranthesis = {
        ")":"(",
        "}":"{",
        "]":"["
    }

    for char in s:
        print(char)
        if char not in paranthesis:
            stack.append(char)
        else:
            if not stack:
                return False
            
            top = stack.pop()
            if top != paranthesis[char]:
                return False
            
    return len(stack) == 0

# s = "({}(])"
# res = valid_paranthesis(s)
# print(res)

def remove_adjacent_duplicate(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

        # My unoptimized 1st version
        # if not stack:
        #     stack.append(char)
        #     continue
            
        # top = stack[-1]
        # if char == top:
        #     stack.pop()
        # else:
        #     stack.append(char)
    return ''.join(stack)

# s = "aaaa"
# res = remove_adjacent_duplicate(s)
# print(res)

def reverse_polish_notation(input_stack):
    operators = {"+", "-", "*", "/"}
    output_stack = []
    for char in input_stack:
        if char in operators:
            a = output_stack.pop()
            b = output_stack.pop()
            
            if char == "+":
                output_stack.append(a+b)
            elif char == "-":
                output_stack.append(a-b)
            elif char == "*":
                output_stack.append(a*b)
            elif char == "/":
                output_stack.append(int(a/b))
        else:
            output_stack.append(int(char))
                
    return output_stack[-1]

# input_stack = ["2","1","+","3","*"]
# res = reverse_polish_notation(input_stack)
# print(res)

def next_greater_element(arr):
    # Brute force solution of mine
    # stack = []

    # for i in range(len(arr)):
    #     max_element = arr[i]

    #     for j in range(i+1, len(arr)):
    #         if arr[j] > max_element:
    #             max_element = arr[j]
    #             stack.append(max_element)
    #             break
            
    #     if max_element == arr[i]:
    #         stack.append(-1)
    # return stack

    stack = []
    result = [-1] * len(arr)
    
    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            index = stack.pop()
            result[index] = arr[i]
        stack.append(i)
    return result

# arr = [2,1,2,4,3]
# res = next_greater_element(arr)
# print(res)

def next_smaller_element(arr):
    stack = []
    result = [-1]*len(arr)

    for i in range(len(arr)):
        while stack and arr[i] < arr[stack[-1]]:
            index = stack.pop()
            result[index] = arr[i]
        stack.append(i)
    return result
# arr = [4,8,5,2,25]
# res = next_smaller_element(arr)
# print(res)

def daily_temp(arr):
    stack = []
    result = [0]*len(arr)

    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            index = stack.pop()
            result[index] = i - index
        stack.append(i)
    return result
# arr = [73,74,75,71,69,72,76,73]
# res = daily_temp(arr)
# print(res)

def next_greater_element_I(nums1, nums2):
    # --- Brute force solution ---
    # res = [-1]*len(nums1)
    # stack = []
    # d = {}

    # for i in range(len(nums1)):
    #     for j in range(len(nums2)):
    #         if nums1[i] == nums2[j]:
    #             d[i] = j

    # for i in d:
    #     for k in range(d[i]+1, len(nums2)):
    #         if nums2[k] > nums1[i]:
    #             res[i] = nums2[k]
    #             break
    
    # return res

    # --- Ideal solution ---
    # stack = []
    # res = [-1]*len(nums1)
    # mapping = {}

    # for i in range(len(nums2)):
    #     while stack and nums2[i] > stack[-1]:
    #         val = stack.pop()
    #         mapping[val] = nums2[i]
    #     stack.append(nums2[i])
    
    # for i, num in enumerate(nums1):
    #     if num in mapping:
    #         res[i] = mapping[num]
    # return res

    # --- Optimized Ideal solution ---
    mapping = {}
    stack = []
    for num in nums2:
        while stack and stack[-1]< num:
            mapping[stack.pop()] = num
        stack.append(num)
    return [mapping.get(num, -1) for num in nums1]

nums1 = [4,1, 2]
nums2 = [1,3,4,2]
# print(next_greater_element_I(nums1, nums2))

def largest_rectangle_histogram(heights):
    ma_area = 0
    stack = []
    pse = 0
    nse = 0
    
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            element = stack.pop()
            nse = i
            pse = -1 if not stack else stack[-1]
            ma_area = max(ma_area, heights[element]*(nse-pse-1))
        stack.append(i)
    
    while stack:
        nse = len(heights)
        element = stack.pop()
        pse = -1 if not stack else stack[-1]
        ma_area = max(ma_area, heights[element]*(nse-pse-1))
 
    return ma_area

heights = [3,2,10,11,5,10,6,3]
# print(largest_rectangle_histogram(heights))

def min_stack(arr):
    # logic - 
    # use 2 stacks 1 for storing all main elements another to keep track of min 
    # and return it's [-1] from min stack also pop whenver main stack ele is popped
    # so that we always have a min at that point.
    return