# Python fundamentals

# Recap
# variables
# strings
# collections
# functions
# loops
# scope
# args and kwargs
# Readability matters


# list comprehension
# # way one to do it (traditional way)
# numbers = [1, 2, 3, 4, 5] # need to multiply for 2

# double_numbers = []

# for numbers in numbers:
#     double_numbers.append(numbers * 2)

# print(double_numbers) # [2, 4, 6, 8, 10]


# # way two to do it (list comprehension)
# double_numbers = [numbers * 2 for numbers in numbers]
# print(double_numbers) # [2, 4, 6, 8, 10]

# Examples

# list numbers, for loop version
# numbers = [1, 2, 3, 4, 5]
# squares = [number ** 2 for number in numbers]
# print(squares) # [1, 4, 9, 16, 25]

# list strings, for loop version
# names = ["John", "Jane", "Jim", "Jill"]
# upper_names = [name.upper()for name in names]
# print(upper_names) # ["JOHN", "JANE", "JIM", "JILL"]


# filter values from a list
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = []

# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)

# print(even_numbers) # [2, 4, 6, 8, 10]

# conditionals in list comprehension
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = [number for number in numbers if number % 2 == 0]
# print(even_numbers) # [2, 4, 6, 8, 10]


# numbers = [1, 2, 3, 4, 5, 6]
# result = [number ** 2 for number in numbers if number % 2 == 0] # condition determines what is added in the new list
# print(result) # [4, 16, 36]


# names = ["John", "Jane", "Jim", "Jill"]
# result = [name for name in names if len(name) >= 4]
# print(result) # ['John', 'Jane', 'Jill']


# several conditions in list comprehension
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = [number for number in numbers if number % 2 == 0 and number % 3 == 0]
# print(result) # [6]


# Dictionary comprehension
# numbers = [1, 2, 3, 4, 5] # -> keys
# squared_numbers = {}

# way one to do it (traditional way)
# for number in numbers:
#     squared_numbers[number] = number ** 2
# print(squared_numbers) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# way two to do it (dictionary comprehension)
# numbers = [1, 2, 3, 4, 5] # -> keys
# squared_numbers = {}
# squared_numbers = {number: number ** 2 for number in numbers} # -> values
# print(squared_numbers) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# dictionary comprehension in a existing dictionary
# prices = {
#     "apple": 10,
#     "banana": 5,
#     "orange": 8
# }

# # double the prices using dictionary comprehension from the existing dictionary
# double_prices = {product: price * 2 for product, price in prices.items()} # we use items() to get the key and value pairs from the dictionary
# print(double_prices) # {"apple": 20, "banana": 10, "orange": 16}


# filter values from a dictionary using dictionary comprehension
# scores = {
#     "Anna": 85,
#     "Bob": 62,
#     "Charlie": 91,
#     "Diana": 70
# }

# # Who passed the exam > 70
# passed = {
#     name: score
#     for name, score in scores.items()
#     if score >= 70
# }
# print(passed) # {'Anna': 85, 'Charlie': 91, 'Diana': 70}


# sets comprehension
# words = ["python", "Java", "python", "C#", "java"]

# lengths = {len(word) for word in words} # -> set because sets are unordered and unique values
# print(lengths) # {2, 3, 4} # unique values


# # Tuples comprehension - generator expression
# numbers = (number * 2 for number in range(5)) # -> tuple because tuples are immutable
# print(numbers) # (0, 2, 4, 6, 8) # generator object, not a tuple


# Remember:
# Readability is the most important thing in programming.
# [ ... ] -> list comprehension
# {key : value ... } -> dictionary comprehension
# { ... } -> set comprehension
# ( ... ) -> generator expression -> for example: (number * 2 for number in range(5))



# Enumerate - gives you the index and the value of the element in the list
# languages = ["Python", "Java", "C#"]

# way one to do it (traditional way)
# for index in range(len(languages)):
#     print(index, languages[index]) # 0 Python, 1 Java, 2 C#

# way two to do it (enumerate)
# for index, languages in enumerate(languages): # unpack the list into index and language in the for loop
#     print(index, languages) # 0 Python, 1 Java, 2 C#

# way three to do it (enumerate with start)
# for position, languages in enumerate(languages, start=1): # start is the index of the first element
#     print(position, languages) # 1 Python, 2 Java, 3 C#

# for language in languages:
#     print(language) # Python, Java, C#

# for index, language in enumerate(languages):
#     print(index, language) # 0 Python, 1 Java, 2 C#


# Zip - combines two lists into a single list of tuples

# names = ["John", "Jane", "Jim"]
# scores = [85, 62, 91]

# way one to do it (traditional way)
# for i in range(len(names)):
#     print(names[i], scores[i]) # John 85 Jane 62 Jim 91

# way two to do it (zip)
# for name, score in zip(names, scores):
#     print(name, score) # John 85 Jane 62 Jim 91

# convert to list
# pairs = list(zip(names, scores))
# print(pairs) # [('John', 85), ('Jane', 62), ('Jim', 91)]

# convert to dictionary
# pairs = dict(zip(names, scores))
# print(pairs) # {'John': 85, 'Jane': 62, 'Jim': 91}

# zip with multiple lists
# names = ["John", "Jane", "Jim"]
# scores = [85, 62, 91]
# cities = ["New York", "Los Angeles", "Chicago"]

# for name, score, city in zip(names, scores, cities):
#     print(name, score, city) # John 85 New York Jane 62 Los Angeles Jim 91 Chicago


