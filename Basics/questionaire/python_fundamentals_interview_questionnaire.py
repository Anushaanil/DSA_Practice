"""
PYTHON FUNDAMENTALS — INTERVIEW REVISION QUESTIONNAIRE
======================================================

Purpose:
    A practical Python fundamentals question bank for backend/SDE interviews.

How to use:
    1. Read only the question first.
    2. Answer aloud or write code without looking at the answer.
    3. Explain WHY, not just the output.
    4. Mark each question:
         3 = Can answer + explain + handle follow-up
         2 = Can answer but explanation is weak
         1 = Recognize it but cannot answer independently
         0 = Don't know
    5. Revisit 0/1 questions using spaced repetition.

Priority:
    P0 = Must know
    P1 = Important
    P2 = Useful follow-up / deeper interview question

NOTE:
    Some implementation details below are CPython-specific. Where that
    matters, it is explicitly called out.
"""


# ============================================================
# SECTION 1 — OBJECTS, REFERENCES, MUTABILITY
# ============================================================

# Q1 [P0]
# What is the difference between an object and a variable in Python?
#
# ANSWER:
# A variable is a name/reference bound to an object. The object is the
# actual value/data. Multiple variables can reference the same object.


# Q2 [P0]
# What happens here?
#
a = [1, 2, 3]
b = a
b.append(4)
print(a)
print(b)
#
# ANSWER:
# Both print [1, 2, 3, 4].
#
# WHY:
# a and b refer to the SAME list object. append() mutates that object.


# Q3 [P0]
# What is the difference between:
#
# a = b
# a = b.copy()
#
# ANSWER:
# a = b makes both names point to the same object.
# b.copy() creates a new outer list.


# Q4 [P0]
# What is the difference between == and is?
#
# ANSWER:
# == compares values/equality.
# is checks whether two references point to the same object.
#
# Example:
#
a = [1, 2]
b = [1, 2]
print(a == b)   # True
print(a is b)   # False


# Q5 [P0]
# What are mutable and immutable objects?
#
# ANSWER:
# Mutable objects can be changed after creation.
# Immutable objects cannot be changed after creation.
#
# Common mutable:
# list, dict, set, bytearray
#
# Common immutable:
# int, float, bool, str, tuple, frozenset, bytes


# Q6 [P0]
# Is a tuple always immutable?
#
# ANSWER:
# The tuple structure itself is immutable, but it can contain mutable objects.
#
t = ([1, 2], 3)
t[0].append(4)
print(t)
#
# ANSWER:
# ([1, 2, 4], 3)
#
# The tuple cannot replace t[0], but the list inside it can be mutated.


# Q7 [P0]
# What happens here?
#
a = [1, 2, 3]
b = a.copy()
b.append(4)
#
# ANSWER:
# a remains [1, 2, 3]; b becomes [1, 2, 3, 4].


# Q8 [P0]
# What is a shallow copy?
#
# ANSWER:
# A shallow copy creates a new outer container, but nested objects may
# still be shared.


# Q9 [P0]
# Demonstrate the shallow-copy problem.
#
a = [[1, 2], [3, 4]]
b = a.copy()
b[0].append(5)
#
# What are a and b?
#
# ANSWER:
# a = [[1, 2, 5], [3, 4]]
# b = [[1, 2, 5], [3, 4]]
#
# The nested list is shared.


# Q10 [P1]
# How do you create a deep copy?
#
# ANSWER:
#
# import copy
# b = copy.deepcopy(a)
#
# Deep copy recursively copies nested objects where applicable.


# Q11 [P0]
# What happens when you do:
#
a = [1, 2, 3]
b = a
a = [4, 5]
#
# Does b change?
#
# ANSWER:
# No.
# Initially a and b reference the same list.
# Then a is rebound to a new list.
# b still points to the original [1, 2, 3].


# Q12 [P0]
# What is the difference between mutating an object and rebinding a name?
#
# ANSWER:
# Mutation changes the existing object.
# Rebinding makes a variable reference a different object.
#
# Mutation:
# a.append(4)
#
# Rebinding:
# a = [4]


# ============================================================
# SECTION 2 — FUNCTION ARGUMENTS
# ============================================================

# Q13 [P0]
# What is wrong with this?
#
def add_item(item, items=[]):
    items.append(item)
    return items
#
# ANSWER:
# The default list is created once when the function is defined and is
# reused across calls that omit items.


# Q14 [P0]
# What is the output?
#
def test(value=[]):
    value.append(1)
    return value
#
# print(test())
# print(test())
# print(test())
#
# ANSWER:
# [1]
# [1, 1]
# [1, 1, 1]


# Q15 [P0]
# What is the recommended fix?
#
# ANSWER:
#
# def test(value=None):
#     if value is None:
#         value = []
#     value.append(1)
#     return value


# Q16 [P0]
# Are Python arguments passed by reference or by value?
#
# ANSWER:
# The most useful precise explanation is:
# Python uses call-by-sharing/object-reference semantics.
# The function receives a reference to the same object.
# Rebinding the parameter does not rebind the caller's variable, but
# mutating the shared mutable object is visible to the caller.


# Q17 [P0]
# What happens?
#
def change(x):
    x.append(4)
#
a = [1, 2, 3]
change(a)
print(a)
#
# ANSWER:
# [1, 2, 3, 4]
#
# The function mutates the same list object.


# Q18 [P0]
# What happens?
#
def change(x):
    x = [100]
