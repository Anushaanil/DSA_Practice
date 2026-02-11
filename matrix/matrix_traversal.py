'''
 # @ Create Time: 2025-07-20 10:53:53
 # @ Modified time: 2025-11-17 00:39:09
 '''


def all_elements_traversal(matrix):
    print('all_elements_traversal\n')
    for row in range(len(matrix)):
        for col in range(len(matrix[row])): # matrix[0] --> gives the len of the 1st row which is anyways same
            print('row', row, '---', 'col', col)
            print('value', matrix[row][col], '\n')

def row_wise_traversal(matrix):
    print('row_wise_traversal\n')
    for i, row in enumerate(matrix):
        print('row', i, '\n')
        for val in row:
            print('val', val,'\n')
        print('\n')

def reverse_row_wise_traversal(matrix):
    print('reverse_row_wise_traversal\n')
    for i, row in enumerate(matrix):
        print('row', i, row, '\n')
        
        for val in range(len(row)-1, -1, -1):
            print('val', row[val],'\n')
        print('\n')

def col_wise_traversal(matrix):
    print('col_wise_traversal\n')
    for col in range(len(matrix[0])):
        print('col', col, '\n')
        for row in range(len(matrix)):
            print('val', matrix[row][col],'\n')
        print('\n')

def top_left_bottom_right_diagonal_elements_traversal(matrix):
    print('top_left_bottom_right_diagonal_elements_traversal\n')
    from collections import defaultdict
    d = defaultdict(list)

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print('row', row, '---', 'col', col)
            d[row + col].append(matrix[row][col])
            
    print('value', d)
    output = []
    for key in sorted(d.keys()):
        diagonal_str = ', '.join(str(val) for val in d[key])
        output.append(diagonal_str)
    print(' -> '.join(output))

def top_right_bottom_left_diagonal_elements_traversal(matrix):
    print('top_right_bottom_left_diagonal_elements_traversal\n')
    from collections import defaultdict
    d = defaultdict(list)

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            # print('row', row, '---', 'col', col)
            d[row - col].append(matrix[row][col])
            
    # print('value', d)
    output = []
    for key in sorted(d.keys()):
       diagonal_str = ', '.join(str(val) for val in d[key])
       output.append(diagonal_str)
    
    print(' -> '.join(output))

def zigzag_traversal(matrix):
    print('zigzag traversal\n')
    for i, row in enumerate(matrix):
        print('row', i, row, '\n')
        if i%2 == 0:
            for val in range(len(row)):
                print('val', row[val],'\n')
        else:
            for val in range(len(row)-1, -1, -1):
                print('val', row[val],'\n')
        print('\n')

def spiral_traversal(matrix):
    print('spiral traversal\n')
    top = 0
    bottom = len(matrix)-1
    left = 0
    right = len(matrix[0])-1

    while top<=bottom and left<=right:
        for i in range(left, right+1):
            print(matrix[top][i])
        top+=1

        for i in range(top, bottom+1):
            print(matrix[i][right])
        right-=1

        if top <= bottom:
        # run bottom row
            for i in range(right, left-1, -1):
                print(matrix[bottom][i])
            bottom-=1

        if left <= right:
        # run left column
            for i in range(bottom, top-1, -1):
                print(matrix[i][left])
            left+=1




matrix = [
            [1, 2],
            [4, 5],
            [7, 8]
         ]

# all_elements_traversal(matrix)
# row_wise_traversal(matrix)
# col_wise_traversal(matrix)
# reverse_row_wise_traversal(matrix)
# top_left_bottom_right_diagonal_elements_traversal(matrix)
# top_right_bottom_left_diagonal_elements_traversal(matrix)
# zigzag_traversal(matrix)
spiral_traversal(matrix)
