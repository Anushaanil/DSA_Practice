'''
Create a Parent Class
Any class can be a parent class, so the syntax is the same as creating any other class:

Example
Create a class named Person, with firstname and lastname properties, and a printname method

'''

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

'''
Create a Child Class
To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

Example
Create a class named Student, which will inherit the properties and methods from the Person class:
What is the correct keyword to use inside an empty class, to avoid getting an error? use pass keyword.
'''


class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()


class Student(Person):
    def __init__(self, school):
        #add properties etc.
        self.school = school
    
    def printschool(self):
       print(self.school)

# x = Student("Mike", "Olsen") # throws error as the child class __init__ method overwrites parent class one here
# x.printname()

x = Student("Cambridge College")
x.printschool()


# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Ross")
x.printname()

# Python also has a super() function that will make the child class inherit all the methods and properties from its parent
# By using the super() function, you do not have to use the name of the parent element, 
# it will automatically inherit the methods and properties from its parent.

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduation_year = 2019

x = Student("Michael", "Ross")
x.printname()
print(x.graduation_year)


# pass graduation year attribute to child class init method only and use it with the method.
class Student(Person):
  def __init__(self, fname, lname, graduation_year):
    super().__init__(fname, lname)
    self.graduation_year = graduation_year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduation_year)


x = Student("Anusha", "Shet", 2020)
# x.printname()
# print(x.graduation_year)
x.welcome()

'''
Inside the editor, complete the following steps:
Create a parent class Animal with an __init__ that takes name
Add a method speak that prints the name
Create a child class Dog that inherits from Animal
Create an object d1 = Dog("Rex")
Call d1.speak()

'''

class Animal:
  def __init__(self, name) -> None:
    self.name = name
  
  def speak(self):
    print(self.name)

class Dog(Animal):
  pass

d1 = Dog("Rex")
d1.speak()