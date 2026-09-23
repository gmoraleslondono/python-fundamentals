# Class 8 - Python fundamentals

## OOP - lesson 2

### Mutable default arguments

This is a problem: `students=[]` as a default value.

Avoid using **mutable** default values (list, dictionary, set, etc.) because the same object is shared by all instances. If one object changes it, the others see the same change.

Example of a bad course class:

```python
class BadCourse:
    def __init__(self, name, students=[]):
        self.name = name
        self.students = students

    def add_student(self, student):
        self.students.append(student)

course1 = BadCourse("Python")
course2 = BadCourse("AI")

course1.add_student("Ada")

print(course1.students)  # ['Ada']
print(course2.students)  # ['Ada'] — both objects share the same default list
```

Solution: use `None` as the default value and create a new list when the object is created.

Example of a good course class:

```python
class GoodCourse:
    def __init__(self, name, students=None):
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
print(course1.students)  # ['Ada']
print(course2.students)  # [] — changing course1 does not affect course2
```

## Dictionaries vs classes

- Dictionaries are a collection of key-value pairs
- Classes are a collection of attributes and methods

```python
# Dictionary
student_dict = {
    "name": "Ada",
    "score": 95,
}

# Class
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

student_class = Student("Ada", 95)
```

Both represent the same information, but the class is more flexible and can be extended. A dictionary is a good choice when you do not need extra behavior related to the data.

## Recap

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_status(self):
        if self.score >= 70:
            return "Pass"
        return "Fail"

student1 = Student("Ada", 95)

print(student1.name)         # Ada
print(student1.score)        # 95
print(student1.get_status())  # Pass
```

- `Student` is a class
- `student1` is an object instance
- `self` refers to the specific object that is being created (`student1`, `student2`, ...)
- `__init__` initializes the object with the attributes that are passed to the class (constructor)

## Class inheritance

Without inheritance, `Dog` and `Cat` repeat the same code:

```python
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

dog.eat()  # Rex is eating
cat.eat()  # Luna is eating
```

Inheritance helps avoid repeating code and makes the code more flexible and reusable.

```python
class Animal:  # Animal is a base class (superclass) of Dog and Cat
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):  # Dog is a subclass of Animal
    pass

class Cat(Animal):  # Cat is a subclass of Animal
    pass

dog = Dog("Rex", 5)
cat = Cat("Luna", 3)

print(dog.name)  # Rex
print(cat.name)  # Luna

dog.eat()  # Rex is eating
cat.eat()  # Luna is eating
```

### Terminology

- **Animal**: parent class, base class, superclass
- **Dog**: child class, subclass, derived class
- **Cat**: child class, subclass, derived class

Use the **"is a"** relationship to decide if inheritance makes sense: Dog is an Animal → yes.

## Inherit methods

A subclass inherits the parent methods:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    pass

dog = Dog("Rex")
print(dog.eat())   # Rex is eating
dog.sleep()        # Rex is sleeping
```

A subclass can also add its own methods. The parent class does not get those methods:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"

class Dog(Animal):
    def bark(self):
        return f"{self.name} is barking"

dog = Dog("Rex")
print(dog.eat())   # Rex is eating
print(dog.bark())  # Rex is barking

animal = Animal("Unknown")
print(animal.bark())  # AttributeError: Animal doesn't have the bark method
```

## Override `__init__` with `super()`

Repeating parent attributes in the child `__init__` is the wrong approach:

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age, breed):
        self.name = name  # This is wrong, we should use super().__init__(name, age)
        self.age = age
        self.breed = breed

dog = Dog("Rex", 5, "Labrador")
print(dog.name)   # Rex
print(dog.age)    # 5
print(dog.breed)  # Labrador
```

Correct way: call the parent `__init__` with `super()`:

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # call Animal.__init__
        self.breed = breed

dog = Dog("Rex", 5, "Labrador")
print(dog.name)   # Rex
print(dog.age)    # 5
print(dog.breed)  # Labrador
```

### Why `super()` matters

The parent class may set extra attributes and run validation. `super()` reuses that instead of copying it.

```python
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
print(dog.name)      # Rex
print(dog.age)       # 5
print(dog.breed)     # Labrador
print(dog.is_alive)  # True — comes from Animal
```

Not recommended: repeating parent setup in the child. You skip validation and duplicate code.

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_alive = True

        if age < 0:
            raise ValueError("Age cannot be negative")

class Dog(Animal):
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.is_alive = True  # works, but skips the age validation
        self.breed = breed
```

## Method overriding

A child class can replace a parent method with its own version:

```python
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

print(animal.make_sound())  # Some animal sound
print(dog.make_sound())     # Woof!
print(cat.make_sound())     # Meow!
```

Override while keeping some functionality from the parent class with `super()`:

```python
class Employee:
    def get_information(self):
        return "Employee information"

class Developer(Employee):
    def get_information(self):
        base_info = super().get_information()  # use the parent method, then extend it
        return f"{base_info} - Developer information"

developer = Developer()
print(developer.get_information())  # Employee information - Developer information
```
