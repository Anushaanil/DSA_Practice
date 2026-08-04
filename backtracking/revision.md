# Backtracking Notes

## What is Backtracking?

Backtracking is a recursive technique used to **explore all possible choices** and **undo a choice** before exploring the next one.

Think of it as:

> **Choose → Explore → Undo → Explore**

It is commonly used to generate **all valid combinations, permutations, paths, or configurations**.

---

# When should I think of Backtracking?

Backtracking is usually the right approach when the problem asks for:

- All subsets
- All combinations
- All permutations
- All possible paths
- Every valid arrangement
- Search with constraints (Sudoku, N-Queens, Word Search)

Keywords:

- All possible...
- Generate...
- Find every...
- Return every...

---

# The Core Pattern

```
Make a choice

↓

Explore recursively

↓

Undo the choice (Backtrack)

↓

Explore another choice
```

---

# The Three Steps

## 1. Choose

Make one decision.

Example:

```
Include current number
```

or

```
Place a queen
```

or

```
Move Right
```

---

## 2. Explore

Recursively continue solving the remaining problem.

```
dfs(next_state)
```

---

## 3. Undo (Backtrack)

Remove the last choice so other possibilities can be explored.

```
path.pop()
```

Without undoing, every recursive branch would affect the next one.

---

# The Current Path vs Final Answer

This is one of the most important concepts.

## Current Path

Temporary.

Keeps changing during recursion.

Example:

```
[]
↓

[1]

↓

[1,2]

↓

[1,2,3]
```

Usually called:

- path
- current
- subset
- res

---

## Final Answer

Permanent.

Stores completed solutions.

```
[
 [1,2,3],
 [1,2],
 [1],
 []
]
```

Usually called:

```
ans
```

---

# Why do we copy the current path?

Suppose:

```
path = [1,2]
```

If we do

```
ans.append(path)
```

both variables point to the **same list**.

Later,

```
path.pop()
```

changes

```
ans
```

too.

Instead,

```
ans.append(path.copy())
```

stores a snapshot.

Think of it as taking a photograph of the current path.

---

# Generic Backtracking Template

```
def dfs(...):

    if solution found:
        save a copy
        return

    make a choice

    dfs(...)

    undo the choice
```

Some problems have multiple choices:

```
for every possible choice:

    choose

    dfs()

    undo
```

---

# Two Common Types

## Type 1 — Include / Exclude

Each element has two choices.

```
Take it

OR

Skip it
```

Used in:

- Subsets
- Subsequence problems

Recursion Tree:

```
          []
        /     \
     Take     Skip
     /           \
   Take         Skip
```

Total subsets:

```
2^n
```

---

## Type 2 — Iterate Through Choices

Instead of just two choices, iterate over all available options.

```
for i in range(...):

    choose nums[i]

    dfs(...)

    undo
```

Used in:

- Combination Sum
- Permutations
- N-Queens
- Word Search

---

# Base Case

The base case means:

> "A complete solution has been built."

Examples:

Subsets

```
Reached end of array
```

Permutations

```
Current permutation length == n
```

Sudoku

```
Board completely filled
```

N-Queens

```
All queens placed
```

---

# Recursion State

Every recursive function should answer:

> **What information do I need to continue solving from here?**

Common state variables:

```
index
current path
visited
remaining target
board
```

Avoid carrying unnecessary information.

---

# Why do we backtrack?

Imagine

```
path = []
```

Choose

```
1
```

```
path = [1]
```

Choose

```
2
```

```
path = [1,2]
```

Now explore.

After finishing,

remove

```
2
```

```
path = [1]
```

Now another branch can choose

```
3
```

```
path = [1,3]
```

Without removing 2, this branch would become

```
[1,2,3]
```

which is incorrect.

---

# Time Complexity

Backtracking often explores **every possible solution**.

Common complexities:

Subsets

```
O(2^n)
```

Permutations

```
O(n!)
```

N-Queens

```
Approximately O(N!)
```

Word Search

```
O(4^L)
```

---

# Space Complexity

Mostly due to recursion stack.

Maximum depth:

```
O(n)
```

Extra answer storage is usually excluded unless explicitly asked.

---

# Common Mistakes

❌ Forgetting to undo the choice

```
path.append(x)

dfs()

# Missing

path.pop()
```

---

❌ Appending the same list

```
ans.append(path)
```

Should be

```
ans.append(path.copy())
```

---

❌ Wrong base case

Always ask:

> "When have I built one complete solution?"

---

❌ Returning values unnecessarily

Most backtracking functions don't return useful values.

Instead they modify

```
ans
```

---

❌ Confusing current path with final answer

Current path

```
Temporary
```

Answer

```
Permanent
```

---

# Mental Model

Imagine walking through a maze.

At every junction:

```
Choose a direction

↓

Walk

↓

Dead end?

↓

Walk back

↓

Try another direction
```

Walking back is exactly what **backtracking** means.

---

# Problems to Practice

Easy

- ✅ Subsets
- ✅ Subsets II
- ✅ Combination Sum
- ✅ Combination Sum II

Medium

- ✅ Permutations
- ✅ Permutations II
- ✅ Letter Combinations of a Phone Number
- ✅ Palindrome Partitioning

Hard

- ✅ N-Queens
- ✅ Sudoku Solver
- ✅ Word Search II

---

# Key Takeaways

- Backtracking = **Choose → Explore → Undo**
- Maintain a **current path** and a **final answer** separately.
- Save **copies** of completed solutions.
- Undo every choice before exploring another branch.
- Think in terms of **decisions**, not loops.
- The recursion state should contain exactly what is needed to make the next decision.