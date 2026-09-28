class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        pairs_count = {}
        equal_pair_count = 0
        
        for x in range(len(nums)-1):
            a = nums[x]
            b = nums[x+1]

            if a!=b:
                # a -> b would make this pair equal.
                pairs_count[(a,b)] = 1 + pairs_count.get((a,b), 0)
                
                # b -> a would make this pair equal.
                pairs_count[(b,a)] = 1 + pairs_count.get((b,a), 0)
            else:
                equal_pair_count+=1
        
        return equal_pair_count + max(pairs_count.values(), default=0)
