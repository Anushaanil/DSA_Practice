# Bit Manipulation: Your DSA Masterclass

## 1. Learning Roadmap

| Phase | Topics | Goal |
|---|---|---|
| 1. Fundamentals | Binary numbers, powers of 2 | Understand how numbers are represented |
| 2. Bitwise operators | `&`, `\|`, `^`, `~`, `<<`, `>>` | Understand what each operator does |
| 3. Essential tricks | Check, set, clear, toggle a bit | Manipulate individual bits |
| 4. Mathematical tricks | `n & (n-1)`, `n & -n` | Recognize important binary patterns |
| 5. XOR patterns | Single number, missing number, duplicates | Solve common interview problems |
| 6. Counting bits | Brian Kernighan's algorithm, bit counting | Optimize binary operations |
| 7. Bitmasking | Represent sets using integers | Solve state-tracking problems |
| 8. Subsets | Generate all subsets using bitmasks | Connect bit manipulation to backtracking |
| 9. Advanced problems | XOR basis concepts, masks with DP, state compression | Prepare for harder interview questions |

**Rule:** Understand the concept, manually trace examples, solve problems, and then learn the optimization.

---

# Phase 1: Understand Binary Numbers

## 2. What Is a Binary Number?

Computers represent integers using bits: `0` and `1`.

Decimal uses base 10, whereas binary uses base 2.

For example:

\[
347 = 3 \times 10^2 + 4 \times 10^1 + 7 \times 10^0
\]

In binary:

```text
Decimal: 13
Binary:  1101
```

Each binary position represents a power of 2.

| Bit position | 3 | 2 | 1 | 0 |
|---|---:|---:|---:|---:|
| Power of 2 | 8 | 4 | 2 | 1 |
| Binary digit | 1 | 1 | 0 | 1 |

Therefore:

\[
13 = 1(8) + 1(4) + 0(2) + 1(1)
\]

\[
13 = 8 + 4 + 1
\]

Thus, `1101` represents decimal `13`.

## 3. Important Terminology

Consider:

```text
n = 13
Binary = 1101
```

- **Bit:** A single binary digit, either `0` or `1`.
- **LSB:** Least Significant Bit; the rightmost bit.
- **MSB:** Most Significant Bit; the leftmost bit in the representation.
- **Set bit:** A bit whose value is `1`.
- **Unset bit:** A bit whose value is `0`.

For `1101`, there are three set bits.

### Convert Decimal to Binary in Python

```python
n = 13

print(bin(n))       # 0b1101
print(bin(n)[2:])   # 1101
```

### Convert Binary to Decimal in Python

```python
print(int("1101", 2))  # 13
```

## 4. Powers of 2 in Binary

```text
1  = 0001
2  = 0010
4  = 0100
8  = 1000
16 = 10000
```

**Key observation:** Every positive power of 2 has exactly one set bit.

This property is useful when solving power-of-two problems.

---

# Phase 2: The Six Bitwise Operators

Consider:

```text
a = 10 = 1010
b = 12 = 1100
```

## 5. AND (`&`)

A bit becomes `1` only when both corresponding bits are `1`.

### Truth Table

| A | B | A & B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

### Example

```text
a = 1010
b = 1100
    ----
&   1000
```

```python
print(10 & 12)  # 8
```

### Applications

- Checking whether a bit is set.
- Clearing a bit using a mask.
- Checking whether a number is a power of 2.
- Counting set bits.
- Working with bitmasks.

---

## 6. OR (`|`)

A bit becomes `1` when at least one corresponding bit is `1`.

### Example

```text
a = 1010
b = 1100
    ----
|   1110
```

```python
print(10 | 12)  # 14
```

### Applications

- Setting a bit.
- Combining flags.
- Building bitmasks.
- Representing sets.

---

## 7. XOR (`^`)

XOR stands for exclusive OR.

A bit becomes `1` when the corresponding bits are different.

