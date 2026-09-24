# OOP - Object-Oriented Programming

# Recap:

# Method overriding
# Child classes can override the methods of the parent class to add their own information to extend the parent method behavior not just only replacing it.
# The parent class is called by super()


# -------------------------------------------------------------

# Polymorphism:

# The word comes from:
# poly = many
# morph = forms

# Polymorphism allows different classes to have the same method name but provide different behavior.
# Different objects can respond to the same method call but in their own way
# here we use a lot list of objects and we call the same method on all of them but they have different implementations.

class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

class Cow:
    def make_sound(self):
        return "Moo!"

animals = [Dog(), Cat(), Cow()] # all objects have different implementations of the make_sound method, actually they dont inherit from any particular class
# for animal in animals:
    # print(animal.make_sound())

# Woof!
# Meow!
# Moo!

# The important part is that we don't need to know whether the object is a Dog or Cat
# we just know that they all have a make_sound method and we can call it on all of them

# -------------------------------------------------------------

# Combine polymorphism with inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Unknown sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

animals = [Dog("Buddy"), Cat("Whiskers")]

# for animal in animals:
#     print(animal.name, animal.make_sound())

# Buddy Woof!
# Whiskers Meow!


# -------------------------------------------------------------
# in Python not always the objects need to inherit from a particular class to process them in the same way
# it looks more about the object that the class they inherit from or they are
# Python is flexible about objects types

# Duck Typing : if it walks like a duck, quacks like a duck, then it is a duck

#classes with the same method name but different implementations, different object types
class Robot:
    def make_sound(self):
        return "Beep!"

class Dog:
    def make_sound(self):
        return "Woof!"

things = [Robot(), Dog()]

# for thing in things:
#     print(thing.make_sound())
# Beep!
# Woof!

# -------------------------------------------------------------
# Since polymorphism is flexible about objects types, we need to check if an object is of a particular type
# isinstance()
# if isinstance(...) ...

class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

# print(isinstance(dog, Animal)) # True -> why is this true? because dog is an instance of the Dog class which is a subclass of the Animal class
# print(isinstance(dog, Dog)) # True

# print(isinstance(dog, str)) # False


# -------------------------------------------------------------
#__str__() method

# __str__() method is used to return a string representation of the object
# it is used to print the object in a readable way

#without __str__() method
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

student = Student("John", 85)

# print(student) # <__main__.Student object at 0x10336cc20>

# with __str__() method
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"{self.name} - score:{self.score}" # must return a string

student = Student("John", 85)
# print(student) # John - score:85

text = student
text1 = student.__str__()
text2 = str(student)

print(text) # John - score:85  -> this is calling the __str__() method but it is not a string it is an object
print(type(text)) # <class '__main__.Student'>
print(text1) # John - score:85  -> this is calling the __str__() method and it is a string but dont use it that way
print(type(text1)) # <class 'str'>
print(text2) # John - score:85  -> this is calling the str() function and it is a string we use this approach to convert the object to a string
print(type(text2)) # <class 'str'>


# -------------------------------------------------------------

# __str__ with inheritance

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return (
            f"{self.name} - "
            f"salary:{self.salary}"
        )

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def __str__(self):
        return (
            f"{self.name} - Developer -"
            f"salary:{self.salary} - "
            f"language:{self.language}"
        )

employee = Employee("John", 45000)
developer = Developer("Jane", 55000, "Python")

# print(employee) # John - salary:45000 
# print(developer) # Jane - Developer - salary:55000 - language:Python


# Developer class inherits from the Employee class
# the __str__() method is overridden in the Developer class to return a string representation of the Developer object


# -------------------------------------------------------------

# class inherit from other classes?
# an object can inherit from a class?
# inheritance is a is-a relationship
# a dog is an animal

# one object can contain another object (has-a relationship) - > composition
# car has an engine

# Composition:

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

engine = Engine(200)
car = Car("Volvo", engine)
# print(car.brand) # Volvo
# print(car.engine.horsepower) # 200

