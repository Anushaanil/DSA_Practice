class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        m = 1
        digit = 0

        for i in range(len(digits)-1, -1, -1):
            digit+=digits[i] * m
            m*=10

        return list(map(int, str(1 + digit)))