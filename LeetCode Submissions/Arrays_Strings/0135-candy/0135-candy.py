class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        output = n*[1]

        # Equal conditions
        if len(set(ratings)) == 1:
            return n
        
        # Left Loop
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                output[i]+=output[i-1]
                
        # Right Loop
        for j in range(n-1, 0, -1):
            if ratings[j-1] > ratings[j]:
                output[j-1]=max(output[j-1], output[j]+1)
        
        # print('final output', output)
        return sum(output)