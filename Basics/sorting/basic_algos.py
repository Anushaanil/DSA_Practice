'''
 # @ Create Time: 2025-11-15 22:16:25
 # @ Modified time: 2026-06-21 01:47:19
 '''


def bubble_sort(arr):
    """
    Gossiping Neighbors |
    Keep swapping adjacent ones

    *** Algorithm ***
    Repeat n-1 times:
    Go left to right:
        If neighbor on left > neighbor on right → swap
    
    What Bubble Sort guarantees after each pass?

    After Pass 1:

    [3, 5, 4, 2, 8]

    The largest element (8) has bubbled to the end.
    After each pass, only the right side becomes fixed.

    The left side is still messy.

    So every pass must begin from the start:

    for i in range(1, ...)

    not from:

    for i in range(pass_num, ...)

    because nothing guarantees the left side is sorted.

    Time - O(n^2)
    Space - O(1)

    """
    print(arr)
    n = len(arr)
    for pass_num in range(n-1):
        for i in range(1, n-pass_num):
        # for i in range(pass_num, n):
            print(arr[i-1], '-----', arr[i])

            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
    return arr

# using a flag
def bubble_sort_flag(arr):
    n = len(arr)
    flag = True

    while flag:
        flag = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                flag = True
                arr[i-1], arr[i] = arr[i], arr[i-1]
    return arr

def selection_sort(arr):
    """
    Strict Teacher | 
    Find smallest → put in front

    *** Algorithm ***
    Repeat n-1 times:
    Go left to right:
        Assume 1st element of the pass to be smallest
        Compare it with elements in pass to find smallest in the pass
        once found swap it with 1st element of pass

    """
    print(arr)
    n = len(arr)
    
    for pass_num in range(n-1):
        smallest = pass_num

        for i in range(pass_num, n):
            if arr[smallest] > arr[i]:
                smallest = i

        arr[smallest], arr[pass_num] = arr[pass_num], arr[smallest]
        print('final', arr)

    return arr

'''
Interview Question

    Can you tell me why Selection Sort can start from:

    for i in range(pass_num, n):

    but Bubble Sort cannot?

    
The key difference

Selection Sort says:

Left side is sorted.
Right side is unsorted.

Bubble Sort says:

Left side is unsorted.
Right side is sorted.

Therefore:

Selection Sort

Shrink from the left:

for i in range(pass_num, n)
Bubble Sort

Shrink from the right:

for i in range(1, n-pass_num)

'''

def insertion_sort(arr):
    """
    Diary Student | Insert one at a time

    *** Algorithm ***
    Divide the section into 2 sorted and unsorted
    add 1 st element to sorted, compare it with 1st 
    element of unsorted and add it to its position in sorted.
    """
    
    print(arr)

    for unsorted_index in range(1, len(arr)):
        prev_sorted_index = unsorted_index-1
        current_val = arr[unsorted_index]

        print(arr[prev_sorted_index], current_val)

        while prev_sorted_index>=0 and current_val < arr[prev_sorted_index]:
            arr[prev_sorted_index+1] = arr[prev_sorted_index]
            prev_sorted_index-=1

        arr[prev_sorted_index+1] = current_val
        print(arr)

    return arr

def merge_sort(arr):
    '''
    Idea
        Split
        Split
        Split
        Until size = 1

        Then merge back

    Example:

        [8,3,5,4]

            [8,3,5,4]
            /       \
        [8,3]     [5,4]
        /  \      /  \
        [8] [3]   [5] [4]

        Merge:
        [3,8]
        [4,5]

        Merge:
        [3,4,5,8]
        Invariant

        When merging:

        Left half is sorted
        Right half is sorted

        You combine them into one sorted array.

    Complexity
        Metric	Value
        Time	O(n log n)
        Space	O(n)
        Stable	Yes
        Memory Trick

    Break family apart → reunite in sorted order.
    '''
    
    # def merge(low, mid, high, arr):
    def merge(low, mid, high, arr):

        left = low
        right = mid + 1

        temp = []

        while left <= mid and right <= high:

            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1

            else:
                temp.append(arr[right])
                right += 1

        print(temp)
        
        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(low, high + 1):
            arr[i] = temp[i - low]
    
    def merge_sort_after_split(low, high, arr):
        
        # there is only 1 element
        if low >= high:
            return
        
        mid = (low+high)//2
        
        merge_sort_after_split(low, mid, arr)
        merge_sort_after_split(mid+1, high, arr)
        merge(low, mid, high, arr)
    
    merge_sort_after_split(0, len(arr)-1, arr)
    return arr

def quick_sort(left, right, arr):
    """
    Pick a pivot (generally the last element considered)

    Move:

    Smaller elements → left side
    Larger elements → right side

    Then recursively repeat for left and right halves.
    
    Average:

    O(n log n)

    Worst case:

    O(n²)
    """
    
    def partition(left, right, arr):
        pivot = arr[right] # used to compare
        i = left # left boundary of smaller elements
        
        for j in range(left, right):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i+=1
                
        arr[i], arr[right] = arr[right], arr[i]
        
        return i
            

    if left >= right:
        return
    
    pivot_index = partition(left, right, arr)

    quick_sort(left, pivot_index-1, arr)
    quick_sort(pivot_index+1, right, arr)

    return arr
    

if __name__ == "__main__":
    # test = [5, 3, 8, 1, 2]
    test = [8,3,5,4,7]
    # print(bubble_sort(test))
    # print(selection_sort(test))
    # print(insertion_sort(test))
    # print(merge_sort(test))
    print(quick_sort(0, len(test)-1, test))
