
def findMinArrowShots(points: list[list[int]]) -> int:
    
    points.sort()
    
    smallest_right_boundary = points[0][1]
    arrows = 1
    
    for point in points[1:]:
        if point[0] <= smallest_right_boundary <= point[1]:
            smallest_right_boundary = min(smallest_right_boundary, point[1])
        else:
            arrows+=1
            smallest_right_boundary = point[1]

    return arrows

points = [[10,16],[2,8],[1,6],[7,12]]
# points = [[1,2],[3,4],[5,6],[7,8]]
# points = [[1,2],[2,3],[3,4],[4,5]]
arrows = findMinArrowShots(points)
print(arrows)