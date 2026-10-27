class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for i in range(32):
            count = 0
            for n in nums:
                count += (n >> i) & 1

            if count % 3 != 0:
                res |= (1<<i)

        # Convert 32-bit two's complement to a negative Python integer
        if res >= (1 << 31):
            res -= (1 << 32)
            
        return res