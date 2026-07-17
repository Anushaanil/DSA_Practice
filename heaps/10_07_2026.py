from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        self.heap = [-1*i for i in stones]
        
        print('before', self.heap)

        while len(self.heap) > 1:
            heapq.heapify(self.heap)
            print('here onwards', self.heap)

            # while len(self.heap) > 2:
            #     heapq.heappop(self.heap)
            
            # can't access it via indices like this because heap 
            # is not sorted array, 1st ele will be smallest but we can't say
            # 2nd is sorted as well here
            
            # x = self.heap[0]
            # y = self.heap[1]

            x = heapq.heappop(self.heap)
            y = heapq.heappop(self.heap)

            print('after pop', self.heap, x, y)

            if x < y:
                heapq.heappush(self.heap, x-y)
            
        print('at the end', self.heap)      
        return -1*self.heap[0]

s = Solution()
# stones = [2,3,6,2,4]
stones = [7,5,8]
print(s.lastStoneWeight(stones))