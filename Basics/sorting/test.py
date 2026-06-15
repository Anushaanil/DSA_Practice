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

selection_sort([7,2,4,6,1,9])