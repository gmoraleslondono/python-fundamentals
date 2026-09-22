# Class 7 - Python fundamentals

## Recap

- a dictionary is a collection of key-value pairs
- methods are used to perform operations on the data

```python
student = {
    "name": "John",
    "score": 100,
    "active": True
}

def get_status(student):
    if student["score"] >= 60:
        return "Pass"
    else:
        return "Fail"

print(get_status(student))
```

## Relationship between data and behavior

- **class**: definition or blueprint of an object
- **object**: a concrete instance of the class, created from the class

Example: `Student` is the class; John, Jane, and Jim are objects.

## First class

```python
class Student:  # (Student, BankAccount)
    pass  # class body empty

student1 = Student()  # student1 is an instance of the Student class

print(type(student1))  # class Student
print(student1)        # <__main__.Student object at 0x...>

student2 = Student()  # student2 is another instance of the Student class

print(student1 is student2)  # False — they are different objects even though they are the same class
```

## Adding information manually

`name` is an **instance attribute**. Object **state** is the values assigned to the object (`name`, `score`).

```python
class Student:
    pass

student1 = Student()
student1.name = "John"
student1.score = 100

print(student1.name)   # John
print(student1.score)  # 100

student2 = Student()
student2.name = "Jane"
student2.score = 80

print(student2.name)   # Jane
print(student2.score)  # 80

print(student1.name, student1.score)  # John 100
print(student2.name, student2.score)  # Jane 80
```

If an attribute was never set, accessing it raises an error:

```python
student3 = Student()
student3.name = "Jim"

print(student3.score)  # AttributeError — score was never assigned
```

## `__init__`

`__init__` is a special method that is called when an object is created. `self` refers to the specific object that is being created (`student1`, `student2`, ...).

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

student1 = Student("John", 100)  # self -> student1 -> name = John, score = 100
print(student1.name, student1.score)

student2 = Student("Jane", 80)   # self -> student2 -> name = Jane, score = 80
print(student2.name, student2.score)
```

Parameter names do not have to match the attribute names:

```python
class Student:
    def __init__(self, student_name, student_score):
        self.name = student_name
        self.score = student_score

student1 = Student("John", 100)
print(student1.name, student1.score)
```

### Default values

```python
class Student:
    def __init__(self, name, score=0, active=True):
        self.name = name
        self.score = score
        self.active = active

student1 = Student("John", 100)
student2 = Student("Jane")

print(student1.name, student1.score, student1.active)
print(student2.name, student2.score, student2.active)
```

### Keyword arguments

```python
student3 = Student(
    name="Jim",
    score=60,
    active=False
)

print(student3.name, student3.score, student3.active)
```

## Object behavior

Behavior is the **methods** of the object.

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def introduce(self):
        print(f"Hello, my name is {self.name}")

student1 = Student("John", 100)
student1.introduce()

student2 = Student("Jane", 80)
student2.introduce()
```

`introduce` is a method of the `Student` class. Each student object uses it with its own `self.name`.

### Method that returns a value: `get_status`

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_status(self):
        if self.score >= 70:
            return "Pass"
        return "Fail"

student1 = Student("John", 80)
print(student1.get_status())

student2 = Student("Jane", 62)
print(student2.get_status())
```

### Method that changes the state of the object: `update_score`

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def update_score(self, new_score):
        self.score = new_score

student1 = Student("John", 100)
print(student1.score)
student1.update_score(80)
print(student1.score)
```

### Validation and exceptions: `update_score`

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def update_score(self, new_score):
        if new_score < 0 or new_score > 100:
            raise ValueError("Score must be between 0 and 100")
        self.score = new_score

student = Student("John", 100)
student.update_score(150)  # ValueError: Score must be between 0 and 100
print(student.score)
```

### Another example: `deposit()`

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

account = BankAccount("John", 100)
print(account.balance)  # 100

account.deposit(500)
print(account.balance)  # 600
```

## Instance attributes vs class attributes

**Instance attributes** belong to a specific object:

```python
class Student:
    def __init__(self, name):
        self.name = name

student1 = Student("Ada")
student2 = Student("Grace")

student1.name = "Ada Lovelace"

print(student1.name)  # Ada Lovelace
print(student2.name)  # Grace
```

**Class attributes** are values shared by all objects created from the same class:

```python
class Student:
    school = "Lexicon"  # class attribute

    def __init__(self, name):
        self.name = name  # instance attribute

student1 = Student("Ada")
student2 = Student("Grace")

print(student1.school)  # Lexicon
print(student2.school)  # Lexicon
print(Student.school)   # Lexicon
```

Changing the class attribute updates it for all objects that still use the shared value:

```python
Student.school = "AI Academy"

print(student1.school)  # AI Academy
print(student2.school)  # AI Academy
print(Student.school)   # AI Academy
```

One object can get its own `school` attribute. After that, class attributes stay as shared class-level data, and instance attributes belong to an individual object:

```python
student1.school = "Another school"

print(student1.school)  # Another school
print(student2.school)  # AI Academy
print(Student.school)   # AI Academy
```

### Another example of class attributes

```python
class Product:
    tax_rate = 0.25

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_with_tax(self):
        return self.price + (self.price * self.tax_rate)

product1 = Product("Laptop", 1000)
print(product1.price_with_tax())  # 1250

product2 = Product("Phone", 500)
print(product2.price_with_tax())  # 625
```

## Collection of objects

A list of objects at the same time:

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_status(self):
        if self.score >= 70:
            return "Pass"
        return "Fail"

students = [
    Student("John", 85),
    Student("Jane", 62),
    Student("Jim", 91)
]

for student in students:
    print(
        student.name,
        student.score,
        student.get_status()
    )

# John 85 Pass
# Jane 62 Fail
# Jim 91 Pass
```

List comprehension:

```python
passed_students = [student for student in students if student.score >= 70]

for student in passed_students:
    print(student.name)  # John, Jim
```

## An attribute can refer to another object

```python
class Teacher:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

teacher = Teacher("John")
course = Course("Python foundation", teacher)

print(course.name)          # Python foundation
print(course.teacher.name)  # John
```

A course can also hold a list of student objects:

```python
class Student:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, name):
        self.name = name
        self.students = [] # internal variable (only accessible within the class)

    def add_student(self, student):
        self.students.append(student)

course = Course("Python foundation")

student1 = Student("John")
student2 = Student("Jane")

course.add_student(student1)
course.add_student(student2)

for student in course.students:
    print(student.name)  # John, Jane
```
