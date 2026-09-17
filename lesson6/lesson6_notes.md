# Class 6 - Python fundamentals

## Recap

- variables
- strings
- collections
- functions
- loops
- scope
- args and kwargs
- Readability matters

## List comprehension

Way one to do it (traditional way):

```python
numbers = [1, 2, 3, 4, 5]  # need to multiply for 2

double_numbers = []

for numbers in numbers:
    double_numbers.append(numbers * 2)

print(double_numbers)  # [2, 4, 6, 8, 10]
```

Way two to do it (list comprehension):

```python
double_numbers = [numbers * 2 for numbers in numbers]
print(double_numbers)  # [2, 4, 6, 8, 10]
```

### Examples

List numbers:

```python
numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]
print(squares)  # [1, 4, 9, 16, 25]
```

List strings:

```python
names = ["John", "Jane", "Jim", "Jill"]
upper_names = [name.upper() for name in names]
print(upper_names)  # ["JOHN", "JANE", "JIM", "JILL"]
```

### Filter values from a list

Traditional way:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)  # [2, 4, 6, 8, 10]
```

Conditionals in list comprehension:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)  # [2, 4, 6, 8, 10]
```

The condition determines what is added in the new list:

```python
numbers = [1, 2, 3, 4, 5, 6]
result = [number ** 2 for number in numbers if number % 2 == 0]
print(result)  # [4, 16, 36]
```

```python
names = ["John", "Jane", "Jim", "Jill"]
result = [name for name in names if len(name) >= 4]
print(result)  # ['John', 'Jane', 'Jill']
```

Several conditions in list comprehension:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [number for number in numbers if number % 2 == 0 and number % 3 == 0]
print(result)  # [6]
```

## Dictionary comprehension

Way one to do it (traditional way):

```python
numbers = [1, 2, 3, 4, 5]  # -> keys
squared_numbers = {}

for number in numbers:
    squared_numbers[number] = number ** 2
print(squared_numbers)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

Way two to do it (dictionary comprehension):

```python
numbers = [1, 2, 3, 4, 5]  # -> keys
squared_numbers = {number: number ** 2 for number in numbers}  # -> values
print(squared_numbers)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Dictionary comprehension on an existing dictionary

We use `items()` to get the key and value pairs from the dictionary:

```python
prices = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}

double_prices = {product: price * 2 for product, price in prices.items()}
print(double_prices)  # {"apple": 20, "banana": 10, "orange": 16}
```

### Filter values from a dictionary using dictionary comprehension

```python
scores = {
    "Anna": 85,
    "Bob": 62,
    "Charlie": 91,
    "Diana": 70
}

# Who passed the exam > 70
passed = {
    name: score
    for name, score in scores.items()
    if score >= 70
}
print(passed)  # {'Anna': 85, 'Charlie': 91, 'Diana': 70}
```

## Set comprehension

Sets are unordered and store unique values:

```python
words = ["python", "Java", "python", "C#", "java"]

lengths = {len(word) for word in words}
print(lengths)  # {2, 3, 4}  # unique values
```

## Generator expression

`( ... )` is a generator expression, not a tuple comprehension:

```python
numbers = (number * 2 for number in range(5))
print(numbers)  # generator object, not a tuple
```

### Remember

Readability is the most important thing in programming.

- `[ ... ]` -> list comprehension
- `{key: value ... }` -> dictionary comprehension
- `{ ... }` -> set comprehension
- `( ... )` -> generator expression, for example: `(number * 2 for number in range(5))`

## Enumerate

`enumerate` gives you the index and the value of the element in the list.

Way one to do it (traditional way):

```python
languages = ["Python", "Java", "C#"]

for index in range(len(languages)):
    print(index, languages[index])  # 0 Python, 1 Java, 2 C#
```

Way two to do it (`enumerate`):

```python
for index, language in enumerate(languages):  # unpack the list into index and language in the for loop
    print(index, language)  # 0 Python, 1 Java, 2 C#
```

Way three to do it (`enumerate` with `start`):

```python
for position, language in enumerate(languages, start=1):  # start is the index of the first element
    print(position, language)  # 1 Python, 2 Java, 3 C#
```

```python
for language in languages:
    print(language)  # Python, Java, C#

for index, language in enumerate(languages):
    print(index, language)  # 0 Python, 1 Java, 2 C#
```

## Zip

`zip` combines two lists into a single list of tuples.

Way one to do it (traditional way):

```python
names = ["John", "Jane", "Jim"]
scores = [85, 62, 91]

for i in range(len(names)):
    print(names[i], scores[i])  # John 85 Jane 62 Jim 91
```

Way two to do it (`zip`):

```python
for name, score in zip(names, scores):
    print(name, score)  # John 85 Jane 62 Jim 91
```

Convert to list:

```python
pairs = list(zip(names, scores))
print(pairs)  # [('John', 85), ('Jane', 62), ('Jim', 91)]
```

Convert to dictionary:

```python
pairs = dict(zip(names, scores))
print(pairs)  # {'John': 85, 'Jane': 62, 'Jim': 91}
```

### Zip with multiple lists

```python
names = ["John", "Jane", "Jim"]
scores = [85, 62, 91]
cities = ["New York", "Los Angeles", "Chicago"]

