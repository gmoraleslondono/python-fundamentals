# OOP - lesson 2

# This is a problem: students= []
# class Course:
#     def __init__(self, name, students= []):
#         self.name = name
#         self.students = students
# Note: avoid to use mutable default values like list, dictionary, set, etc. as a class attribute because it will be shared by all objects of the class, and all objects will have the same value for that attribute

# Example of a bad course class
class BadCourse():
    def __init__(self, name, students= []):
        self.name = name
        self.students = students

    def add_student(self, student):
        self.students.append(student)

course1 = BadCourse("Python")
course2 = BadCourse("AI")

course1.add_student("Ada")

# print(course1.students) # ['Ada'] - > both object receive the same default list, when course change the list the course 2 receive the same value
# print(course2.students) # ['Ada']

# Solution: use None as default value and then assign a list to the students attribute when the object is created

# Example of a good course class
class GoodCourse():
    def __init__(self, name, students= None):
        self.name = name
        if students is None:
            self.students = []
        else:
            self.students = students

    def add_student(self, student):
        self.students.append(student)

course1 = GoodCourse("Python")
course2 = GoodCourse("AI")

course1.add_student("Ada")
# print(course1.students) # ['Ada'] # changing the students list of course1 will not affect the students list of course2
# print(course2.students) # []

# ------------------------------------------------------------
# Dictionaries vs classes

# Dictionaries are a collection of key-value pairs
# Classes are a collection of attributes and methods

# Dictionaries
student_dict = {
    "name": "Ada",
    "score": 95,
}

# Classes
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

student_class = Student("Ada", 95)

# both represent the same information, but the class is more flexible and can be extended to represent more information
# dictionary is a good choice when we dont need more behavior related to the data


# ------------------------------------------------------------
# OOP Part 2 --> class inheritance

# Recap
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_status(self):
        if self.score >= 70:
            return "Pass"
        return "Fail"

student1 = Student("Ada", 95)

# print(student1.name) # Ada
# print(student1.score) # 95
# print(student1.get_status()) # Pass

# Student is a class
# student is an object instance
# self refer to the specific object that is being created (student1 or student2 ... etc)
# what __init__ does is to initialize the object with the attributes that are passed to the class (constructor function)


# ------------------------------------------------------------
# Class inheritance

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating")

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating")

dog = Dog("Rex", 5)
cat = Cat("Luna", 3)

# dog.eat() # Rex is eating
# cat.eat() # Luna is eating

# Note: Inheritance helps to avoid repeating code and to create a more flexible and reusable code

class Animal: # Animal is a base class (superclass) of Dog and Cat
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal): # Dog is a subclass of Animal
    pass

class Cat(Animal): # Cat is a subclass of Animal
    pass

dog = Dog("Rex", 5)
cat = Cat("Luna", 3)

# print(dog.name) # Rex
# print(cat.name) # Luna

# dog.eat() # Rex is eating
# cat.eat() # Luna is eating

#Note:
# Terminology:
# Animal: Parent class, Base class, Superclass
# Dog: Child class, Subclass, Derived class
# Cat: Child class, Subclass, Derived class


# Note: Use the "is a" relationship - > Dog is an Animal : yes to create a class inheritance

# ------------------------------------------------------------
# Inherit methods

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        print(f"{self.name} is sleeping") # Rex is sleeping


# class Dog(Animal):
#     pass

# dog = Dog("Rex")
# print(dog.eat()) # Rex is eating
# print(dog.sleep()) # Rex is sleeping


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"

class Dog(Animal):
    def bark(self):
        return f"{self.name} is barking"

dog = Dog("Rex")
# print(dog.eat()) # Rex is eating
# print(dog.bark()) # Rex is barking


animal = Animal("Unknown")
# print(animal.bark()) # ERROR:Animal doesn't have the bark method

# ------------------------------------------------------------

# class inheritance override

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age, breed):
        self.name = name # This is wrong, we should use super().__init__(name, age)
        self.age = age
        self.breed = breed

dog = Dog("Rex", 5, "Labrador")
# print(dog.name) # Rex
# print(dog.age) # 5
# print(dog.breed) # Labrador


# correct way to initialize the Dog class using super()
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age) # This is correct, we use super() to call the __init__ method of the Animal
        self.breed = breed

dog = Dog("Rex", 5, "Labrador")
# print(dog.name) # Rex
# print(dog.age) # 5
# print(dog.breed) # Labrador

# ------------------------------------------------------------
# Another example of class inheritance

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        self.is_alive = True

        if age < 0:
            raise ValueError("Age cannot be negative")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

dog = Dog("Rex", 5, "Labrador")
# print(dog.name) # Rex
# print(dog.age) # 5
# print(dog.breed) # Labrador
# print(dog.is_alive) # True  -> because the Animal class has the is_alive attribute and the Dog class has the is_alive attribute

# ------------------------------------------------------------
# another example of class inheritance no recommended way. Try to use super() to call the __init__ method of the Animal class avoid repetition of code

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        self.is_alive = True

        if age < 0:
            raise ValueError("Age cannot be negative")


class Dog(Animal):
    def __init__(self, name, age, breed): # use super() to call the __init__ method of the Animal class avoid repetition of code
        self.name = name
        self.age = age
        self.is_alive = True # This will work but it is missing the is_alive attribute validation it will be always True

        self.breed = breed

dog = Dog("Rex", 5, "Labrador")
# print(dog.name) # Rex
# print(dog.age) # 5
# print(dog.breed) # Labrador
# print(dog.is_alive) # True  -> because the Animal class has the is_alive attribute and the Dog class has the is_alive attribute

# ------------------------------------------------------------


# Method overriding

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some animal sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

animal = Animal("animal")
dog = Dog("Rex")
cat = Cat("Luna")

# print(animal.make_sound()) # Some animal sound
# print(dog.make_sound()) # Woof!
# print(cat.make_sound()) # Meow!

# other way to override but keeping some functionality from parent class

class Employee:

    def get_information(self):
        return "Employee information"

class Developer(Employee):
    def get_information(self):
        base_info = super().get_information() # it add to the super class instead of overriding the method
        return f"{base_info} - Developer information"

developer = Developer()
print(developer.get_information()) # Employee information - Developer information

