class Solution:
    def reverseBits(self, n: int) -> int:
        # b = '0'* (32-len(bin(n)[2:])) + bin(n)[2:] if len(bin(n)[2:])< 32 else bin(n)[2:]
        b = bin(n)[2:].zfill(32)
        return int(b[::-1], 2)
        