### Truth Table

| A | B | A ^ B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

### Example

```text
a = 1010
b = 1100
    ----
^   0110
```

```python
print(10 ^ 12)  # 6
```

### Three Essential XOR Properties

**Property 1: A number XOR itself is zero.**

\[
a \oplus a = 0
\]

```python
print(7 ^ 7)  # 0
```

**Property 2: XOR with zero leaves the number unchanged.**

\[
a \oplus 0 = a
\]

```python
print(7 ^ 0)  # 7
```

**Property 3: XOR is associative and commutative.**

\[
a \oplus b = b \oplus a
\]

\[
(a \oplus b) \oplus c = a \oplus (b \oplus c)
\]

Therefore, XOR operations can be reordered and regrouped without changing the result.

### XOR Interview Pattern: Single Number

Consider:

```python
nums = [4, 1, 2, 1, 2]
```

Every number appears twice except `4`.

XOR all the numbers:

\[
4 \oplus 1 \oplus 2 \oplus 1 \oplus 2
\]

Rearrange:

\[
(1 \oplus 1) \oplus (2 \oplus 2) \oplus 4
\]

Since identical numbers cancel out:

\[
0 \oplus 0 \oplus 4 = 4
\]

The answer is `4`.

This is the core idea behind **LeetCode 136: Single Number**.

---

## 8. NOT (`~`)

NOT flips every bit.

```text
0 becomes 1
1 becomes 0
```

For an illustrative 8-bit representation:

```text
00001101
```

Flipping every bit gives:

```text
11110010
```

However, Python handles integer bitwise NOT using its signed integer semantics.

```python
print(~5)  # -6
```

The identity to remember is:

\[
\boxed{\sim n = -(n+1)}
\]

Therefore:

\[
\sim 5 = -(5+1) = -6
\]

**Interview warning:** Do not confuse fixed-width bit flipping with Python's `~` operator. Fixed-width unsigned representations can produce different results.

---

## 9. Left Shift (`<<`)

Left shift moves bits to the left.

```text
5 = 0101

5 << 1 = 1010
```

```python
print(5 << 1)  # 10
print(5 << 2)  # 20
```

For non-negative integers:

\[
\boxed{n \ll k = n \times 2^k}
\]

For example:

\[
5 \ll 3 = 5 \times 8 = 40
\]

### Application: Constructing a Mask

```python
mask = 1 << 3

print(mask)  # 8
```

Binary representation:

```text
00001000
```

This creates a number whose bit at position `3` is set.

---

## 10. Right Shift (`>>`)

Right shift moves bits to the right.

```text
12 = 1100

12 >> 1 = 0110
```

```python
print(12 >> 1)  # 6
```

For non-negative integers:

\[
\boxed{n \gg k = \left\lfloor \frac{n}{2^k} \right\rfloor}
\]

Examples:

```python
print(13 >> 1)  # 6
print(13 >> 2)  # 3
print(13 >> 3)  # 1
```

Each right shift by one position divides a non-negative integer by two and discards the fractional part.

### Operator Summary

| Operator | Name | Main idea | Example |
|---|---|---|---|
| `&` | AND | Both bits must be 1 | `10 & 12 = 8` |
| `\|` | OR | At least one bit must be 1 | `10 \| 12 = 14` |
| `^` | XOR | Bits must differ | `10 ^ 12 = 6` |
| `~` | NOT | Flip every bit | `~5 = -6` in Python |
| `<<` | Left shift | Move bits left | `5 << 2 = 20` |
| `>>` | Right shift | Move bits right | `12 >> 1 = 6` |

---

# Phase 3: Essential Bit Manipulation Tricks

Assume `n` is a non-negative integer and `k` is a valid, non-negative bit position.

Bit positions are counted from the right, starting at zero.

For example:

```text
Binary:   1 1 0 1
Position: 3 2 1 0
```

## 11. Check Whether the kth Bit Is Set