#
a = [1, 2, 3]
change(a)
print(a)
#
# ANSWER:
# [1, 2, 3]
#
# x is only rebound locally.


# Q19 [P1]
# What are *args and **kwargs?
#
# ANSWER:
# *args collects extra positional arguments into a tuple.
# **kwargs collects extra keyword arguments into a dictionary.


# Q20 [P1]
# What does argument unpacking mean?
#
# ANSWER:
#
# args = [1, 2, 3]
# func(*args)
#
# passes the list elements as separate positional arguments.
#
# kwargs = {"name": "Anusha", "age": 25}
# func(**kwargs)
#
# passes dictionary entries as keyword arguments.


# Q21 [P1]
# What is the difference between positional and keyword arguments?
#
# ANSWER:
# Positional arguments are matched by position.
# Keyword arguments are matched by parameter name.


# Q22 [P1]
# What are keyword-only arguments?
#
# ANSWER:
#
# def create_user(name, *, is_active=True):
#     ...
#
# is_active must be supplied as a keyword.


# ============================================================
# SECTION 3 — SCOPE, LEGB, CLOSURES
# ============================================================

# Q23 [P0]
# What is LEGB?
#
# ANSWER:
# Python searches names in:
# Local -> Enclosing -> Global -> Built-in


# Q24 [P0]
# What happens?
#
x = 10
#
def f():
    x = 20
    print(x)
#
# f()
# print(x)
#
# ANSWER:
# 20
# 10
#
# The local x shadows the global x.


# Q25 [P1]
# What does the global keyword do?
#
# ANSWER:
# It allows a function to rebind a variable from the module/global scope.


# Q26 [P1]
# What does nonlocal do?
#
# ANSWER:
# It allows an inner function to rebind a variable from its enclosing
# function scope.


# Q27 [P1]
# What is a closure?
#
# ANSWER:
# A closure is an inner function that retains access to variables from
# its enclosing scope even after the enclosing function has returned.


# Q28 [P1]
# Explain the late-binding closure problem.
#
funcs = []
for i in range(3):
    funcs.append(lambda: i)
#
# What happens if you call all three?
#
# ANSWER:
# They all typically return 2.
# The lambdas look up i when they execute, not when they are created.
#
# Common fix:
# funcs.append(lambda i=i: i)


# ============================================================
# SECTION 4 — LISTS, DICTS, SETS, TUPLES
# ============================================================

# Q29 [P0]
# Difference between list, tuple, set and dict?
#
# ANSWER:
# list  -> ordered mutable sequence
# tuple -> ordered immutable sequence
# set   -> collection of unique hashable elements
# dict  -> key-value mapping with hashable keys


# Q30 [P0]
# Why can't a list normally be used as a dictionary key?
#
# ANSWER:
# Dictionary keys must be hashable.
# Lists are mutable and therefore unhashable.


# Q31 [P0]
# Can a tuple be a dictionary key?
#
# ANSWER:
# Yes, if all elements contained in the tuple are hashable.


# Q32 [P0]
# What is the average complexity of dictionary lookup?
#
# ANSWER:
# Average O(1), because dictionaries use hash-table-based lookup.
# Worst-case behavior can degrade because of collisions.


# Q33 [P0]
# What is the average complexity of set membership?
#
# ANSWER:
# Average O(1).


# Q34 [P1]
# What is the difference between remove(), pop(), and del?
#
# ANSWER:
# remove(value) removes the first matching value.
# pop(index) removes and returns an element.
# del removes a variable, slice, or indexed item.


# Q35 [P1]
# What is the difference between append() and extend()?
#
# ANSWER:
#
# a = [1, 2]
# a.append([3, 4])
# -> [1, 2, [3, 4]]
#
# a = [1, 2]
# a.extend([3, 4])
# -> [1, 2, 3, 4]


# Q36 [P1]
# What does list.insert(i, x) do?
#
# ANSWER:
# Inserts x before index i.
# It may require shifting later elements, so it is generally O(n).


# Q37 [P1]
# What is list slicing?
#
# ANSWER:
# a[start:stop:step]
# start is inclusive, stop is exclusive.


# Q38 [P0]
# What happens when you mutate a list while iterating over it?
#
# ANSWER:
# Behavior depends on the mutation, but it can cause skipped elements,
# repeated processing, or non-termination.
# Do not assume the loop iterates over an immutable snapshot.


# Q39 [P0]
# What happens?
#
x = [1, 2, 3]
# for i in x:
#     x.append(i)
#
# ANSWER:
# The list keeps growing while the iterator continues finding appended
# elements, so this can become an infinite loop.


# Q40 [P1]
# How would you safely modify a list while iterating?
#
# ANSWER:
# Common approaches:
# - iterate over a copy: for x in items.copy()
# - build a new list
# - iterate backwards for certain deletion problems
# - use a list comprehension where appropriate


# ============================================================
# SECTION 5 — COMPREHENSIONS
# ============================================================

# Q41 [P0]
# Convert this to a list comprehension:
#
result = []
for x in range(10):
    if x % 2 == 0:
        result.append(x)
#
# ANSWER:
# result = [x for x in range(10) if x % 2 == 0]


# Q42 [P1]
# What is a dictionary comprehension?
#
# ANSWER:
#
# squares = {x: x * x for x in range(5)}


# Q43 [P1]
# What is a set comprehension?
#
# ANSWER:
#
# unique = {x % 3 for x in range(10)}


