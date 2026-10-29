def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    row_size = len(matrix)
    col_size = len(matrix[0])

    left = 0
    right = row_size * col_size - 1

    while left <= right:
        mid = (left + right) // 2
        # formula to find the row and col for given position
        row = mid // col_size
        col = mid % col_size

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False 

    # This approach does b.s row wise but 
    # they need it to be applied on entire matrix
    # for row in range(row_size):
    #     l = 0
    #     r = col_size-1
    #     while l < r:
    #         m = (l+r)//2
    #         if matrix[row][m] == target:
    #             return True
    #         elif matrix[row][m] < target:
    #             l = m + 1
    #         else:
    #             r = m - 1
    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 36
# Output: true
print(searchMatrix(matrix, target))