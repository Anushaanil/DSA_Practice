def convert2binary(num):
    """
    Complexity:
    - Time: \(O(\log n)\)
    - Auxiliary space: \(O(\log n)\)
    Why \(O(\log n)\)?

    Every iteration divides the number by two. Therefore, a positive integer \(n\) requires approximately \(\log_2 n\) iterations.

    Using a list also avoids repeatedly rebuilding the entire string.
    """
    if num == 0:
        return "0"
    
    res = []
    while num>0:
        res.append(str(num%2))
        num = num//2
    return ''.join(res[::-1])


def convert2binarybuiltin(num):
    return bin(num)[2:]


def convert2decimal(bin_num):
    power = 1
    res = 0
    for i in range(len(bin_num)-1, -1, -1):
        if bin_num[i] == '1':
            res+=power
        power*=2
    return res
            
def convert2decimalbuiltin(bin_num):
    return int(bin_num, 2)

num = 13
res = convert2binary(num)
print(res) # stored in 32 bits for int like 00000... last 4 bits would be 1101

res = convert2binarybuiltin(num)
print(res)

ans = convert2decimal(res)
print(ans)

ans = convert2decimalbuiltin(res)
print(ans)

def addBinary(self, a: str, b: str) -> str:
    # int(a, 2) -> treats a as binary base 2 and then converts it into int
    return bin(int(a, 2) + int(b, 2))[2:]

def addBinaryXorWay(a, b):
    '''
    Every iteration does two things:
    1. XOR: Calculates the partial sum without carrying.
    2. AND + left shift: Calculates the carry that still needs to be added.
    The next iteration adds that carry to the partial sum.

    The process repeats until there are no carry bits left.
    '''
    x, y = int(a,2), int(b,2)

    while y:
        ans = x ^ y # add bits without carrying.
        carry = (x & y) << 1 # calculate the carry and move it to the next position.
        x, y = ans, carry

    return bin(x)[2:]

print(addBinaryXorWay('11', '1'))

def reverseBits(n: int) -> int:
    b = '0'* (32-len(bin(n)[2:])) + bin(n)[2:] if len(bin(n)[2:])< 32 else bin(n)[2:]
    return int(b[::-1], 2)

print(reverseBits(43261596))

def reverseBits(n: int) -> int:
    result = 0

    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1

    return result

print(reverseBits(43261596))