# Q44 [P1]
# When should you avoid an overly complex comprehension?
#
# ANSWER:
# When readability becomes worse than an ordinary loop.
# Interview code should be clear, not merely concise.


# ============================================================
# SECTION 6 — ITERABLES, ITERATORS, GENERATORS
# ============================================================

# Q45 [P0]
# What is an iterable?
#
# ANSWER:
# An object that can provide an iterator, typically via __iter__().
# Examples: list, tuple, string, dict, set.


# Q46 [P0]
# What is an iterator?
#
# ANSWER:
# An object that implements __iter__() and __next__() and maintains
# iteration state.


# Q47 [P0]
# What does iter(obj) do?
#
# ANSWER:
# It obtains an iterator from an iterable.


# Q48 [P0]
# What does next(iterator) do?
#
# ANSWER:
# It asks the iterator for its next value.
# When there are no more values, StopIteration is raised.


# Q49 [P0]
# What is a generator?
#
# ANSWER:
# A generator is a lazy iterator created by a generator function
# containing yield or by a generator expression.


# Q50 [P0]
# What does yield do?
#
# ANSWER:
# yield produces a value and pauses the generator's execution.
# Its state is preserved so that the next call resumes from that point.


# Q51 [P0]
# Difference between return and yield?
#
# ANSWER:
# return ends the function and gives back a result.
# yield produces a value and pauses a generator so it can resume later.


# Q52 [P0]
# When does a generator function actually execute?
#
# ANSWER:
# Calling the generator function creates a generator object.
# Its body begins executing when next() is called or when iteration starts.


# Q53 [P1]
# Why are generators useful?
#
# ANSWER:
# They allow lazy, incremental processing and avoid materializing an
# entire potentially large sequence at once.


# Q54 [P1]
# Give real backend use cases for generators.
#
# ANSWER:
# - Streaming/processing large files
# - Incremental record processing
# - Data pipelines
# - Large database result processing
# - Potentially infinite sequences


# Q55 [P1]
# Do generators automatically make code faster?
#
# ANSWER:
# No.
# Their main advantage is lazy evaluation and reduced materialization/
# memory usage. They can even add some execution overhead.


# Q56 [P1]
# What happens when a generator is exhausted?
#
# ANSWER:
# next() raises StopIteration.
# A for loop catches this internally and terminates.


# Q57 [P1]
# What is a generator expression?
#
# ANSWER:
#
# g = (x * x for x in range(10))
#
# It creates a generator lazily instead of a list.


# ============================================================
# SECTION 7 — DECORATORS
# ============================================================

# Q58 [P0]
# What is a decorator?
#
# ANSWER:
# A decorator is a callable that takes a function/class and returns
# a modified or wrapped version of it.
#
# Syntax:
#
# @decorator
# def func():
#     ...


# Q59 [P0]
# What does @decorator do conceptually?
#
# ANSWER:
#
# @decorator
# def func():
#     pass
#
# is roughly:
#
# def func():
#     pass
# func = decorator(func)


# Q60 [P1]
# Write a simple decorator that prints before and after a function call.
#
# ANSWER:
#
# def log_call(func):
#     def wrapper(*args, **kwargs):
#         print("Before")
#         result = func(*args, **kwargs)
#         print("After")
#         return result
#     return wrapper


# Q61 [P1]
# Why is functools.wraps useful in decorators?
#
# ANSWER:
# It preserves useful metadata such as __name__ and __doc__ from the
# wrapped function.


# Q62 [P1]
# Where are decorators used in Django?
#
# ANSWER:
# Examples include authentication/authorization decorators and other
# cross-cutting concerns. Django and DRF also provide decorator-based
# mechanisms around views and behavior.


# ============================================================
# SECTION 8 — EXCEPTIONS
# ============================================================

# Q63 [P0]
# Explain try/except/else/finally.
#
# ANSWER:
# try    -> code that may raise
# except -> handles matching exceptions
# else   -> runs if no exception occurred
# finally -> runs whether or not an exception occurred


# Q64 [P0]
# Difference between raise and return?
#
# ANSWER:
# return gives a value/control back to the caller.
# raise signals an exception and changes normal control flow.


# Q65 [P1]
# Why should you avoid bare except?
#
# ANSWER:
# It catches almost everything, including exceptions you may not intend
# to handle, making debugging and error handling harder.


# Q66 [P1]
# Should you catch Exception everywhere?
#
# ANSWER:
# No.
# Catch exceptions where you can meaningfully handle them.
# Broad catching can hide programming bugs.


# Q67 [P1]
# How do you create a custom exception?
#
# ANSWER:
#
# class InvalidUserError(Exception):
#     pass


# ============================================================
# SECTION 9 — CONTEXT MANAGERS
# ============================================================

# Q68 [P0]
# What is a context manager?
#
# ANSWER:
# An object that manages setup and cleanup around a block of code,
# commonly used with the with statement.


# Q69 [P0]
# Why use with open(...)?
#
# ANSWER:
# It ensures the file is properly closed even if an exception occurs.


# Q70 [P1]
# What are __enter__ and __exit__?
#
# ANSWER:
# They are the core methods used by a class implementing the context
# manager protocol.


# Q71 [P1]
# How would you create a simple context manager?
#
# ANSWER:
#
# class Resource:
#     def __enter__(self):
#         # acquire
#         return self
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         # cleanup
#         pass


