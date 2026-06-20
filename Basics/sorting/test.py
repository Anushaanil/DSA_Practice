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

print(insertion_sort([7,2,4,6,1,9]))

