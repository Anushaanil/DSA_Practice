# Assignment
# Note: Shallow and Deep copy applies only to the mutable objects

# immutable object
a = 1
b = a
print('--- Assignment: Immutable objects ---')
print(a, b)
print(id(a), id(b))
print('are they same?', id(a) == id(b))
print('\n')

# mutable object
a = [1,2,3]
b = a
print('--- Assignment: Mutable objects ---')
print(a, b)
print(id(a), id(b))
print('are they same?', id(a) == id(b))
print('\n')


# Shallow copy
import copy

# immutable object
a = 1
b = copy.copy(a)
print('--- Shallow copy: Immutable objects ---')
print(a, b)
print(id(a), id(b))
print('are they same?', id(a) == id(b))
print('\n')

# mutable object 1D Array
a = [1,2,3]
b = copy.copy(a)
print('--- Shallow copy: Mutable objects 1D Array--- \n')
print(a, b)
print(id(a), id(b))

# outer box is different with a and b
print('outer list same?', id(a) == id(b))
print('\n')

# inner box is same with a and b
print(id(a[0]), id(b[0]))
print('inner element reference same?', id(a[0]) == id(b[0]))
print('\n')

b[2] = 45
print('after modify once', a, b, a[2], b[2], id(a[2]), id(b[2]))

b.append(34)
print('after modify twice', a, b)


# mutable object 2D Array
c = [[1,2,3], [4,5,6]]
d = copy.copy(c)

print('--- Shallow copy: Mutable objects 2D array --- \n')
print(c, d)
print(id(c), id(d))

# outer box is different with c and d
print('outer list same?', id(c) == id(d))
print('\n')

# inner box is same with c and d
print(id(c[0]), id(d[0]))
print('inner element reference same?', id(c[0]) == id(d[0]))
print('\n')

c[0][2] = 1000
print('after modify once', c, d, c[0][2], d[0][2], id(c[0][2]), id(d[0][2]))

c.append([390])
print('after modify twice', c, d)
print('\n')

##### Deep copy #####

# immutable object
a = 1
b = copy.deepcopy(a)
print('--- Deep copy: Immutable objects ---')
print(a, b)
print(id(a), id(b))
print('are they same?', id(a) == id(b))
print('\n')

# mutable object 1D Array
a = [1,2,3]
b = copy.copy(a)
print('--- Deep copy: Mutable objects 1D Array--- \n')
print(a, b)
print(id(a), id(b))

# outer box is different with a and b
print('outer list same?', id(a) == id(b))
print('\n')

# inner box is same with a and b
print(id(a[0]), id(b[0]))
print('inner element reference same?', id(a[0]) == id(b[0]))
print('\n')

b[2] = 45
print('after modify once', a, b, a[2], b[2], id(a[2]), id(b[2]))

b.append(34)
print('after modify twice', a, b)
print('\n')


# mutable object 2D Array
c = [[1,2,3], [4,5,6]]
d = copy.copy(c)

print('--- Deep copy: Mutable objects 2D array --- \n')
print(c, d)
print(id(c), id(d))

# outer box is different with c and d
print('outer list same?', id(c) == id(d))
print('\n')

# inner box is same with c and d
print(id(c[0]), id(d[0]))
print('inner element reference same?', id(c[0]) == id(d[0]))
print('\n')

c[0][2] = 1000
print('after modify once', c, d, c[0][2], d[0][2], id(c[0][2]), id(d[0][2]))

c.append([390])
print('after modify twice', c, d)