# ============================================================
# SECTION 10 — OOP
# ============================================================

# Q72 [P0]
# What are the main principles commonly associated with OOP?
#
# ANSWER:
# Encapsulation, abstraction, inheritance, polymorphism.


# Q73 [P0]
# What is self?
#
# ANSWER:
# self is the conventional name for the instance passed to an instance
# method. It refers to the current object.


# Q74 [P0]
# Difference between instance, class, static methods?
#
# ANSWER:
# Instance method -> receives self.
# Class method    -> receives cls and can operate on the class.
# Static method   -> receives neither automatically; behaves like a
#                    function namespaced inside the class.


# Q75 [P0]
# What does @classmethod do?
#
# ANSWER:
# It creates a method that receives the class as its first argument.


# Q76 [P0]
# What does @staticmethod do?
#
# ANSWER:
# It creates a method that does not receive self or cls automatically.


# Q77 [P1]
# What is inheritance?
#
# ANSWER:
# A class derives behavior/attributes from another class.


# Q78 [P1]
# What is method overriding?
#
# ANSWER:
# A subclass provides its own implementation of a method defined in
# a parent class.


# Q79 [P1]
# What does super() do?
#
# ANSWER:
# It provides a way to access behavior from a parent/superclass,
# commonly to call a parent implementation.


# Q80 [P1]
# What is polymorphism?
#
# ANSWER:
# Different objects can provide the same interface/operation while
# implementing it differently.


# Q81 [P1]
# What is duck typing?
#
# ANSWER:
# Python often cares about what an object can do rather than its exact
# type: "if it behaves like the required object, use it."


# ============================================================
# SECTION 11 — CLASS / OBJECT BEHAVIOR
# ============================================================

# Q82 [P1]
# What is __init__?
#
# ANSWER:
# It initializes an instance after the instance has been created.
# Strictly speaking, __new__ is responsible for creating the instance.


# Q83 [P1]
# What is __new__?
#
# ANSWER:
# It is responsible for creating/returning a new instance and runs
# before __init__.


# Q84 [P1]
# What is a class attribute vs instance attribute?
#
# ANSWER:
# A class attribute belongs to the class and can be shared.
# An instance attribute belongs to a particular object.


# Q85 [P1]
# What is the danger of mutable class attributes?
#
# ANSWER:
# A mutable class attribute can accidentally be shared across all
# instances unless an instance-specific value is created.


# ============================================================
# SECTION 12 — SPECIAL / DUNDER METHODS
# ============================================================

# Q86 [P1]
# What are dunder methods?
#
# ANSWER:
# Special methods with names such as __init__, __str__, __len__,
# __eq__, __iter__, __next__, etc. They define how objects interact
# with Python's protocols and operators.


# Q87 [P1]
# Difference between __str__ and __repr__?
#
# ANSWER:
# __str__ is intended for a user-friendly representation.
# __repr__ is intended to be a more developer-oriented/unambiguous
# representation.


# Q88 [P1]
# What does __len__ allow?
#
# ANSWER:
# It allows len(obj) to obtain the object's length through the
# corresponding protocol.


# Q89 [P1]
# What does __eq__ control?
#
# ANSWER:
# It defines equality behavior for ==.


# ============================================================
# SECTION 13 — HASHING
# ============================================================

# Q90 [P0]
# What does hashable mean?
#
# ANSWER:
# An object is hashable if it has a hash value that remains stable
# during its lifetime and can participate in hash-based collections
# such as dict keys and set elements.


# Q91 [P0]
# Why must dictionary keys be hashable?
#
# ANSWER:
# Dictionaries use hashing to locate keys efficiently.


# Q92 [P1]
# Why are mutable objects generally not hashable?
#
# ANSWER:
# If an object's value affecting its hash changed while stored in a
# hash table, its lookup location could become inconsistent.


# Q93 [P1]
# What is the relationship between __eq__ and __hash__?
#
# ANSWER:
# Equal objects must have equal hashes when both are hashable.
# Custom implementations need to preserve that contract.


# ============================================================
# SECTION 14 — MEMORY MANAGEMENT / GARBAGE COLLECTION
# ============================================================

# Q94 [P0]
# What is heap memory?
#
# ANSWER:
# It is memory managed dynamically during program execution, where
# objects can be allocated and live beyond a single stack frame.


# Q95 [P0]
# What is heap management?
#
# ANSWER:
# The process of allocating, tracking, and reclaiming dynamically
# managed memory.


# Q96 [P0]
# Is heap management the same as a min-heap?
#
# ANSWER:
# No.
# Heap memory management is about runtime memory.
# A min-heap is a data structure.


# Q97 [P0]
# How does CPython manage memory at a high level?
#
# ANSWER:
# CPython uses its own memory allocator and primarily uses reference
# counting for object lifetime, along with cyclic garbage collection
# for reference cycles.


# Q98 [P0]
# What is reference counting?
#
# ANSWER:
# A mechanism that tracks references to objects. In CPython, when an
# object's reference count reaches zero, it can generally be deallocated.


# Q99 [P1]
# What is a reference cycle?
#
# ANSWER:
# Objects reference each other in a cycle, so simple reference counting
# alone cannot identify them as unreachable.


# Q100 [P1]
# Why does Python need cyclic garbage collection?
#
# ANSWER:
# To detect and handle unreachable reference cycles that reference
# counting alone cannot reclaim.


