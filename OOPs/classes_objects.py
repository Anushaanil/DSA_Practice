# Class Example

# Create a class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

# Create an object
p1 = Person("John", 36)

# Call the greet method
p1.greet()


'''

Why Use __init__()?
Without the __init__() method, you would need to set properties manually for each object:

Example
Create a class without __init__():

'''

class Person:
  pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age)

'''
def __init__(self, name, age=18) # Set a default value for the age parameter

Note: The self parameter must be the first parameter of any method in the class.

The self parameter is a reference to the current instance of the class.

It is used to access properties and methods that belong to the class.
'''

# Access the properties of an object

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)


# Change the age property

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Tobias", 25)
print(p1.age)

p1.age = 26
print(p1.age)

# Delete the age property

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 30)

del p1.age

print(p1.name) # This works
# print(p1.age) # This would cause an error

# Class Properties vs Object Properties
# Properties defined inside __init__() belong to each object (instance properties).
# Properties defined outside methods belong to the class itself (class properties) and are shared by all objects

class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

# When you modify a class property, it affects all objects

class Person:
  lastname = ""

  def __init__(self, name):
    self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Refsnes"

print(p1.lastname)
print(p2.lastname)


# You can add new properties to existing objects


class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)

# Inside the editor, complete the following steps:
# Create a class Student with an __init__ that takes name and grade, and stores them as properties
# Create an object s1 with name "Anna" and grade "A"
# Print the grade of s1
# Change the grade of s1 to "B"
# Print the updated grade

class Student:
  def __init__(self, name, grade):
    self.name = name
    self.grade = grade

s1 = Student("Anna", "A")
print(s1.grade)

s1.grade = "B"
print(s1.grade)
  

# Class Methods
# Methods are functions that belong to a class. They define the behavior of objects created from the class.

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()


# Methods with Parameters
# Methods can accept parameters just like regular functions:

class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

# Methods Accessing Properties
# Methods can access and modify object properties using self


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info())

# Methods Modifying Properties
# Methods can modify the properties of an object


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()


# The __str__() Method
# The __str__() method is a special method that controls what is returned when the object is printed

# Without the __str__() method:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)
print(p1)


# With the __str__() method:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)


# A class can have multiple methods that work together
# You can delete methods from a class using the del keyword:
# del Person.greet
# p1.greet() # This will cause an error

'''
Inside the editor, complete the following steps:
Create a class called Rectangle
Add an __init__ method with width and height, and store them as properties
Add a method called area that returns the width multiplied by the height
Create an object r1 with width 5 and height 3
Print the area of r1
'''

class Rectangle:
  def __init__(self, width, height) -> None:
    self.width = width
    self.height = height

  def area(self):
    return self.width * self.height

r1 = Rectangle(5, 3)
print(r1.area())