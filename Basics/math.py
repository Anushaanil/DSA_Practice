def plusOne(digits: list[int]) -> list[int]:
        m = 1
        digit = 0

        for i in range(len(digits)-1, -1, -1):
            print(i, digits[i], m)
            digit+=digits[i]*m
            m*=10
        return list(map(int, str(1+digit)))
        
# digits = [0]
# p = plusOne(digits)
# print(p)

def trailingZeroes(n: int) -> int:
        # Thought of using BF first but for large number it fails, so using Legendre's formula
        # We divide by 5 (and its powers) because a trailing zero is created every time a 2 and a 5 multiply together to make 10.
        # counts numbers with at least one factor of 5:
        # Numbers like 5, 10, 15, and 20 each contribute one factor of 5.
        # n! = [n/5] + [n/25] + [n/125] .. stop when div becomes zero

        # count = 0
        # pow = 1
        # div = 1

        # while div!=0:
        #     div = (n//5**pow)
        #     print('div', div)

        #     count += div
        #     print('count', count)

        #     pow +=1
        #     print('pow', pow)
            
        # return count

        # simplest way possible div num by 5 and keep count
        count = 0
        while n >=5:
            n = n // 5
            count+=n
        return count

print(trailingZeroes(5))


def myPow(x: float, n: int) -> float:
    # handle -ve number don't do this at beginning 
    # as there could be issues with precision
    neg_num = n < 0
    n = abs(n)

    res = 1.0
    while n > 0:
        if n % 2 == 1:
            res *= x

        x *=x
        n //=2

    if neg_num: return 1/ res

    return res

print(myPow(2,5))
print(myPow(-0.9999999968539456, -1669585506))