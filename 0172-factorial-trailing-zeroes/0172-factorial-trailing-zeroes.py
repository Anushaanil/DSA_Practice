class Solution:
    def trailingZeroes(self, n: int) -> int:
        # Thought of using BF first but for large number it fails, so using Legendre's formula
        # n! = [n/5] + [n/25] + [n/125] .. stop when div becomes zero

        count = 0
        pow = 1
        div = 1

        while div!=0:
            div = (n//5**pow)
            count += div
            pow += 1

        return count