Suppose:

```text
n = 13 = 1101
```

Check whether bit position `2` is set.

First, construct the mask:

```python
mask = 1 << 2
```

The mask is:

```text
0100
```

Now perform AND:

```text
n    = 1101
mask = 0100
       ----
AND  = 0100
```

The result is nonzero, so bit `2` is set.

### Implementation

```python
def is_bit_set(n: int, k: int) -> bool:
    return (n & (1 << k)) != 0
```

Examples:

```python
print(is_bit_set(13, 2))  # True
print(is_bit_set(13, 1))  # False
```

**Pattern:**

```python
n & (1 << k)
```

Use this when a problem asks whether a particular bit is set.

---

## 12. Set the kth Bit

Setting a bit means changing it to `1`, regardless of its original value.

Suppose:

```text
n = 9 = 1001
```

Set bit position `2`.

Mask:

```text
0100
```

Perform OR:

```text
n    = 1001
mask = 0100
       ----
OR   = 1101
```

The result is `13`.

### Implementation

```python
def set_bit(n: int, k: int) -> int:
    return n | (1 << k)
```

```python
print(set_bit(9, 2))  # 13
```

Why does it work?

| Existing bit | Mask bit | Result |
|---|---|---|
| 0 | 1 | 1 |
| 1 | 1 | 1 |

OR with `1` always produces `1`.

**Pattern:**

```python
n | (1 << k)
```

---

## 13. Clear the kth Bit

Clearing a bit means changing it to `0`.

Suppose:

```text
n = 13 = 1101
```

Clear bit position `2`.

Mask:

```text
1 << 2 = 0100
```

Complement the mask. Using a four-bit illustration:

```text
0100 -> 1011
```

Now perform AND:

```text
n       = 1101
mask    = 1011
          ----
AND     = 1001
```

The result is `9`.

### Implementation

```python
def clear_bit(n: int, k: int) -> int:
    return n & ~(1 << k)
```

```python
print(clear_bit(13, 2))  # 9
```

AND with `0` clears a bit. AND with `1` preserves the original bit.

**Pattern:**

```python
n & ~(1 << k)
```

---

## 14. Toggle the kth Bit

Toggling means:

- `0` becomes `1`.
- `1` becomes `0`.

Suppose:

```text
n = 13 = 1101
```

Toggle bit position `2`:

```text
n    = 1101
mask = 0100
       ----
XOR  = 1001
```

The result is `9`.

### Implementation

```python
def toggle_bit(n: int, k: int) -> int:
    return n ^ (1 << k)
```

```python
print(toggle_bit(13, 2))  # 9
print(toggle_bit(9, 2))   # 13
```

Toggling the same bit twice restores the original number.

\[
(n \oplus m) \oplus m = n
\]

**Pattern:**

```python
n ^ (1 << k)
```

---

## 15. Remove the Rightmost Set Bit

This is one of the most important tricks in bit manipulation.

\[
\boxed{n \ \& \ (n-1)}
\]

Suppose:

```text
n = 12 = 1100
```

Subtract one:

```text
n     = 1100
n - 1 = 1011
```

Subtracting one changes the rightmost set bit from `1` to `0` and changes all bits to its right from `0` to `1`.

Now perform AND:

```text
n     = 1100
n - 1 = 1011
        ----
AND   = 1000
```

The rightmost set bit has been removed.

Another example:

```text
n = 13 = 1101
n - 1 = 1100

  1101
& 1100
------
  1100
```

### Implementation

```python
n = 12
print(n & (n - 1))  # 8
```

### Applications

- Counting set bits.
- Checking whether a number is a power of 2.
- Repeatedly removing set bits.
- Optimizing certain bit manipulation problems.

---

## 16. Isolate the Rightmost Set Bit

The expression is:

\[
\boxed{n \ \& \ (-n)}
\]

Suppose:

```text
n = 12 = 1100
```

Using an 8-bit two's-complement illustration:

