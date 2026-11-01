class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
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