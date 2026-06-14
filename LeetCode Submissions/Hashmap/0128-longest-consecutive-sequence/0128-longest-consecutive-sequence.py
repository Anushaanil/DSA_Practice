class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # using set to avoid duplicates
        nums_set = set(nums)
        current_chain = 0
        longest_chain = 0

        for num in nums_set:
            # gives us the start of the chain
            if num - 1 not in nums_set:
                cur_num = num
                current_chain = 1
                # gives us the sequence
                while cur_num + 1 in nums_set:
                    cur_num += 1
                    current_chain += 1

                longest_chain = max(longest_chain, current_chain)
                
        return longest_chain