# Binary Search - Interview Revision

## 📌 Recognition 👀

Think Binary Search whenever you see:

- Sorted array
- Monotonic answer
- First/Last occurrence
- Search in O(log n)
- Minimum/Maximum possible value
- Kth smallest/largest
- Rotated sorted array
- Peak element
- Infinite sorted array
- Search space can be reduced by half

---

# Main Idea ⭐

Binary Search is **not just searching an element**.

It is about **eliminating half of the search space every iteration.**

---

# Binary Search Checklist ✅

Before solving ask yourself:

- Is the search space sorted?
- Can I eliminate one half confidently?
- Am I searching an element or an answer?
- Which pointer should move?
- Am I looking for:
    - Exact answer
    - First occurrence
    - Last occurrence
    - Lower Bound
    - Upper Bound

---

# Binary Search Templates

## 1. Classic Binary Search

Use when searching an exact element.

```python
while left <= right:
```

Move pointers:

```
nums[mid] == target
return

nums[mid] < target
left = mid + 1

nums[mid] > target
right = mid - 1
```

---

## 2. Boundary Search

Use when searching:

- First occurrence
- Last occurrence
- Lower Bound
- Upper Bound

```python
while left < right:
```

Don't return immediately.

Shrink towards the answer.

---

## 3. Binary Search on Answer

Used for problems like:

- Koko Eating Bananas
- Ship Within Days
- Allocate Books
- Split Array Largest Sum

Instead of searching an element,
search the **minimum/maximum valid answer**.

---

# Common Tricks ⭐

### Search Insert Position

Target not found?

Return

```python
left
```

because left always points to the insertion position.

---

### First Occurrence

Move

```
right = mid
```

when condition is true.

Keep searching left.

---

### Last Occurrence

Move

```
left = mid
```

using

```python
mid = (left + right + 1) // 2
```

to avoid infinite loops.

---

### Rotated Sorted Array

Main Hook ⭐

> One half is **always sorted**.

Find the sorted half first.

---

### Peak Element

Main Hook ⭐

Compare

```
nums[mid]
nums[mid+1]
```

If decreasing

```
peak is on left
```

Else

```
peak is on right
```

---

### Minimum in Rotated Array

Main Hook ⭐

Compare

```
nums[mid]
nums[right]
```

If

```
nums[mid] <= nums[right]
```

minimum lies on left.

Else

minimum lies on right.

---

### Infinite Sorted Array

Main Hook ⭐

First expand the search window exponentially.

```
1
2
4
8
16
32
...
```

Then apply Binary Search.

---

### Median of Two Sorted Arrays

Main Hook ⭐

Don't merge arrays.

Partition both arrays so that

```
Left Partition <= Right Partition
```

Median lies between partitions.

---

### TimeMap

Main Hook ⭐

For every key:

Store timestamps in sorted order.

Binary Search for the **largest timestamp ≤ given timestamp**.

---

# Time Complexity

## Classic Binary Search

Time

```
O(log n)
```

Why?

Every iteration removes **half** the search space.

```
n

n/2

n/4

n/8

...
```

After log₂(n) steps only one element remains.

---

## Space

```
O(1)
```

Why?

Only pointers are used.

No extra array or recursion.

---

# Binary Search on Answer Complexity

Usually

```
O(n log M)
```

Why?

- Binary Search takes **log M**
- Every validity check scans the array once (**O(n)**)

Example:

Koko Eating Bananas

```
O(n log(maxPile))
```

Ship Within Days

```
O(n log(sum(weights)))
```

---

# Pointer Memory Tricks 🧠

After Binary Search fails:

```
left
```

→ Smallest value greater than target

```
right
```

→ Largest value smaller than target

---

# Mid Formula

Normal

```python
mid = (left + right) // 2
```

Upper Mid

```python
mid = (left + right + 1) // 2
```

Use upper mid whenever

```
left = mid
```

Otherwise you'll get an infinite loop.

---

# Interview Memory Hooks 🧠

- Binary Search = Eliminate half every iteration.
- Rotated Array = One half is always sorted.
- Peak = Compare with next element.
- First Occurrence = Keep moving left.
- Last Occurrence = Keep moving right.
- Binary Search on Answer = Search answer, not element.
- TimeMap = Largest timestamp ≤ target.
- Median = Partition, don't merge.