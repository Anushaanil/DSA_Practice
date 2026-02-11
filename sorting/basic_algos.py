'''
 # @ Create Time: 2025-11-15 22:16:25
 # @ Modified time: 2025-11-17 00:37:38
 '''


def bubble_sort(arr):
    """
    Gossiping Neighbors |
    Keep swapping adjacent ones

    *** Algorithm ***
    Repeat n-1 times:
    Go left to right:
        If neighbor on left > neighbor on right → swap

    """
    print(arr)
    n = len(arr)
    for pass_num in range(n-1):
        for i in range(1, n-pass_num):
            print(arr[i-1], '-----', arr[i])

            if arr[i-1] > arr[i]:
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

def quick_sort(arr):
    
    return arr

if __name__ == "__main__":
    test = [5, 3, 8, 1, 2]
    # print(bubble_sort(test))
    # print(selection_sort(test))
    print(insertion_sort(test))
