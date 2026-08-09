# without stack
def next_taller_person(n, h):
    res = 0
    for i in range(1, n):
        if h[i] > h[i-1]:
            res+=1
        else:
            cur_ind = i
            while cur_ind < n and h[cur_ind] < h[i-1]:
                cur_ind+=1
            
            if cur_ind < n-1:
                res+=cur_ind-(i-1)
    return res

def next_taller_person_stack_sol(n,h):
    stack = []
    res = 0

    for i in range(n):
        while stack and h[i] > h[stack[-1]]:
            res += i - stack[-1]
            stack.pop()
        
        stack.append(i)
    return res


n = 6
h = [165, 175, 170, 185, 168, 172]

# print(next_taller_person(n, h))
print(next_taller_person_stack_sol(n, h))