```text
 n = 00001100
-n = 11110100
```

AND them:

```text
 n = 00001100
-n = 11110100
     --------
AND  = 00000100
```

The result is `4`, corresponding to bit position `2`.

### Implementation

```python
n = 12
print(n & -n)  # 4
```

Another example:

```python
n = 40  # Binary: 101000
print(n & -n)  # 8
```

### Important Distinction

| Expression | Purpose |
|---|---|
| `n & (n - 1)` | Removes the rightmost set bit |
| `n & -n` | Isolates the rightmost set bit |

Do not confuse these two expressions.

---

# Phase 4: Important Interview Patterns

## 17. Check Whether a Number Is a Power of 2

A positive power of 2 has exactly one set bit.

Examples:

```text
1  = 0001
2  = 0010
4  = 0100
8  = 1000
16 = 10000
```

Consider `8`:

```text
n     = 8 = 1000
n - 1 = 7 = 0111
```

AND:

```text
  1000
& 0111
------
  0000
```

The result is zero.

Now consider `10`:

```text
n     = 10 = 1010
n - 1 =  9 = 1001
```

AND:

```text
  1010
& 1001
------
  1000
```

The result is not zero.

Therefore, for a positive integer:

\[
\boxed{n > 0 \text{ and } (n \ \& \ (n-1)) = 0}
\]

### Implementation

```python
def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0
```

Examples:

```python
print(is_power_of_two(1))   # True
print(is_power_of_two(8))   # True
print(is_power_of_two(16))  # True
print(is_power_of_two(10))  # False
print(is_power_of_two(0))   # False
print(is_power_of_two(-8))  # False
```

**Important:** The `n > 0` condition is necessary. Zero is not a power of 2.

---

## 18. Count the Number of Set Bits

Suppose:

```text
n = 13 = 1101
```

There are three set bits.

### Approach 1: Check Each Bit

```python
def count_set_bits(n: int) -> int:
    count = 0

    while n > 0:
        count += n & 1
        n >>= 1

    return count
```

Why does `n & 1` work?

The mask `1` is:

```text
0001
```

AND with this mask checks whether the rightmost bit is set.

```text
1101 & 0001 = 0001
1100 & 0001 = 0000
```

Each iteration examines one bit.

**Time complexity:** `O(log n)` for positive integers.

**Auxiliary space:** `O(1)`.

### Approach 2: Brian Kernighan's Algorithm

Instead of examining every bit, remove the rightmost set bit each time.

```python
def count_set_bits(n: int) -> int:
    count = 0

    while n > 0:
        n &= n - 1
        count += 1

    return count
```

For `n = 13`:

```text
Initial: 1101

Iteration 1:
1101 & 1100 = 1100
count = 1

Iteration 2:
1100 & 1011 = 1000
count = 2

Iteration 3:
1000 & 0111 = 0000
count = 3
```

The loop runs exactly as many times as there are set bits.

If the number has `k` set bits:

- Time complexity: `O(k)`.
- Auxiliary space: `O(1)`.

For sparse binary representations, this can be more efficient than examining every bit.

Python also provides:

```python
n.bit_count()
```

This counts the set bits of a non-negative integer directly.

**Interview advice:** Learn to derive Brian Kernighan's algorithm yourself, even though Python has a built-in method.

---

## 19. Find the Number That Appears Once

**Problem: LeetCode 136 — Single Number**

Given an array in which every element appears twice except one element, find the element that appears once.

Example:

```python
nums = [4, 1, 2, 1, 2]
```

Expected output:

```text
4
```

### Brute-Force Approach

Count the frequency of each element using a dictionary.

This works but requires additional space.

### Optimal XOR Approach

```python
def singleNumber(nums: list[int]) -> int:
    result = 0

    for num in nums:
        result ^= num

    return result
```

Why does it work?

\[
a \oplus a = 0
\]

\[
a \oplus 0 = a
\]

