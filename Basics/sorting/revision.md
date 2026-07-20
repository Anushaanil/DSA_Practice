# Sorting Algorithms

| Algorithm | Recognition | Main Hook | Time | Space |
|-----------|-------------|-----------|------|-------|
| Bubble Sort | Adjacent swapping | Largest element bubbles to the end after every pass | O(n²) | O(1) |
| Selection Sort | Repeatedly choose smallest/largest | Each pass fixes exactly one position | O(n²) | O(1) |
| Insertion Sort | Nearly sorted arrays | Insert current element into the already sorted left portion | O(n²), Best O(n) | O(1) |
| Merge Sort | Stable sorting, linked lists, divide & conquer | Split → Sort → Merge | O(n log n) | O(n) |
| Quick Sort | General-purpose fast sorting | Pivot partitions array into two halves | Avg O(n log n), Worst O(n²) | O(log n) |
| Heap Sort | Kth largest/smallest, priority queue | Build Heap → Extract Root repeatedly | O(n log n) | O(1) |

---

# Bubble Sort

## Pattern
Sorting

## Recognition 👀
Think Bubble Sort when:
- Learning sorting fundamentals.
- The question specifically asks for adjacent swaps.

## Main Logic
Repeatedly compare adjacent elements and swap if needed.

## Main Hook ⭐
After every pass, **the largest element reaches its correct position at the end**.

## Why This Works
Each adjacent swap pushes larger elements towards the end ("bubbling").

## Complexity

### Time: O(n²)
**Why?**
- Outer loop runs `n-1` passes.
- Inner loop compares adjacent elements in each pass.

### Space: O(1)
**Why?**
- Sorting is performed in-place.

## Memory Hook 🧠
> Bubble the largest element to the end after every pass.

---

# Selection Sort

## Pattern
Sorting

## Recognition 👀
Think Selection Sort when:
- Need minimum swaps.
- Want to repeatedly select the minimum/maximum element.

## Main Logic
Find the smallest element in the unsorted portion and swap it with the current position.

## Main Hook ⭐
After every pass, **the left side is permanently sorted**.

## Why This Works
Each pass fixes exactly one position.

## Complexity

### Time: O(n²)
**Why?**
- Every pass scans the remaining unsorted elements.

### Space: O(1)
**Why?**
- Uses only one index to track the smallest element.

## Memory Hook 🧠
> Find the smallest, place it in front.

---

# Insertion Sort

## Pattern
Sorting

## Recognition 👀
Think Insertion Sort when:
- Array is nearly sorted.
- Need an online sorting algorithm.

## Main Logic
Take one element and insert it into its correct position in the already sorted left half.

## Main Hook ⭐
Left side is always sorted.

## Why This Works
Every iteration expands the sorted portion by one element.

## Complexity

### Time
- Best: O(n)
- Average/Worst: O(n²)

**Why?**
Worst case shifts every previous element.

### Space: O(1)

**Why?**
Sorting happens in-place.

## Memory Hook 🧠
> Pick one card and insert it into the sorted hand.

---

# Merge Sort

## Recognition 👀
- Divide and Conquer
- Stable sorting
- Linked List sorting

## Main Hook ⭐
Split until one element remains, then merge while maintaining order.

## Complexity

### Time: O(n log n)

**Why?**
- log n levels of recursion.
- O(n) work at every level.

### Space: O(n)

**Why?**
Extra array is required during merging.

## Memory Hook 🧠
> Divide first, merge later.

---

# Quick Sort

## Recognition 👀
- Partitioning around a pivot.
- In-place Divide & Conquer.

## Main Hook ⭐
Correct pivot placement automatically divides the problem.

## Complexity

### Time
- Average: O(n log n)
- Worst: O(n²)

**Why?**
Balanced partitions give log n levels; worst case creates n levels.

### Space: O(log n)

**Why?**
Recursive call stack.

## Memory Hook 🧠
> Pivot decides everything.

---

# Heap Sort

## Recognition 👀
- Kth largest/smallest
- Priority Queue
- Heap problems

## Main Hook ⭐
Largest element always stays at the root.

## Complexity

### Time: O(n log n)

**Why?**
Building heap is O(n), then n heapify operations cost O(log n).

### Space: O(1)

**Why?**
Heap is built inside the original array.

## Memory Hook 🧠
> Build Heap → Remove Root.

---

# General Interview Rules

Whenever solving a new problem, ask yourself:

- Why does this algorithm work?
- How do I recognize this pattern?
- Why is the complexity O(...)?
- Can I explain the main hook in one sentence?
- What's the interview trick behind this solution?

If you cannot answer these five questions, you haven't fully understood the solution yet.