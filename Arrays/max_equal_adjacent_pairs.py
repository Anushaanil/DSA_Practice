def maxEqualAdjacentPairsBf(nums: list[int]) -> int:
    # brute force solution I developed on my own
    distinct_keys = list(set(nums))
    distinct_keys_len = len(distinct_keys)
    max_pairs = 0

    if distinct_keys_len == 1:
        return len(nums) - 1
    
    for x in range(distinct_keys_len):
        for y in range(distinct_keys_len):
            if x == y:
                continue

            count = 0
            nums_ = nums.copy()

            for z in range(len(nums_)):
                if nums_[z]==distinct_keys[x]:
                    nums_[z] = distinct_keys[y]

            print(distinct_keys[x], distinct_keys[y])
            print(nums_)

            for z in range(len(nums_)-1):
                if nums_[z]==nums_[z+1]:
                    count+=1
            print(count)

            max_pairs = max(max_pairs, count)

    print(max_pairs)
    return max_pairs

# nums = [2,8,2,5,5,6]
# maxEqualAdjacentPairsBf(nums)


def maxEqualAdjacentPairsOptimal(nums: list[int]) -> int:
    # optimal solution derived from GPT
    # distinct_keys_len = len(set(nums))
    pairs_count = {}
    equal_pair_count = 0
    
    # if distinct_keys_len == 1:
    #     return len(nums) - 1
    
    for x in range(len(nums)-1):
        # left and right anology
        # if x > 0:
        #     left = nums[x-1]
        #     if nums[x]!=left:
        #         pairs_count[(nums[x], left)] = 1+ pairs_count.get((nums[x], left), 0)

        # if x < len(nums)-1:
        #     right  = nums[x+1]
        #     if nums[x]!=right:
        #         pairs_count[(nums[x], right)] = 1+ pairs_count.get((nums[x], right), 0)
        
        # # current equal pairs
        # if nums[x]==nums[x+1]:
        #     equal_pair_count+=1
        
        # print(pairs_count)

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

nums = [2,8,2,5,5,6]
ans = maxEqualAdjacentPairsOptimal(nums)
print(ans)