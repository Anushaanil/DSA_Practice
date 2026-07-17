import heapq
from typing import List
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # heap push and maintain only k records which are close to origin
        heap = []
        for point in points:
            distance = -1 * sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(heap, [distance, point])

            if len(heap) > k:
                heapq.heappop(heap)

        return [item[1] for item in heap]

s = Solution()
points = [[0,2],[2,0], [2,2]]
k = 2
print(s.kClosest(points, k))