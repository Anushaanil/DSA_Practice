class Solution:
    def myPow(self, x: float, n: int) -> float:
        negative_exp = n < 0
        n = abs(n)

        res = 1.0

        while n > 0:
            if n % 2 == 1:
                res *= x

            x *= x
            n //= 2

        if negative_exp:
            return 1 / res

        return res