# Q101 [P1]
# Does Python guarantee immediate memory return to the OS whenever an
# object is deleted?
#
# ANSWER:
# No.
# Object lifetime/deallocation and returning memory to the operating
# system are separate concepts. The runtime allocator may retain memory
# for reuse.


# ============================================================
# SECTION 15 — COPY / IDENTITY / MEMORY TRAPS
# ============================================================

# Q102 [P0]
# What does id(obj) represent?
#
# ANSWER:
# It returns an integer identifying the object for its lifetime.
# In CPython it is commonly related to the object's memory address,
# but code should not rely on that implementation detail.


# Q103 [P1]
# What happens?
#
a = [1, 2]
b = a
c = a.copy()
#
# Which pairs are identical?
#
# ANSWER:
# a is b -> True
# a is c -> False
# b is c -> False


# Q104 [P1]
# What is the difference between copy.copy and copy.deepcopy?
#
# ANSWER:
# copy.copy creates a shallow copy.
# copy.deepcopy recursively copies nested objects where possible.


# ============================================================
# SECTION 16 — STRINGS
# ============================================================

# Q105 [P0]
# Are Python strings mutable?
#
# ANSWER:
# No. Strings are immutable.


# Q106 [P0]
# What happens here?
#
s = "hello"
# s[0] = "H"
#
# ANSWER:
# TypeError. Strings cannot be modified in place.


# Q107 [P1]
# Why can repeated string concatenation be inefficient?
#
# ANSWER:
# Because strings are immutable; repeated concatenation can create
# multiple intermediate string objects.
#
# For many pieces, collecting them and using "".join(parts) is commonly
# more appropriate.


# Q108 [P1]
# What is string interning?
#
# ANSWER:
# An optimization where some identical immutable strings may be reused.
# Do not use is to compare string values; use ==.


# ============================================================
# SECTION 17 — BOOLEAN / TRUTHINESS
# ============================================================

# Q109 [P0]
# What values are commonly falsy in Python?
#
# ANSWER:
# False, None, 0, 0.0, "", empty collections such as [], {}, set(),
# and objects whose __bool__/__len__ indicate false.


# Q110 [P1]
# Difference between:
#
# if x:
# if x is not None:
#
# ANSWER:
# if x checks truthiness.
# if x is not None checks specifically whether x is not None.
#
# They are NOT equivalent.


# Q111 [P1]
# Why can using `if value` be wrong when 0 is a valid value?
#
# ANSWER:
# Because 0 is falsy. If 0 is a meaningful value, explicitly check
# against None when that is the intended condition.


# ============================================================
# SECTION 18 — CONDITIONALS / EXPRESSIONS
# ============================================================

# Q112 [P1]
# What is a conditional expression?
#
# ANSWER:
# value_if_true if condition else value_if_false


# Q113 [P1]
# What is short-circuit evaluation?
#
# ANSWER:
# Python may stop evaluating an expression once the result is known.
#
# False and expensive_function()
# does not call expensive_function().
#
# True or expensive_function()
# also does not call it.


# Q114 [P1]
# What is the difference between `and` / `or` and boolean-only operators?
#
# ANSWER:
# Python's and/or return one of their operands, not necessarily True/False.
#
# Example:
# "hello" or "world" -> "hello"
# "" or "world"     -> "world"


# ============================================================
# SECTION 19 — LOOPS / ITERATION
# ============================================================

# Q115 [P0]
# What does range(1, 9) contain?
#
# ANSWER:
# 1 through 8. The stop value is excluded.


# Q116 [P0]
# Difference between break and continue?
#
# ANSWER:
# break exits the loop.
# continue skips the current iteration and proceeds to the next.


# Q117 [P1]
# What does pass do?
#
# ANSWER:
# It does nothing; it is a syntactic placeholder.


# Q118 [P1]
# What does enumerate() do?
#
# ANSWER:
# It provides index/value pairs while iterating.
#
# for index, value in enumerate(items):
#     ...


# Q119 [P1]
# What does zip() do?
#
# ANSWER:
# It combines iterables element-by-element and produces tuples.
# By default, it stops when the shortest iterable is exhausted.


# Q120 [P1]
# What is the difference between range and list(range(...))?
#
# ANSWER:
# range is a lazy range object representing the sequence.
# list(range(...)) materializes all values into a list.


# ============================================================
# SECTION 20 — SORTING
# ============================================================

# Q121 [P0]
# Difference between sorted() and list.sort()?
#
# ANSWER:
# sorted(iterable) returns a new sorted list.
# list.sort() sorts the list in place and returns None.


# Q122 [P0]
# What is the key parameter in sorting?
#
# ANSWER:
# It specifies a function used to determine the sorting key.
#
# users.sort(key=lambda u: u.name)


# Q123 [P1]
# What does reverse=True do?
#
# ANSWER:
# It sorts in descending order.


# Q124 [P1]
# Is Python sorting stable?
#
# ANSWER:
# Yes. Python's sort is stable: equal-key elements preserve their
# relative order.


# ============================================================
# SECTION 21 — HEAP DATA STRUCTURE
# ============================================================

# Q125 [P1]
# What is a min-heap?
#
# ANSWER:
# A complete binary tree where each parent is <= its children.
# The minimum element is at the root.


# Q126 [P1]
# Is a heap a sorted array?
#
# ANSWER:
# No. A heap only guarantees the heap property.


# Q127 [P1]
# What is heapq in Python?
#
# ANSWER:
# Python's heapq module provides a min-heap implementation.