# names = ["John", "Jane", "Jim", "Diana"]
# scores = [85, 62, 91]

# for name, score in zip(names, scores):
#     print(name, score) # John 85 Jane 62 Jim 91  -> it skips diana because it is not in the scores list, it stops at the shortest list


# unpacking
# unpacking a tuple into variables
# coordinate = (10, 20)
# x, y = coordinate
# print(x) # 10
# print(y) # 20

# unpacking multiple values from a list into variables
# numbers = [1, 2, 3, 4, 5]
# a, b, c, d, e = numbers
# print(a) # 1
# print(b) # 2
# print(c) # 3
# print(d) # 4
# print(e) # 5

# names = ["John", "Jane", "Jim"]
# first, second, third = names
# print(first) # John
# print(second) # Jane
# print(third) # Jim

# numbers = [1, 2, 3, 4, 5]
# first, *rest = numbers # first is the first value, rest is the rest of the values
# print(first) # 1
# print(rest) # [2, 3, 4, 5]

# numbers = [1, 2, 3, 4, 5]
# first, *middle, last = numbers
# print(first) # 1
# print(middle) # [2, 3, 4]
# print(last) # 5

# unpacking multiple values from a dictionary into variables
# person = {"name": "John", "age": 30, "city": "New York"}
# name, age, city = person
# print(name) # John


# ignore a value
# person = ("Ada", 36, "London")
# # ignore 36
# name, _, city = person # _ is a convention to use when not interested in the value, but there is technically a value there
# print(name) # Ada
# print(city) # London
# print(_) # 36

# ignore multiple values
# person = ("Ada", 36, True, False "London")
# name, age, *_, city = person
# print(name) # Ada
# print(age) # 36
# print(city) # London


# unpacking and packing - combining
#list combination
# first = [1, 2, 3]
# second = [4, 5, 6]
# result = [*first, *second]
# print(result) # [1, 2, 3, 4, 5, 6]

# dictionary combination
# defaults = {
#     "theme": "light",
#     "language": "English"
# }

# user_settings = {
#     "language": "Swedish",
#     "notifications": True
# }

# settings = {
#     **defaults,
#     **user_settings
# }
# print(settings) # {'theme': 'light', 'language': 'Swedish', 'notifications': True}


# Lambda functions - small anonymous functions
# # traditional way
# def double(number):
#     return number * 2
# print(double(5)) # 10

# # Lambda function
# double = lambda number: number * 2 # lambda parameters : expression -> the result of the expression return automatically
# print(double(5)) # 10

# names = ["John", "Jane", "Jim", "Diana"]
# print(sorted(names)) # ['Diana', 'Jane', 'Jim', 'John']

# sorted by length
# traditional way
# names = ["John", "Jane", "Jim", "Diana"]
# def get_length(name):
#     return len(name)

# sorted_names = sorted(names, key=get_length)
# print(sorted_names) # ['Jim', 'Jane', 'John', 'Diana']

# Lambda function
# names = ["John", "Jane", "Jim", "Diana"]
# sorted_names = sorted(names, key=lambda name: len(name))
# print(sorted_names) # ['Jim', 'Jane', 'John', 'Diana']


# sort dictionaries using lambda function

# students = [
#     {"name": "Anna", "score": 85},
#     {"name": "Bob", "score": 62},
#     {"name": "Charlie", "score": 91}
# ]

# # sort by score
# sorted_students = sorted(students, key=lambda student: student["score"])
# print(sorted_students) # [{'name': 'Bob', 'score': 62}, {'name': 'Anna', 'score': 85}, {'name': 'Charlie', 'score': 91}]

# reverse sort by score
# sorted_students = sorted(students, key=lambda student: student["score"], reverse= True)
# print(sorted_students) # [{'name': 'Charlie', 'score': 91}, {'name': 'Anna', 'score': 85}, {'name': 'Bob', 'score': 62}]


# map function - apply a function to each element in a list

# numbers = [1, 2, 3, 4, 5] # double each number
# double = map(lambda number: number * 2, numbers)
# print(double) # <map object at 0x7f51a0100000>
# print(list(double)) # [2, 4, 6, 8, 10]


# list comprehension
# numbers = [1, 2, 3, 4, 5] # double each number
# double = [number * 2 for number in numbers]
# print(double) # [2, 4, 6, 8, 10]



# filter function - filter elements in a list -> returns a filter that are true
# numbers = [1, 2, 3, 4, 5] # filter even numbers
# even = filter(lambda number: number % 2 == 0, numbers)
# print(even) # <filter object at 0x7f51a0100000>
# print(list(even)) # [2, 4]

# list comprehension
# numbers = [1, 2, 3, 4, 5] # filter even numbers
# even = [number for number in numbers if number % 2 == 0]
# print(even) # [2, 4]

# reduce function - reduce a list to a single value
# numbers = [1, 2, 3, 4, 5] # sum of numbers
# total = reduce(lambda x, y: x + y, numbers)
# print(total) # 15

# list comprehension
# numbers = [1, 2, 3, 4, 5] # sum of numbers
# total = [number for number in numbers]
# print(total) # 15

# any() and all()
# any() returns True if at least one item is True.
# numbers = [1, 3, 5, 8]
# result = any(number % 2 == 0 for number in numbers)
# print(result) # True

# all() returns True only if every item is True.
# numbers = [2, 4, 6, 8]
# result = all(number % 2 == 0 for number in numbers)
# print(result) # True
