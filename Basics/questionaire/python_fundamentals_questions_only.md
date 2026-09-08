# Python Fundamentals — Interview Self-Test

**Purpose:** Questions only. No answers or hints.

**How to use:** For each question, mark yourself:
- **3** — Can answer clearly + explain why
- **2** — Know the concept but need some thought
- **1** — Recognize it but cannot explain properly
- **0** — Don't know

---

## 1. Objects, References & Mutability

1. What is the difference between an object and a variable in Python?
2. What happens here?
   ```python
   a = [1, 2, 3]
   b = a
   b.append(4)
   print(a)
   print(b)
   ```
3. What is the difference between:
   ```python
   a = b
   a = b.copy()
   ```
4. What is the difference between `==` and `is`?
5. What are mutable and immutable objects?
6. Is a tuple always immutable?
7. What happens here?
   ```python
   a = [1, 2, 3]
   b = a.copy()
   b.append(4)
   ```
8. What is a shallow copy?
9. Demonstrate the shallow-copy problem:
   ```python
   a = [[1, 2], [3, 4]]
   b = a.copy()
   b[0].append(5)
   ```
   What are `a` and `b`?
10. How do you create a deep copy?
11. What happens here?
    ```python
    a = [1, 2, 3]
    b = a
    a = [4, 5]
    ```
    Does `b` change?
12. What is the difference between mutating an object and rebinding a name?

## 2. Function Arguments

13. What is wrong with this?
    ```python
    def add_item(item, items=[]):
        items.append(item)
        return items
    ```
14. What is the output?
    ```python
    def test(value=[]):
        value.append(1)
        return value

    print(test())
    print(test())
    print(test())
    ```
15. What is the recommended fix for the mutable default argument problem?
16. Are Python arguments passed by reference or by value?
17. What happens?
    ```python
    def change(x):
        x.append(4)

    a = [1, 2, 3]
    change(a)
    print(a)
    ```
18. What happens?
    ```python
    def change(x):
        x = [100]

    a = [1, 2, 3]
    change(a)
    print(a)
    ```
19. What are `*args` and `**kwargs`?
20. What does argument unpacking mean?
21. What is the difference between positional and keyword arguments?
22. What are keyword-only arguments?

## 3. Scope, LEGB & Closures

23. What is LEGB?
24. What happens?
    ```python
    x = 10

    def f():
        x = 20
        print(x)

    f()
    print(x)
    ```
25. What does the `global` keyword do?
26. What does `nonlocal` do?
27. What is a closure?

## 4. Lists

28. What is the difference between `append()` and `extend()`?
29. What does `list.insert(i, x)` do?
30. What is list slicing?
31. What happens when you mutate a list while iterating over it?
32. What happens?
    ```python
    x = [1, 2, 3]

    for i in x:
        x.append(i)
    ```
33. How would you safely modify a list while iterating?

## 5. Comprehensions

34. Convert this to a list comprehension:
    ```python
    result = []

    for x in range(10):
        if x % 2 == 0:
            result.append(x)
    ```
35. What is a dictionary comprehension?
36. What is a set comprehension?
37. When should you avoid an overly complex comprehension?

## 6. Iterables, Iterators & Generators

38. What is an iterable?
39. What is an iterator?
40. What does `iter(obj)` do?
41. What does `next(iterator)` do?
42. What is a generator?
43. What does `yield` do?
44. What is the difference between `return` and `yield`?
45. When does a generator function actually execute?
46. Why are generators useful?
47. Give real backend use cases for generators.
48. Do generators automatically make code faster?
49. What happens when a generator is exhausted?
50. What is a generator expression?

## 7. Decorators

51. What is a decorator?
52. Why are decorators useful?
53. How does the `@decorator` syntax work?
54. What is a wrapper function?
55. Why is `functools.wraps` useful?

## 8. Exceptions

56. What is an exception?
57. Difference between `try`, `except`, `else`, and `finally`?
58. What is the difference between `raise` and `return`?
59. How do you create a custom exception?
60. Why is catching `Exception` broadly sometimes dangerous?
61. What happens if an exception is not handled?

## 9. OOP

62. What is a class?
63. What is an object/instance?
64. What is `self`?
65. What is the difference between instance, class, and static methods?
66. What does `@classmethod` do?
67. What does `@staticmethod` do?
68. What is inheritance?
69. What is method overriding?
70. What does `super()` do?
71. What is polymorphism?
72. What is duck typing?

## 10. Class/Object Behaviour

73. What is `__init__`?
74. What is `__new__`?
75. What is a class attribute vs an instance attribute?
76. What is the danger of mutable class attributes?

## 11. Dunder Methods

77. What are dunder methods?
78. What is the difference between `__str__` and `__repr__`?
79. What does `__len__` allow?
80. What does `__eq__` control?

## 12. Hashing

81. What does hashable mean?
82. Why are mutable objects generally not hashable?
83. What is the relationship between `__eq__` and `__hash__`?

## 13. Memory Management

84. What is heap memory?
85. What is heap management?
86. Is heap management the same as a min-heap?
87. How does CPython manage memory at a high level?
88. What is reference counting?
89. What is a reference cycle?
90. Why does Python need cyclic garbage collection?
91. Does Python guarantee immediate memory return to the OS whenever an object is deleted?

## 14. Copy / Identity / Memory Traps

92. What does `id(obj)` represent?
93. What happens?
    ```python
    a = [1, 2]
    b = a
    c = a.copy()
    ```
    Which pairs are identical?
94. What is the difference between `copy.copy()` and `copy.deepcopy()`?

## 15. Strings

95. Are Python strings mutable?
96. What happens?
    ```python
    s = "hello"
    s[0] = "H"
    ```
