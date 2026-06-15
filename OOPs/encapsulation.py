'''
Python Encapsulation
Encapsulation is about protecting data inside a class.

It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.

This prevents accidental changes to your data and hides the internal details of how your class works.
'''

# Private Properties
# In Python, you can make properties private by using a double underscore __ prefix
# Note: Private properties cannot be accessed directly from outside the class.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

p1 = Person("Emil", 25)
# print(p1.name)
# print(p1.__age) # This will cause an error

# To access a private property, you can create a getter method:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property
  
  def get_age(self):
    print(self.__age)

p1 = Person("Emil", 25)
print(p1.name)
p1.get_age()

# To modify a private property, you can create a setter method.
# The setter method can also validate the value before setting it

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property
  
  def get_age(self):
    print(self.__age)
  
  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("Emil", 25)
print(p1.name)
# p1.get_age()

p1.set_age(26)
p1.get_age()

'''
Why Use Encapsulation?
Encapsulation provides several benefits:

Data Protection: Prevents accidental modification of data
Validation: You can validate data before setting it
Flexibility: Internal implementation can change without affecting external code
Control: You have full control over how data is accessed and modified

'''

class Student:
  def __init__(self, name):
    self.name = name
    self.__grade = 0

  def set_grade(self, grade):
    if 0 <= grade <= 100:
      self.__grade = grade
    else:
      print("Grade must be between 0 and 100")

  def get_grade(self):
    return self.__grade

  def get_status(self):
    if self.__grade >= 60:
      return "Passed"
    else:
      return "Failed"

student = Student("Emil")
student.set_grade(95)
print(student.get_grade())
print(student.get_status())


# Python also has a convention for protected properties using a single underscore _ prefix:
# Note: A single underscore _ is just a convention. 
# It tells other programmers that the property is intended for internal use, but Python doesn't enforce this restriction.

class Person:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary # Protected property

p1 = Person("Linus", 50000)
print(p1.name)
print(p1._salary) # Can access, but shouldn't


# You can also make methods private using the double underscore prefix:

class Calculator:
  def __init__(self):
    self.result = 0

  def __validate(self, num):
    if not isinstance(num, (int, float)):
      return False
    return True

  def add(self, num):
    if self.__validate(num):
      self.result += num
    else:
      print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)
# calc.__validate(5) # This would cause an error
# Note: Just like private properties with double underscores, private methods cannot be called directly from outside the class. 
# The __validate method can only be used by other methods inside the class.

# Name Mangling
# Name mangling is how Python implements private properties and methods.

# When you use double underscores __, Python automatically renames it internally by adding _ClassName in front.

# For example, __age becomes _Person__age.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

p1 = Person("Emil", 30)

# This is how Python mangles the name:
print(p1._Person__age) # Not recommended!
# Note: While you can access private properties using the mangled name, it's not recommended. It defeats the purpose of encapsulation.


'''
Inside the editor, complete the following steps:
Create a class ScoreBoard
Add an __init__ with a score parameter and store it as a private attribute
Add a method called get_score that returns the private score
Create an object s1 with a score of 0
Print the score of s1
'''

class ScoreBoard:
  def __init__(self, score):
    self.__score = score
  
  def get_score(self):
    return self.__score

s1 = ScoreBoard(0)
print(s1.get_score())