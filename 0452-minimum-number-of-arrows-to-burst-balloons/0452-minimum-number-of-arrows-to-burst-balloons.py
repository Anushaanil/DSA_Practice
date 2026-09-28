class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x:x[1])
    
        smallest_right_boundary = points[0][1]
        arrows = 1
        
        for point in points[1:]:
            if point[0] <= smallest_right_boundary <= point[1]:
                smallest_right_boundary = min(smallest_right_boundary, point[1])
            else:
                arrows+=1
                smallest_right_boundary = point[1]

        return arrows