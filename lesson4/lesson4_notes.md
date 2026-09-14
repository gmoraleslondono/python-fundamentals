# Class 4 - Python fundamentals

## Functions

Reusable blocks of code.

```python
def greet():
    print("Hello")

greet()  # Hello
greet()  # Hello
greet()  # Hello
greet()  # Hello
```

Function names follow the same convention as variables: lowercase and snake case.

```python
def say_good_morning():
    print("Good morning")

say_good_morning()  # Good morning
```

## Function parameters

Parameters are the values passed to the function.

```python
def greet(name):  # name is the parameter
    print("Hello", name)

greet("Ada")    # Hello Ada - Ada is the argument
greet("Grace")  # Hello Grace
```

### Multiple parameters

```python
def introduce(name, age):
    print(name, "is", age, "years old")

introduce("Ada", 30)  # Ada is 30 years old
```

Arguments are positional: they are placed by their position.

```python
def introduce(name, age):
    print("Name:", name)
    print("Age:", age)

introduce(36, "Ada")              # Name: 36, Age: Ada
introduce(age=36, name="Ada")     # Name: Ada, Age: 36 - keyword arguments, they are place by their name
```

## Return values

Functions can return a value.

```python
def calculate_tax(income, tax_rate):
    tax = income * tax_rate
    print("Tax:", tax)

calculate_tax(50000, 0.3)  # Tax: 15000
```

`return` is used to return a value from a function.

```python
def calculate_tax(income, tax_rate):
    tax = income * tax_rate
    return tax

result = calculate_tax(50000, 0.3)

calculate_tax(result)  # Tax: 15000
```

```python
def add_with_print(a, b):
    print(a + b)  # 8

result = add_with_print(5, 3)
print("Result:", result)  # Result: None - because the function does not return a value
```

```python
def add_with_print(a, b):
    return a + b

result = add_with_print(5, 3)
print("Result:", result)  # Result: 8
```

```python
def calculate_tax(income, tax_rate):
    return income * tax_rate

tax = calculate_tax(50000, 0.3)

income_after_tax = 50000 - tax

print("Tax:", tax)                              # Tax: 15000
print("Income after tax:", income_after_tax)    # Income after tax: 35000
```

```python
def calculate_tax(income, tax_rate):
    return income * tax_rate

print(calculate_tax(50000, 0.3))  # 15000
```

```python
def example():
    print("Before return")
    return 10  # this will exit the function and return the value 10
    print("After return")  # this will not be executed

result = example()
print("Result:", result)  # Result: 10
```

## Functions and conditions

```python
def check_grade(score):
    if score >= 70:
        return "Pass"
    else:
        return "Fail"

print(check_grade(85))  # Pass
print(check_grade(62))  # Fail
```

```python
def check_grade(score):
    if score >= 70:
        return "Pass"

    return "Fail"

print(check_grade(85))  # Pass
print(check_grade(62))  # Fail
```

## Functions, lists, and collections

```python
def get_first_item(items):
    return items[0]

languages = ["Python", "Java", "C#"]

print(get_first_item(languages))  # Python
```

## Functions and loops

```python
def print_languages(languages):
    for language in languages:
        print(language)

my_languages = ["Python", "Java", "C#"]
print_languages(my_languages)  # Python, Java, C#
```

### Combination with loops, collections, and conditions

```python
def count_passing_scores(scores):
    passed = 0

    for score in scores:
        if score >= 70:
            passed += 1

    return passed

scores = [85, 62, 91, 70, 48]

result = count_passing_scores(scores)
print("Passed", result)  # Passed 3
```

## Functions and dictionaries

```python
def get_student_status(student):
    if student["score"] >= 70:
        return "Pass"

    return "Fail"

student = {
    "name": "John",
    "score": 85
}

status = get_student_status(student)
print(student["name"], status)  # John Pass
```

### Functions and lists of dictionaries

```python
students = [
    {"name": "Anna", "score": 85},
    {"name": "Bob", "score": 62},
    {"name": "Charlie", "score": 91}
]

def get_student_status(student):
    if student["score"] >= 70:
        return "Pass"

    return "Fail"

for student in students:
    status = get_student_status(student)
    print(student["name"], status)  # Anna Pass, Bob Fail, Charlie Pass
```

## Default parameter values

```python
def introduce(name, age=20):
    print("Name:", name)
    print("Age:", age)

introduce("Ada")        # Name: Ada, Age: 20
introduce("Grace", 25)  # Name: Grace, Age: 25
```

Default parameters must be at the end of the parameter list.

```python
# def greet(greeting="Hello", name):  # invalid
def greet(name, greeting="Hello"):
    print(greeting, name)

greet("Ada")  # Hello Ada
```

```python
def create_user(name, role="student", active=True):
    print("Name:", name)
    print("Role:", role)
    print("Active:", active)

create_user("Ada")                  # Name: Ada, Role: student, Active: True
create_user("Ada", role="teacher")  # Name: Ada, Role: teacher, Active: True
create_user("Ada", active=False)    # Name: Ada, Role: student, Active: False
```

## Return multiple values as a tuple

```python
def min_and_max(numbers):
    return min(numbers), max(numbers)

result = min_and_max([4, 8, 1, 12, 3])
print(result)        # (1, 12)
print(type(result))  # <class 'tuple'>

smallest, largest = min_and_max([4, 8, 1, 12, 3])  # unpacking the tuple into smallest and largest
print("Smallest:", smallest)  # Smallest: 1
print("Largest:", largest)    # Largest: 12
```

## Functions calling functions

The order of calling functions is important. Python reads from top to bottom.

```python
def calculate_tax(income, tax_rate):
    return income * tax_rate

def calculate_income_after_tax(income, tax_rate):
    tax = calculate_tax(income, tax_rate)
    return income - tax

result = calculate_income_after_tax(50000, 0.3)
print("Income after tax:", result)  # Income after tax: 35000
```

## Built-in functions vs methods vs custom functions

```python
numbers = [5, 2, 9, 1]
print(len(numbers))  # 4 - built-in function

numbers.sort()  # method belonging to the list object - built-in method
print(numbers)  # [1, 2, 5, 9]

def get_first_item(items):  # custom function
    return items[0]

print(get_first_item(numbers))  # 1
```

## Type hints

Types are not enforced by the interpreter, but it is a good practice to use them.

```python
def add(a: int, b: int) -> int:
    return a + b

print(add(1, 2))              # 3
print(add("Hello", "World"))  # HelloWorld 🤯
```

## Documentation strings (docstrings)

```python
def calculate_area(width, height):
    """Return the area of a rectangle."""
    return width * height

print(calculate_area(10, 20))  # 200
print(calculate_area.__doc__)  # Return the area of a rectangle.
```
