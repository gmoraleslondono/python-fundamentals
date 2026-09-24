# Class 9 - Python fundamentals

## Recap

### Method overriding

Child classes can override parent methods to add their own information and **extend** the parent behavior, not only replace it. The parent class is called with `super()`.

## Polymorphism

The word comes from:

- **poly** = many
- **morph** = forms

Polymorphism allows different classes to have the same method name but provide different behavior. Different objects can respond to the same method call, each in their own way. You often use a list of objects and call the same method on all of them, even if the implementations differ.

```python
class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

class Cow:
    def make_sound(self):
        return "Moo!"

animals = [Dog(), Cat(), Cow()]  # they do not inherit from a particular class

for animal in animals:
    print(animal.make_sound())

# Woof!
# Meow!
# Moo!
```

The important part is that we do not need to know whether the object is a `Dog` or a `Cat`. We just know that they all have a `make_sound` method, and we can call it on all of them.

### Combine polymorphism with inheritance

```python
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

for animal in animals:
    print(animal.name, animal.make_sound())

# Buddy Woof!
# Whiskers Meow!
```

In Python, objects do not always need to inherit from the same class to be processed the same way. It is more about what the object can do than which class it inherits from. Python is flexible about object types.

## Duck typing

If it walks like a duck and quacks like a duck, then it is a duck.

Classes can share the same method name with different implementations, even if they are different types:

```python
class Robot:
    def make_sound(self):
        return "Beep!"

class Dog:
    def make_sound(self):
        return "Woof!"

things = [Robot(), Dog()]

for thing in things:
    print(thing.make_sound())

# Beep!
# Woof!
```

## `isinstance()`

Because polymorphism is flexible about types, you sometimes need to check if an object is of a particular type.

```python
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

print(isinstance(dog, Animal))  # True — Dog is a subclass of Animal
print(isinstance(dog, Dog))     # True
print(isinstance(dog, str))     # False
```

## `__str__()`

`__str__()` returns a string representation of the object, so `print` shows it in a readable way.

Without `__str__()`:

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

student = Student("John", 85)
print(student)  # <__main__.Student object at 0x...>
```

With `__str__()` — it must return a string:

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"{self.name} - score:{self.score}"

student = Student("John", 85)
print(student)  # John - score:85
```

`print` uses `__str__()` automatically. Prefer `str(student)` if you need a string; avoid calling `__str__()` directly.

```python
text = student
text1 = student.__str__()
text2 = str(student)

print(text)        # John - score:85  — still a Student object
print(type(text))  # <class '__main__.Student'>

print(text1)        # John - score:85  — a string, but don't call __str__ this way
print(type(text1))  # <class 'str'>

print(text2)        # John - score:85  — preferred: convert with str()
print(type(text2))  # <class 'str'>
```

### `__str__` with inheritance

```python
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

print(employee)   # John - salary:45000
print(developer)  # Jane - Developer - salary:55000 - language:Python
```

`Developer` inherits from `Employee`. `__str__()` is overridden in `Developer` to include extra information.

## Inheritance vs composition

- Inheritance is an **is-a** relationship: a dog is an animal
- Composition is a **has-a** relationship: a car has an engine

One object can contain another object (composition):

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

engine = Engine(200)
car = Car("Volvo", engine)

print(car.brand)             # Volvo
print(car.engine.horsepower)  # 200
```