# Q128 [P1]
# Typical complexities of a binary heap?
#
# ANSWER:
# Peek minimum -> O(1)
# Push        -> O(log n)
# Pop minimum -> O(log n)
# Heapify     -> O(n)


# ============================================================
# SECTION 22 — MODULES / IMPORTS
# ============================================================

# Q129 [P0]
# Difference between:
#
# import module
# from module import name
#
# ANSWER:
# import module imports the module and accesses names through module.name.
# from module import name imports that name directly into the namespace.


# Q130 [P1]
# What is __name__ == "__main__" used for?
#
# ANSWER:
# It allows code to run when the file is executed directly but not when
# the file is imported as a module.


# Q131 [P1]
# What is a module?
#
# ANSWER:
# A Python file containing definitions/statements that can be imported.


# Q132 [P1]
# What is a package?
#
# ANSWER:
# A way to organize related Python modules into a package namespace.
# Modern Python packages can be regular packages or namespace packages.


# ============================================================
# SECTION 23 — TYPE HINTS
# ============================================================

# Q133 [P1]
# What are type hints?
#
# ANSWER:
# Annotations that describe expected types. Python generally does not
# enforce them at runtime by default.
#
# def add(a: int, b: int) -> int:
#     return a + b


# Q134 [P1]
# What is Optional / | None used for?
#
# ANSWER:
# It expresses that a value may be of a type or None.
#
# name: str | None


# Q135 [P2]
# What is a Protocol / structural typing?
#
# ANSWER:
# It can describe an expected interface based on available methods/
# attributes rather than requiring a specific inheritance hierarchy.


# ============================================================
# SECTION 24 — DATACLASSES
# ============================================================

# Q136 [P1]
# What is a dataclass?
#
# ANSWER:
# A utility that reduces boilerplate for classes primarily used to
# represent data. It can generate methods such as __init__, __repr__,
# and comparisons depending on configuration.


# Q137 [P1]
# Why use dataclass instead of writing __init__ manually?
#
# ANSWER:
# When the class mainly stores data, dataclass can generate common
# boilerplate and make the intent clearer.


# ============================================================
# SECTION 25 — PERFORMANCE / COMPLEXITY
# ============================================================

# Q138 [P0]
# Average complexity of:
#
# list append
# list membership
# dict lookup
# set membership
#
# ANSWER:
# list.append -> amortized O(1)
# x in list   -> O(n)
# dict lookup -> average O(1)
# set lookup  -> average O(1)


# Q139 [P0]
# Why is checking membership in a set generally faster than a list?
#
# ANSWER:
# Sets use hash-based lookup with average O(1) membership.
# Lists require scanning elements and are O(n) in the average/general case.


# Q140 [P1]
# Why can inserting into the middle of a list be O(n)?
#
# ANSWER:
# Elements after the insertion position may need to be shifted.


# Q141 [P1]
# Why can deleting from the front of a list be O(n)?
#
# ANSWER:
# Remaining elements may need to be shifted.


# Q142 [P1]
# What is amortized O(1)?
#
# ANSWER:
# An operation may occasionally be expensive, but averaged across a
# sequence of operations, the cost per operation is O(1).
# list.append is a common example because resizing occasionally requires
# allocating/copying storage.


# ============================================================
# SECTION 26 — PYTHONIC BEHAVIOR / COMMON TRAPS
# ============================================================

# Q143 [P0]
# What is the output?
#
a = [1, 2, 3]
# print(a * 2)
#
# ANSWER:
# [1, 2, 3, 1, 2, 3]
#
# It repeats the list; it does not multiply individual elements.


# Q144 [P1]
# What happens?
#
a = [[0] * 3] * 3
a[0][0] = 1
#
# ANSWER:
# All rows' first elements can change because the same inner list is
# repeated by reference.
#
# Result:
# [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
#
# Safer:
# [[0] * 3 for _ in range(3)]


# Q145 [P1]
# What is the difference between `x += y` and `x = x + y` for mutable
# objects?
#
# ANSWER:
# They can differ because += may perform in-place mutation when supported,
# while x = x + y generally creates/rebinds to a new object.


# Q146 [P1]
# What does dict.get(key, default) do?
#
# ANSWER:
# Returns the value for key if present; otherwise returns the supplied
# default instead of raising KeyError.


# Q147 [P1]
# Difference between d[key] and d.get(key)?
#
# ANSWER:
# d[key] raises KeyError if key is missing.
# d.get(key) returns None by default if key is missing.


# Q148 [P1]
# What does setdefault() do?
#
# ANSWER:
# If the key exists, it returns its value.
# If absent, it inserts the default and returns it.
#
# Be careful: it can mutate the dictionary.


# ============================================================
# SECTION 27 — PROPERTY / DESCRIPTOR BASICS
# ============================================================

# Q149 [P2]
# What does @property do?
#
# ANSWER:
# It allows a method to be accessed like an attribute.
#
# @property
# def full_name(self):
#     return f"{self.first} {self.last}"


# Q150 [P2]
# What is a descriptor?
#
# ANSWER:
# An object implementing methods such as __get__, __set__, or __delete__
# that controls attribute access. Descriptors are an important mechanism
# behind properties and several Python frameworks.


# ============================================================
# SECTION 28 — ASYNC BASICS
# ============================================================

# Q151 [P1]
# What is async def?
#
# ANSWER:
# It defines a coroutine function.


