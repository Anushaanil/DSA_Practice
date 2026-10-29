a = 10 # 1010
b = 12 # 1100

# AND & operator
# A bit becomes 1 only when both corresponding bits are 1.
print(a&b, bin(a&b)[2:])

# OR (|)
# A bit becomes 1 when at least one corresponding bit is 1.
print(a|b, bin(a|b)[2:])

# XOR (^)
# A bit becomes 1 when the corresponding bits are different.
print(a^b, bin(a^b)[2:])

# Property 1: A number XOR itself is zero, as they are identical with no diff
print(8^8, bin(8^8)[2:])

# Property 2: XOR with zero leaves the number unchanged.
print(8^0, bin(8^0)[2:])

# Property 3: XOR is associative and commutative.
# a+b = b+a
# a+(b+c) = (a+b)+c
# This means you can reorder XOR operations and group them differently without changing the result.

# NOT (~)
# NOT flips every bit.
print(~5)  # -6

# Left shift (<<)
# Left shift moves bits to the left.
# Left shift is particularly useful for constructing masks.
# 5 = 0101   5 << 1 = 1010
# For non-negative integers, shifting left by k positions is equivalent to multiplying by (2^k)
# For example:
# 5 << 3 = 5 * 8 = 40

print(5 << 1)  # 10
print(5 << 2)  # 20

# Right shift (>>)
# Right shift moves bits to the right.
# 12 = 1100   12 >> 1 = 0110
# For non-negative integers, shifting right by k positions is equivalent to dividing by (2^k)
print(13 >> 1)  # 6
print(13 >> 2)  # 3
print(13 >> 3)  # 1

# bit manipulation tricks
#### Trick 1: Check whether the kth bit is set -- Perform AND
n = 13 # Binary = 1101 k =2
# How do we check it?
# Create a mask with only bit 2 set (right -> left 0->n)
mask = 1 << 2
# Now perform AND:
# n    = 1101
# mask = 0100
#        ----
# AND  = 0100
def is_bit_set(n: int, k: int) -> bool:
    return (n & (1<<k))!=0

print(is_bit_set(n, 2))

#### Trick 2: Set the kth bit -- Perform OR
# Regardless of the original bit, OR with 1 makes it 1.
def set_bit(n: int, k: int) -> int:
    return n | (1 << k)
print(set_bit(9, 2))

#### Trick 3: Clear the kth bit
def clear_bit(n: int, k: int) -> int:
    return n & ~(1 << k)

print(bin(13))
ans = clear_bit(13, 2)
print(bin(ans), ans)

#### Trick 4: Toggle the kth bit
def toggle_bit(n: int, k: int) -> int:
    return n ^ (1<<k)

print(bin(13))
ans = toggle_bit(13, 2)
print(bin(ans), ans)


#### Trick 5: Remove the rightmost set bit n & (n-1)
n = 13
print(n & (n - 1), bin(12)[2:])  # 12

# n = 13 = 1101
# n - 1  = 1100

#   1101
# & 1100
# ------
#   1100

#### Trick 6: Isolate the rightmost set bit
# - Position of the rightmost set bit: 2
# - Value of that bit: \(2^2 = 4\)
# - Result of n & (-n): 4
# How do we represent -12?
# In two's complement, we calculate the negative representation by:
# 1. Inverting all bits of 12.
# 2. Adding 1.
n = 12
ans = n & (-n)
print(ans, bin(ans)[2:])

def is_power_of_2(num):
    return num > 0 and (num & (num - 1))==0

print(is_power_of_2(10))

# Brian Kernighan's algorithm
def count_set_bits(num):
    count = 0
    while num > 0:
        num = num & (num-1)
        count+=1
    return count

print(bin(18), count_set_bits(18))

# built in method
n = 18
print(n.bit_count())

print(7&1) # gives 1 as answe so odd
print(10&1) # gives 0 as answer so even


# Task	Expression
# Check whether kth bit is set	(n & (1 << k)) != 0
# Set kth bit	n | (1 << k)
# Clear kth bit	n & ~(1 << k)
# Toggle kth bit	n ^ (1 << k)
# Remove rightmost set bit	n & (n - 1)
# Isolate rightmost set bit	n & -n
# Check whether n is a power of 2	n > 0 and (n & (n - 1)) == 0
# Count set bits	n.bit_count()
# Multiply by \(2^k\)	n << k
# Divide a non-negative n by \(2^k\), discarding the remainder	n >> k
# Check whether n is odd	n & 1
# Check whether n is even	(n & 1) == 0


# One final trick: odd and even checks do not require division or modulo.

# The last bit of an odd number is always 1, while the last bit of an even number is always 0.

def singleNumber(nums: list[int]) -> int:
        res = 0
        for i in range(32):
            count = 0
            for n in nums:
                count += (n >> i) & 1

            if count % 3 != 0:
                res |= (1<<i)
        return res


def singleNumberInt(nums):
    result = 0

    for i in range(32):
        count = 0

        for num in nums:
            print(num, i, (bin(num >> i)[2:]), num >> i)
            count += (num >> i) & 1
            print('count', count)
        if count % 3:
            result |= (1 << i)

    if result >= (1 << 31):
        result -= (1 << 32)

    return result

# print(singleNumberInt([0,1,0,1,0,1,99]))

def rangeBitwiseAnd(left: int, right: int) -> int:
    shifts = 0

    while left!=right:
        left = left >> 1
        right = right >> 1
        shifts+=1

    return left << shifts

# Brian Kernighan's trick
def rangeBitwiseAndBrian(left: int, right: int) -> int:
    while right > left:
        right = right & (right-1)
    return right

# print(rangeBitwiseAnd(26,30))
print(rangeBitwiseAndBrian(26,30))