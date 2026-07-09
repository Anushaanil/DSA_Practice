'''
 # @ Create Time: 2026-07-01 13:11:28
 # @ Modified time: 2026-07-01 16:06:08
 '''

import heapq

class KthLargest:
    def __init__(self, k, nums) -> None:
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

        print(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)
        print('push', self.heap)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

        print('after pop', self.heap)

        print(self.heap[0])
        return self.heap[0]

kthLargest = KthLargest(3, [1, 2, 3, 3])
kthLargest.add(3);   # return 3
kthLargest.add(5);   # return 3
kthLargest.add(6);   # return 3
kthLargest.add(7);   # return 5
kthLargest.add(8);   # return 6