# Q152 [P1]
# What does await do?
#
# ANSWER:
# It suspends the current coroutine until the awaited awaitable completes,
# allowing the event loop to run other work.


# Q153 [P1]
# Is async automatically parallel?
#
# ANSWER:
# No.
# Async primarily provides cooperative concurrency. CPU-bound work does
# not automatically become parallel just because it is async.


# Q154 [P1]
# When is async useful in backend applications?
#
# ANSWER:
# Especially for I/O-bound workloads where the program spends time waiting
# for network/database/external-service operations and can use that time
# to progress other tasks.


# ============================================================
# SECTION 29 — THREADS / PROCESSES / GIL
# ============================================================

# Q155 [P1]
# Difference between process and thread?
#
# ANSWER:
# Processes have separate memory spaces and are heavier to create/manage.
# Threads share a process's memory and are lighter but require care with
# shared state.


# Q156 [P1]
# What is the GIL in CPython?
#
# ANSWER:
# The Global Interpreter Lock allows only one thread at a time to execute
# Python bytecode in a CPython interpreter process under the traditional
# GIL model.
#
# It does not mean threads are useless; threads can still be useful for
# I/O-bound work and C extensions may release the GIL.


# Q157 [P1]
# Why can multiprocessing help CPU-bound Python work?
#
# ANSWER:
# Separate processes can execute Python code in separate interpreter
# processes, allowing CPU work to use multiple cores without sharing the
# same GIL.


# ============================================================
# SECTION 30 — TESTING / DEBUGGING BASICS
# ============================================================

# Q158 [P1]
# What is the difference between a unit test and an integration test?
#
# ANSWER:
# Unit tests focus on a small isolated unit.
# Integration tests verify interaction between components such as a
# database, service, API, or external dependency.


# Q159 [P1]
# Why mock dependencies?
#
# ANSWER:
# To isolate the code under test and make tests deterministic and faster,
# especially when interacting with external services.


# Q160 [P1]
# What is a regression test?
#
# ANSWER:
# A test that helps ensure a previously fixed/working behavior does not
# break after future changes.


# ============================================================
# SECTION 31 — BACKEND-RELEVANT PYTHON QUESTIONS
# ============================================================

# Q161 [P0]
# Why should mutable global state generally be avoided?
#
# ANSWER:
# It can create hidden coupling, concurrency issues, difficult-to-test
# behavior, and unexpected state shared across requests.


# Q162 [P1]
# Why can global variables be particularly problematic in web applications?
#
# ANSWER:
# A web process may serve many requests, and global mutable state can be
# shared across requests within a process. With multiple workers/processes,
# state may also differ between workers.


# Q163 [P1]
# What is serialization?
#
# ANSWER:
# Converting an in-memory object/data structure into a representation that
# can be stored or transmitted, such as JSON or bytes.


# Q164 [P1]
# What is deserialization?
#
# ANSWER:
# Reconstructing data/object representation from a serialized format.


# Q165 [P1]
# Why should you be careful with pickle?
#
# ANSWER:
# Unpickling untrusted data can execute arbitrary code. Never treat
# untrusted pickle data as safe input.


# Q166 [P1]
# What is JSON's limitation compared with Python objects?
#
# ANSWER:
# JSON supports a limited set of data types and does not directly preserve
# arbitrary Python object types or behavior.


# ============================================================
# SECTION 32 — RAPID-FIRE OUTPUT QUESTIONS
# ============================================================

# Q167 [P0]
# What is the output?
#
x = [1, 2]
y = x
y += [3]
print(x)
#
# ANSWER:
# [1, 2, 3]
#
# The list is mutated in place for this operation.


# Q168 [P0]
# What is the output?
#
x = [1, 2]
y = x.copy()
y += [3]
print(x)
print(y)
#
# ANSWER:
# [1, 2]
# [1, 2, 3]


# Q169 [P0]
# What is the output?
#
a = [1, 2, 3]
print(a[-1])
print(a[::-1])
#
# ANSWER:
# 3
# [3, 2, 1]


# Q170 [P0]
# What is the output?
#
d = {"a": 1}
print(d.get("b"))
#
# ANSWER:
# None


# Q171 [P0]
# What is the output?
#
d = {"a": 1}
# print(d["b"])
#
# ANSWER:
# KeyError


# Q172 [P0]
# What is the output?
#
print(bool([]))
print(bool([0]))
#
# ANSWER:
# False
# True
#
# A non-empty list is truthy even if its element is 0.


# Q173 [P1]
# What is the output?
#
print("a" and "b")
print("" and "b")
print("a" or "b")
print("" or "b")
#
# ANSWER:
# b
# ""
# a
# b


# Q174 [P1]
# What is the output?
#
x = [1, 2, 3]
print(x is x)
print(x == x)
#
# ANSWER:
# True
# True


# ============================================================
# SECTION 33 — INTERVIEW EXPLANATION QUESTIONS
# ============================================================

# Q175 [P0]
# Explain "Python is dynamically typed."
#
# ANSWER:
# Names do not have fixed declared types in the way statically typed
# languages commonly do. Objects have types, and a name can be rebound
# to objects of different types.


# Q176 [P0]
# Does Python have types?
#
# ANSWER:
# Yes. Python is dynamically typed, not untyped. Objects have runtime
# types.


# Q177 [P0]
# What is duck typing?
#
# ANSWER:
# Code can often operate on an object based on the methods/behavior it
# provides rather than requiring a specific class.