for name, score, city in zip(names, scores, cities):
    print(name, score, city)  # John 85 New York Jane 62 Los Angeles Jim 91 Chicago
```

`zip` stops at the shortest list:

```python
names = ["John", "Jane", "Jim", "Diana"]
scores = [85, 62, 91]

for name, score in zip(names, scores):
    print(name, score)  # John 85 Jane 62 Jim 91  -> it skips Diana because it is not in the scores list
```

## Unpacking

Unpacking a tuple into variables:

```python
coordinate = (10, 20)
x, y = coordinate
print(x)  # 10
print(y)  # 20
```

Unpacking multiple values from a list into variables:

```python
numbers = [1, 2, 3, 4, 5]
a, b, c, d, e = numbers
print(a)  # 1
print(b)  # 2
print(c)  # 3
print(d)  # 4
print(e)  # 5
```

```python
names = ["John", "Jane", "Jim"]
first, second, third = names
print(first)   # John
print(second)  # Jane
print(third)   # Jim
```

```python
numbers = [1, 2, 3, 4, 5]
first, *rest = numbers  # first is the first value, rest is the rest of the values
print(first)  # 1
print(rest)   # [2, 3, 4, 5]
```

```python
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5
```

### Ignore a value

`_` is a convention to use when you are not interested in the value, but there is technically a value there:

```python
person = ("Ada", 36, "London")
name, _, city = person  # ignore 36
print(name)  # Ada
print(city)  # London
print(_)     # 36
```

Ignore multiple values:

```python
person = ("Ada", 36, True, False, "London")
name, age, *_, city = person
print(name)  # Ada
print(age)   # 36
print(city)  # London
```

## Unpacking and packing - combining

List combination:

```python
first = [1, 2, 3]
second = [4, 5, 6]
result = [*first, *second]
print(result)  # [1, 2, 3, 4, 5, 6]
```

Dictionary combination:

```python
defaults = {
    "theme": "light",
    "language": "English"
}

user_settings = {
    "language": "Swedish",
    "notifications": True
}

settings = {
    **defaults,
    **user_settings
}
print(settings)  # {'theme': 'light', 'language': 'Swedish', 'notifications': True}
```

## Lambda functions

Small anonymous functions.

Traditional way:

```python
def double(number):
    return number * 2
print(double(5))  # 10
```

Lambda function:

`lambda parameters: expression` — the result of the expression is returned automatically.

```python
double = lambda number: number * 2
print(double(5))  # 10
```

```python
names = ["John", "Jane", "Jim", "Diana"]
print(sorted(names))  # ['Diana', 'Jane', 'Jim', 'John']
```

Sorted by length, traditional way:

```python
names = ["John", "Jane", "Jim", "Diana"]
def get_length(name):
    return len(name)

sorted_names = sorted(names, key=get_length)
print(sorted_names)  # ['Jim', 'Jane', 'John', 'Diana']
```

Sorted by length with a lambda:

```python
names = ["John", "Jane", "Jim", "Diana"]
sorted_names = sorted(names, key=lambda name: len(name))
print(sorted_names)  # ['Jim', 'Jane', 'John', 'Diana']
```

### Sort dictionaries using a lambda function

```python
students = [
    {"name": "Anna", "score": 85},
    {"name": "Bob", "score": 62},
    {"name": "Charlie", "score": 91}
]

# sort by score
sorted_students = sorted(students, key=lambda student: student["score"])
print(sorted_students)  # [{'name': 'Bob', 'score': 62}, {'name': 'Anna', 'score': 85}, {'name': 'Charlie', 'score': 91}]

# reverse sort by score
sorted_students = sorted(students, key=lambda student: student["score"], reverse=True)
print(sorted_students)  # [{'name': 'Charlie', 'score': 91}, {'name': 'Anna', 'score': 85}, {'name': 'Bob', 'score': 62}]
```

## `map`

Apply a function to each element in a list:

```python
numbers = [1, 2, 3, 4, 5]  # double each number
double = map(lambda number: number * 2, numbers)
print(double)       # <map object ...>
print(list(double))  # [2, 4, 6, 8, 10]
```

List comprehension:

```python
numbers = [1, 2, 3, 4, 5]
double = [number * 2 for number in numbers]
print(double)  # [2, 4, 6, 8, 10]
```

## `filter`

Filter elements in a list — returns the values that are true:

```python
numbers = [1, 2, 3, 4, 5]  # filter even numbers
even = filter(lambda number: number % 2 == 0, numbers)
print(even)       # <filter object ...>
print(list(even))  # [2, 4]
```

List comprehension:

```python
numbers = [1, 2, 3, 4, 5]
even = [number for number in numbers if number % 2 == 0]
print(even)  # [2, 4]
```

## `reduce`

Reduce a list to a single value:

```python
numbers = [1, 2, 3, 4, 5]  # sum of numbers
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15
```
