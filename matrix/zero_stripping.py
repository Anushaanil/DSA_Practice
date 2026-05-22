def zero_stripping_app_1(matrix):
    """ This sol uses 2 extra sets to keep track of 
        rows and cols, use existing structure to save space
    """
    rows = set()
    cols = set()

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col]==0:
                rows.add(row)
                cols.add(col)
    
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row in rows or col in cols:
                matrix[row][col] = 0
    
    print(matrix)
    return matrix

def zero_stripping_app_2(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                matrix[0][col] = 0
                matrix[row][0] = 0
    
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[0][col]==0 or matrix[row][0]==0:
                matrix[row][col]=0

    print(matrix)

matrix = [
            [1, 2, 3, 4, 5],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 0]
        ]

matrix = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

# zero_stripping_app_1(matrix)
zero_stripping_app_2(matrix)