Every duplicated element cancels itself out, leaving only the unique element.

### Complexity

- **Time:** `O(n)`.
- **Auxiliary space:** `O(1)`.

### Limitation

This approach works when every other value occurs exactly twice and one value occurs once.

Variants where elements appear three times, or where two elements occur once, require different reasoning.

---

# Phase 5: Bit Manipulation Cheat Sheet

Assume `n` is a non-negative integer and `k` is a valid bit position.

| Task | Expression |
|---|---|
| Check whether kth bit is set | `(n & (1 << k)) != 0` |
| Set kth bit | `n \| (1 << k)` |
| Clear kth bit | `n & ~(1 << k)` |
| Toggle kth bit | `n ^ (1 << k)` |
| Remove rightmost set bit | `n & (n - 1)` |
| Isolate rightmost set bit | `n & -n` |
| Check whether n is a power of 2 | `n > 0 and (n & (n - 1)) == 0` |
| Count set bits | `n.bit_count()` |
| Multiply by `2^k` | `n << k` |
| Divide non-negative n by `2^k`, discarding the remainder | `n >> k` |
| Check whether n is odd | `n & 1` |
| Check whether n is even | `(n & 1) == 0` |

### Odd and Even Without Modulo

The rightmost bit of an odd number is always `1`. The rightmost bit of an even number is always `0`.

```text
7  = 0111 -> 7 & 1 = 1 -> Odd
10 = 1010 -> 10 & 1 = 0 -> Even
```

```python
def is_odd(n: int) -> bool:
    return (n & 1) == 1

def is_even(n: int) -> bool:
    return (n & 1) == 0
```

---

# Phase 6: Mentor-Assigned Exercises

**Do not write code immediately. Solve these manually using binary representations first.**

## Question 1: Basic Operators

What are the results?

```python
a = 10
b = 6

print(a & b)
print(a | b)
print(a ^ b)
print(a << 1)
print(a >> 1)
```

For each answer, explain at least one operation in binary.

## Question 2: Set a Bit

Given:

```python
n = 10  # Binary: 1010
```

What is the result of setting bit position `0`?

Write:
1. The mask.
2. The binary operation.
3. The final decimal result.

## Question 3: Clear a Bit

Given:

```python
n = 15  # Binary: 1111
```

What happens when you clear bit position `2`?

## Question 4: XOR Reasoning

What is the output?

```python
result = 5 ^ 7 ^ 5
print(result)
```

Explain why the answer is correct without converting every number to binary.

## Question 5: Remove the Rightmost Set Bit

Given:

```python
n = 20  # Binary: 10100
print(n & (n - 1))
```

What is the output? Show the binary subtraction and AND operation.

## Question 6: Power of 2

Which of these are powers of 2?

```text
0, 1, 2, 6, 8, 16, 18, 32
```

Explain the bitwise property that distinguishes powers of 2.

## Question 7: Count Set Bits

How many set bits does `29` have?

Do not use `bit_count()` or `bin()`.

Manually trace Brian Kernighan's algorithm until the number becomes zero.

---

# Next Steps

After completing these exercises, move through the following topics in order:

1. **XOR patterns:** Single Number II, Missing Number, and finding two unique numbers.
2. **Bit manipulation interview patterns:** Counting bits, reversing bits, and checking individual bits.
3. **Bitmasking:** Representing sets, generating subsets, and solving state-based problems.
4. **Advanced DSA:** Bitmask DP and problems where bit manipulation improves the algorithm.

## Final Mentor Advice

Do not memorize bit manipulation tricks without understanding why they work.

For every expression, ask yourself:

- What does each bit represent?
- Why does this operator produce the required result?
- Can I derive the expression instead of memorizing it?
- What are the edge cases?
- What are the time and space complexities?

Bit manipulation is most useful when it provides a compact way to represent or manipulate binary states. It is not automatically better than ordinary arithmetic or data structures.