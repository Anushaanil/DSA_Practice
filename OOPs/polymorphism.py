'''
The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators 
with the same name that can be executed on many objects or classes.

An example of a Python function that can be used on different objects is the len() function.

on strings -> len(a) -> gives number of chars in string a
on tuple -> len(a) -> gives no.of items in tuple a
on dict -> len(a) -> gives no.of key-value pairs in dict a

'''


# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move()


class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

# for x in (car1, boat1, plane1):
#   x.move()


'''
Inheritance Class Polymorphism
What about classes with child classes with the same name? Can we use polymorphism there?
Yes. If we use the example above and make a parent class called Vehicle, and make Car, Boat, Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:

Child classes inherits the properties and methods from the parent class.

In the example below you can see that the Car class is empty, but it inherits brand, model, and move() from Vehicle.

The Boat and Plane classes also inherit brand, model, and move() from Vehicle, but they both override the move() method.

Because of polymorphism we can execute the same method for all classes.

'''

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand, x.model)
  x.move()


'''
Inside the editor, complete the following steps:
Create a class Cat with a method sound that prints "Meow"
Create a class Fox with a method sound that prints "Wa-pa-pa-pa-pa-pow!"
Create objects c1 = Cat() and f1 = Fox()
Call sound() on both objects
'''

class Cat:
  def sound(self):
    print('Meow')

class Fox:
  def sound(self):
    print('Wa-pa-pa-pa-pa-pow!')

c1 = Cat()
f1 = Fox()

for x in (c1, f1):
  x.sound()
