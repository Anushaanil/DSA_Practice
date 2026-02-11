'''
👉 LEVEL 4: Loop + shifting logic (insertion-sort style)
(8) Insert a number into a sorted array at correct position

This is exactly insertion sort but simpler.

(9) Shift all elements right by 1

(Practice shifting, not swapping.)

(10) Reverse a string manually (no slicing)

You’ll learn:

two pointers

moving inward

swapping

stopping when they meet
'''

# LEVEL 1: Basic loop shaping
def loop_1():
# Print all numbers from 10 to 1
# Direction: backward
# Walker: number
# Stop: when reaches 1
    print('inside loop 1')
    for number in range(10, 0, -1):
        print(number, end=' ')
    
    print()
    number = 10
    while number>=1:
        print(number, end=' ')
        number-=1
    return

def loop_2():
# Print every second number from 0 to 20
# (0, 2, 4, 6…but using a loop, not range step)
# Ask:
# What am I repeating? → printing
# What changes? → +2
# When stop? → >20
    print()
    print('inside loop 2')
    for number in range(0, 21):
        if number%2 == 0:
            print(number, end=' ')

    print()
    number = 0
    while number<=20:
        print(number, end=' ')
        number+=2
    return

def loop_3(arr):

# (3) Find count of even numbers in an array
# Practice:
# Walker → current_index
# Stop → when index reaches len(arr)
    print()
    print('inside loop 3')
    c = 0
    for current_index in range(len(arr)):
        # print(current_index)
        if arr[current_index]%2 == 0:
            c+=1
    print(c)

    return

# LEVEL 2: Thinking in reverse loops
def loop_4(arr):
# (4) Print an array backwards
# (You’ll practice moving the walker left)
    print()
    print('inside loop 4')

    n = len(arr)
    for current_index in range(n):
        # print(current_index)
        print(arr[n-current_index-1], end=' ')
    
    print()
    for current_index in range(n-1, -1, -1):
        print(arr[current_index], end=' ')

    print()
    current_index = n-1
    while current_index >=0:
        print(arr[current_index], end=' ')
        current_index-=1

    return

def loop_5(arr):
# (5) Find first number > 10, but scanning from the end
# This is insertion-sort-style thinking.
    print()
    print('inside loop 5')
    n = len(arr)
    current_index = n-1
    while current_index>=0:
        if arr[current_index]>10:
            print(arr[current_index])
            break
        current_index-=1

    return

# LEVEL 3: Loop + condition shaping
def loop_6(arr):
# (6) Move all zeros to the end (in-place, single pass)
# You must design: walker, filler position, when they move
    # if position of elements matter
    # for i in range(len(arr)):
    #     j = i
    #     current_val = arr[i]
    #     print('j', j, '  ',  'ele at arr[i]', current_val)
    #     if current_val == 0:
    #         while j < len(arr)-1:
    #             arr[j], arr[j+1] = arr[j+1], arr[j]
    #             j+=1
    #             print('arr after', arr)
    # print('arr final', arr)

    # if position of elements doesn't matter
    write_pos = 0   # where the next non-zero element should go

    for read_pos in range(len(arr)):
        current_val = arr[read_pos]

        if current_val != 0:
            arr[write_pos] = current_val
            write_pos += 1

    # Fill remaining with zeros
    while write_pos < len(arr):
        arr[write_pos] = 0
        write_pos += 1

    print('arr final', arr)

    return

def loop_7(arr):

# (7) Count how many pairs of numbers add to 10
# (This builds nested-loop intuition.)
    return
    
if __name__ == "__main__":
    
    # loop_1()
    # loop_2()
    # loop_3([1,2,3,4,8,12,9,10])
    # loop_4([1,2,3,4,8,12,9,10])
    # loop_5([1,2,3,14,8,12,9,10])
    loop_6([1,0,3,14,0,12,0,10])
    # loop_7([1,2,3,14,8,12,9,10])