# Q178 [P0]
# Why is "everything is an object" useful to understand in Python?
#
# ANSWER:
# Functions, classes, numbers, strings, collections, etc. are objects
# with identity, type, and behavior. This explains first-class functions,
# passing functions as arguments, references, and many Python protocols.


# Q179 [P1]
# What does "first-class function" mean?
#
# ANSWER:
# Functions can be assigned to variables, passed as arguments, returned
# from functions, and stored in collections.


# ============================================================
# SECTION 34 — QUESTIONS YOU SHOULD BE ABLE TO CODE FROM SCRATCH
# ============================================================

# Q180 [P0]
# Implement a function that reverses a string.


# Q181 [P0]
# Implement a function that checks whether a string is a palindrome.


# Q182 [P0]
# Count the frequency of each element in a list.


# Q183 [P0]
# Remove duplicates from a list while preserving order.


# Q184 [P0]
# Find the first non-repeating character in a string.


# Q185 [P0]
# Group a list of words into anagram groups.


# Q186 [P0]
# Merge two dictionaries.


# Q187 [P1]
# Flatten a nested dictionary.


# Q188 [P1]
# Flatten a nested list.


# Q189 [P1]
# Implement your own generator that yields even numbers up to N.


# Q190 [P1]
# Implement an iterator class with __iter__ and __next__.


# Q191 [P1]
# Write a decorator that logs a function call.


# Q192 [P1]
# Write a decorator that measures execution time.


# Q193 [P1]
# Implement a simple context manager.


# ============================================================
# SECTION 35 — "WHY?" FOLLOW-UP QUESTIONS
# ============================================================

# Q194 [P0]
# Why is a dictionary lookup average O(1)?


# Q195 [P0]
# Why is list membership O(n)?


# Q196 [P0]
# Why is a set useful for duplicate detection?


# Q197 [P0]
# Why is a mutable default argument dangerous?


# Q198 [P0]
# Why does yield preserve the function's state?


# Q199 [P0]
# Why can modifying a collection while iterating cause bugs?


# Q200 [P0]
# Why doesn't copy() fully isolate nested mutable objects?


# Q201 [P0]
# Why can't a list be a dictionary key?


# Q202 [P0]
# Why does a generator save memory in the right use case?


# Q203 [P0]
# Why doesn't a generator necessarily make computation faster?


# Q204 [P0]
# Why does `is` not replace `==`?


# Q205 [P1]
# Why can broad exception handling hide bugs?


# Q206 [P1]
# Why can global mutable state be dangerous in backend services?


# ============================================================
# FINAL INTERVIEW CHECKLIST
# ============================================================

# Before an interview, you should be able to answer these without notes:
#
# 1. Mutable vs immutable
# 2. Object vs reference
# 3. == vs is
# 4. Shallow vs deep copy
# 5. Mutable default arguments
# 6. Python argument passing
# 7. *args / **kwargs
# 8. LEGB
# 9. Closures
# 10. List/dict/set/tuple differences
# 11. Hashability
# 12. Dictionary/set complexity
# 13. append vs extend
# 14. Mutation while iterating
# 15. List comprehensions
# 16. Iterable vs iterator
# 17. Generator vs iterator
# 18. yield / next / StopIteration
# 19. Decorators
# 20. Exceptions
# 21. Context managers
# 22. Instance/class/static methods
# 23. Inheritance / overriding / polymorphism
# 24. dunder methods
# 25. __str__ vs __repr__
# 26. Heap memory management
# 27. Reference counting
# 28. Garbage collection
# 29. Strings and immutability
# 30. Truthiness
# 31. enumerate / zip
# 32. sorted vs sort
# 33. Heap data structure
# 34. Modules/imports
# 35. Type hints
# 36. async/await
# 37. threads/processes/GIL
# 38. serialization
# 39. testing basics
# 40. Python performance traps


# ============================================================
# HOW TO REVISE THIS BANK
# ============================================================

# DO NOT attempt to memorize 206 answers at once.
#
# Use three passes:
#
# PASS 1:
#   Questions 1-60
#   Core Python behavior, objects, functions, iterators/generators.
#
# PASS 2:
#   Questions 61-130
#   Decorators, exceptions, OOP, memory, hashing, collections, modules.
#
# PASS 3:
#   Questions 131-206
#   Type hints, async, concurrency, backend concerns, rapid-fire and
#   reasoning questions.
#
# For every failed question:
#
#   Day 0  -> learn it
#   Day 1  -> answer from memory
#   Day 3  -> answer again
#   Day 7  -> answer again
#   Day 14 -> answer again
#
# The goal is NOT:
#   "I have read this topic."
#
# The goal is:
#   "An interviewer can ask me this unexpectedly and I can explain it
#    clearly, predict code behavior, and handle a follow-up."


# ============================================================
# IMPORTANT: INTERVIEW ANSWER STRUCTURE
# ============================================================

# For code-output questions:
#
#   1. State the output.
#   2. Explain object/reference behavior.
#   3. Explain mutation vs rebinding.
#   4. Explain what survives after the operation.
#
# For conceptual questions:
#
#   1. Give a one-sentence definition.
#   2. Explain how it works.
#   3. Give one concrete example.
#   4. Give one real backend use case.
#   5. Mention one important trade-off or caveat.
#
# This is much stronger than giving a memorized one-line definition.