97. Why can repeated string concatenation be inefficient?
98. What is string interning?

## 16. Boolean / Truthiness

99. What values are commonly falsy in Python?
100. Difference between:
     ```python
     if x:
     ```
     and
     ```python
     if x is not None:
     ```
101. Why can using `if value` be wrong when `0` is a valid value?

## 17. Conditionals / Expressions

102. What is a conditional expression?
103. What is short-circuit evaluation?

## 18. Loops / Iteration

104. What does `range(1, 9)` contain?
105. Difference between `break` and `continue`?
106. What does `pass` do?
107. What does `enumerate()` do?
108. What does `zip()` do?
109. What is the difference between `range` and `list(range(...))`?

## 19. Sorting

110. Difference between `sorted()` and `list.sort()`?
111. What is the `key` parameter in sorting?
112. What does `reverse=True` do?
113. Is Python sorting stable?

## 20. Heap Data Structure

114. What is a min-heap?
115. Is a heap a sorted array?
116. What is `heapq` in Python?
117. What are the typical complexities of a binary heap?

## 21. Modules / Imports

118. Difference between:
     ```python
     import module
     ```
     and
     ```python
     from module import name
     ```
119. What is `__name__ == "__main__"` used for?
120. What is a module?
121. What is a package?

## 22. Type Hints

122. What are type hints?
123. What is `Optional` / `| None` used for?
124. What is a `Protocol` / structural typing?

## 23. Dataclasses

125. What is a dataclass?
126. Why use a dataclass instead of writing `__init__` manually?

## 24. Performance / Complexity

127. What is the average complexity of:
    - `list.append`
    - list membership
    - dictionary lookup
    - set membership
128. Why is checking membership in a set generally faster than a list?
129. Why can inserting into the middle of a list be `O(n)`?
130. Why can deleting from the front of a list be `O(n)`?
131. What is amortized `O(1)`?

## 25. Pythonic Behaviour / Common Traps

132. What is the output?
    ```python
    a = [1, 2, 3]
    print(a * 2)
    ```
133. What is the difference between `list.copy()` and assigning the list directly?
134. What happens when you use `+=` with a list?
135. What is the difference between `None`, `False`, `0`, and an empty collection in a condition?

## 26. Async / Await

136. What is `async def`?
137. What does `await` do?
138. Is async automatically parallel?
139. When is async useful in backend applications?

## 27. Threads / Processes / GIL

140. Difference between a process and a thread?
141. What is the GIL in CPython?
142. Why can multiprocessing help CPU-bound Python work?

## 28. Testing / Debugging

143. What is the difference between a unit test and an integration test?
144. Why mock dependencies?
145. What is a regression test?

## 29. Backend-Relevant Python

146. Why should mutable global state generally be avoided?
147. Why can global variables be particularly problematic in web applications?
148. What is serialization?
149. What is deserialization?
150. Why should you be careful with `pickle`?
151. What is JSON's limitation compared with Python objects?

## 30. Rapid-Fire Output Questions

152. What is the output?
    ```python
    x = [1, 2]
    y = x
    y += [3]
    print(x)
    ```

153. What is the output?
    ```python
    x = [1, 2]
    y = x.copy()
    y += [3]
    print(x)
    print(y)
    ```

154. What is the output?
    ```python
    a = [1, 2, 3]
    print(a[-1])
    print(a[::-1])
    ```

155. What is the output?
    ```python
    d = {"a": 1}
    print(d.get("b"))
    ```

156. What happens?
    ```python
    d = {"a": 1}
    print(d["b"])
    ```

157. What is the output?
    ```python
    print(bool([]))
    print(bool([0]))
    ```

158. What is the output?
    ```python
    print("a" and "b")
    print("" and "b")
    print("a" or "b")
    print("" or "b")
    ```

159. What is the output?
    ```python
    x = [1, 2, 3]
    print(x is x)
    print(x == x)
    ```

## 31. Python Explanation Questions

160. Explain: **"Python is dynamically typed."**
161. Does Python have types?
162. What is duck typing?
163. Why is **"everything is an object"** useful to understand in Python?
164. What does **"first-class function"** mean?

## 32. Code From Scratch

165. Implement a function that reverses a string.
166. Implement a function that checks whether a string is a palindrome.
167. Count the frequency of each element in a list.
168. Remove duplicates from a list while preserving order.
169. Find the first non-repeating character in a string.
170. Group a list of words into anagram groups.
171. Merge two dictionaries.
172. Flatten a nested dictionary.
173. Flatten a nested list.
174. Implement your own generator that yields even numbers up to `N`.
175. Implement an iterator class with `__iter__` and `__next__`.
176. Write a decorator that logs a function call.
177. Write a decorator that measures execution time.
178. Implement a simple context manager.

## 33. "Why?" Follow-ups

179. Why is a dictionary lookup average `O(1)`?
180. Why is list membership `O(n)`?
181. Why is a set useful for duplicate detection?
182. Why is a mutable default argument dangerous?
183. Why does `yield` preserve the function's state?
184. Why can modifying a collection while iterating cause bugs?
185. Why doesn't `copy()` fully isolate nested mutable objects?
186. Why can't a list be a dictionary key?
187. Why does a generator save memory in the right use case?
188. Why doesn't a generator necessarily make computation faster?
189. Why does `is` not replace `==`?
190. Why can broad exception handling hide bugs?
191. Why can global mutable state be dangerous in backend services?

---

## Self-Test Rule

For now, do **not** look at the answers.

For each question, record:

`3 = know + can explain`

`2 = mostly know`

`1 = vaguely recognize`

`0 = don't know`

The goal is to identify your actual gaps before we review the answers.
