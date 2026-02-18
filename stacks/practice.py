'''
 # @ Create Time: 2026-02-17 21:45:14
 # @ Modified time: 2026-02-19 00:58:34
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
arr = [73,74,75,71,69,72,76,73]
res = daily_temp(arr)
print(res)