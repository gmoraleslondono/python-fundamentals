# Lab 6
# Part A - List comprehensions
#1 Create squares for numbers 1-20 using a normal loop, then a list comprehension.
# normal loop
# squares = []
# for number in range(1,(20+1)):
#     squares.append(number ** 2)
# print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]

# list comprehension
# squares = [number ** 2 for number in range(1,(20+1))]
# print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]


# 2 Create a list containing only even numbers from 1-100.
# even_numbers = [number for number in range(1, (100+1)) if number % 2 == 0]
# print(even_numbers)
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]


# 3 Convert a list of names to stripped, title-cased names.
# names = ["John lennon ", "  jane doe ", "   JIM LIN "]
# title_cased_names = [name.strip().title() for name in names]
# print(title_cased_names) # ['John Lennon', 'Jane Doe', 'Jim Lin']


# 4 Given scores, create a list containing only passing scores.
# scores = [95, 65, 40, 55, 80, 35, 75, 35]
# passing_scores = [score for score in scores if score >= 55]
# print(passing_scores) # [95, 65, 55, 80, 75]


# 5 Create labels such as 'PASS'/'FAIL' for every score using a conditional expression in a comprehension.
# scores = [95, 65, 40, 55, 80, 35, 75, 35]
# label_scores = {score: "PASS" if score >= 50  else "FAIL" for score in scores}
# print(label_scores) # {95: 'PASS', 65: 'PASS', 40: 'FAIL', 55: 'PASS', 80: 'PASS', 35: 'FAIL', 75: 'PASS'}


# 6 Rewrite three earlier loop-based transformations from Lessons 2-4 as comprehensions.
# # 1 - Find the multiples of 3 -> Fizz 5 -> Buzz Both -> FizzBuzz
# Traditional way
# for number in range(1, (100+1)):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# List comprehension way
# fizz_buzz = [
#     "FizzBuzz" if number % 3 == 0 and number % 5 == 0
#     else "Fizz" if number % 3 == 0
#     else "Buzz" if number % 5 == 0
#     else number
#     for number in range(1, (100+1))
# ]
# print(fizz_buzz) # [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'FizzBuzz', 31, 32, 'Fizz', 34, 'Buzz', 'Fizz', 37, 38, 'Fizz', 'Buzz', 41, 'Fizz', 43, 44, 'FizzBuzz', 46, 47, 'Fizz', 49, 'Buzz', 'Fizz', 52, 53, 'Fizz', 'Buzz', 56, 'Fizz', 58, 59, 'FizzBuzz', 61, 62, 'Fizz', 64, 'Buzz', 'Fizz', 67, 68, 'Fizz', 'Buzz', 71, 'Fizz', 73, 74, 'FizzBuzz', 76, 77, 'Fizz', 79, 'Buzz', 'Fizz', 82, 83, 'Fizz', 'Buzz', 86, 'Fizz', 88, 89, 'FizzBuzz', 91, 92, 'Fizz', 94, 'Buzz', 'Fizz', 97, 98, 'Fizz', 'Buzz']

# # 2 -  Text histogram: for each number in [3, 5, 2] print that many *
# Traditional way
# numbers = [3, 5, 2]
# for number in numbers:
#     print("*" * number)

# List comprehension
# numbers = [3, 5, 2]
# histogram = ["*" * number for number in numbers]
# print(histogram) # ['***', '*****', '**']

# 3
# Traditional way
# words = ["airplane", "yes", "no", "class", "studies" ]
# def get_long_word(words, minimum_length):
#     long_words = []
#     for word in words:
#         if len(word) >= minimum_length:
#             long_words.append(word)
#     return long_words

# result = get_long_word(words, 5)
# print(result) # ['airplane', 'class', 'studies']

# list comprehension
# words = ["airplane", "yes", "no", "class", "studies" ]
# def get_long_word(words, minimum_length):
#     long_words = [word for word in words if len(word) >= minimum_length]
#     return long_words

# result = get_long_word(words, 5)
# print(result) # ['airplane', 'class', 'studies']


# Part B - Dictionary and set comprehensions
# 1 Create a dictionary mapping numbers 1-10 to their squares.
# squared_numbers = {number: number ** 2 for number in range(1, (10+1))}
# print(squared_numbers) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


# 2 Given a list of words, create a dictionary mapping each word to its length.
# words = ["airplane", "yes", "no", "class", "studies" ]

# words_map = { word: len(word) for word in words}
# print(words_map) # {'airplane': 8, 'yes': 3, 'no': 2, 'class': 5, 'studies': 7}


# 3 Given a list with duplicates, create a set comprehension containing lowercase normalized values.
# words = ["Airplane", "YeS", "no", "CLASS", "studies", "Airplane", "no", "CLASS"]
# normalized_words = {word.strip().lower() for word in words}
# print(normalized_words) # {'yes', 'no', 'class', 'airplane', 'studies'}


# 4 Create a dictionary of only products whose price is below a chosen threshold.
# products = [
#     {"product": "orange", "price": 10, "stock": 100},
#     {"product": "apple", "price": 20, "stock": 200},
#     {"product": "banana", "price": 30, "stock": 300},
#     {"product": "pear", "price": 40, "stock": 400},
#     {"product": "pineapple", "price": 50, "stock": 500},
# ]
# threshold = 30

# lower_prices = {product["product"] : product["price"] for product in products if product["price"] <= threshold}
# print(lower_prices) # {'orange': 10, 'apple': 20, 'banana': 30}


# 5 Create a dictionary mapping student names to PASS/FAIL from a list of student dictionaries.
# students = [
#     {"name": "John", "age": 30, "city": "New York", "score": 75},
#     {"name": "Eva", "age": 25, "city": "Los Angeles", "score": 80},
#     {"name": "Mike", "age": 35, "city": "Chicago", "score": 62}
# ]

# passed_fails_score = {student["name"]: student["score"] for student in students if student["score"] >= 70 }
# print(passed_fails_score) # {'John': 75, 'Eva': 80}


# Part C - enumerate
# 1 Print a playlist with numbering starting at 1 using enumerate.
# playlist = ["track1", "track2", "track3", "track4", "track5"]

# for position, track in enumerate(playlist, start=1):
#     print(position, track)

# # 1 track1
# # 2 track2
# # 3 track3
# # 4 track4
# # 5 track5


# 2 Given a list of tasks, print 'Task 1:', 'Task 2:' etc.
# tasks = ["laundry", "groceries", "homework", "dinner", "sleep"]

# for position, task in enumerate(tasks, start=1):
#     print(f"Task {position}: {task}")

# # Task 1: laundry
# # Task 2: groceries
# # Task 3: homework
# # Task 4: dinner
# # Task 5: sleep


# 3 Find and print indexes of all values above a threshold.
# numbers = [1, 0, 5, -4, 10,80, 69, -20, 12, -8, 7, 999, 5, -15, 6, 55]
# threshold = 50

# for position, number in enumerate(numbers):
#     if number >= threshold:
#         print(position) # 5 6 11 15


# 4 Rewrite a range(len(...)) loop using enumerate and explain why the new version is clearer.
# Using range(len(...)) loop
# numbers = [1, 0, 5, -4, 10,80, 69, -20, 12, -8, 7, 999, 5, -15, 6, 55]
# threshold = 50

# for position in range(len(numbers)):
#     if numbers[position] >= threshold:
#         print(position) # 5 6 11 15

# Using enumerate
# numbers = [1, 0, 5, -4, 10,80, 69, -20, 12, -8, 7, 999, 5, -15, 6, 55]
# threshold = 50

# for position, number in enumerate(numbers):
#     if number >= threshold:
#         print(position) # 5 6 11 15

# the new version is clearer because it is more readable and easier to understand.

# Part D - zip and unpacking
# 1 Combine separate name and score lists using zip and print each pair.
# names = ["John", "Jane", "Jim", "Diana"]
# scores = [85, 62, 91, 78]

# for name, score in zip(names, scores):
#     print(name, score)
# # John 85
# # Jane 62
# # Jim 91
# # Diana 78


# 2 Create a dictionary using dict(zip(keys, values)).
# names = ["John", "Jane", "Jim", "Diana"]
# scores = [85, 62, 91, 78]

# students = dict(zip(names, scores))
# print(students) # {'John': 85, 'Jane': 62, 'Jim': 91, 'Diana': 78}


# 3 Combine three lists: product name, price and stock.
# product_names = ["apple", "banana", "cherry"]
# prices = [1.00, 2.00, 3.00]
# stocks = [100, 200, 300]

# products = list(zip(product_names, prices, stocks))
# print(products) # [('apple', 1.0, 100), ('banana', 2.0, 200), ('cherry', 3.0, 300)]


# 4 Investigate what happens when zipped lists have different lengths.
# When zipped lists have different lengths, the standard zip() function in Python automatically stops at the end of the shortest list and ignores any extra elements in the longer lists


# 5 Use tuple unpacking directly in a for loop over zipped data.
# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 22]

# for name, age in zip(names, ages):
#     print(f"{name} is {age} years old") # unpacks each tuple directly into name and age.
# # Alice is 25 years old
# # Bob is 30 years old
# # Charlie is 22 years old


# 6 Swap two variables without a temporary variable.
# a = 10
# b = 20
# a, b = b, a
# print(a, b) # 20 10


# Part E - sorted and lambda
# 1 Sort a list of words by length using sorted(..., key=...).
# words = ["which", "words", "should", "I", "sort"]

# sorted_words = sorted(words, key=lambda word:len(word))
# print(sorted_words) # ['I', 'sort', 'which', 'words', 'should']


# 2 Sort a list of student dictionaries by score ascending and descending.
# students = [
#     {"name": "John", "age": 30, "city": "New York", "score": 75},
#     {"name": "Eva", "age": 25, "city": "Los Angeles", "score": 80},
#     {"name": "Mike", "age": 35, "city": "Chicago", "score": 62}
# ]
# sort_ascending_score = sorted(students, key=lambda student: student["score"])
# print(sort_ascending_score)
# # [{'name': 'Mike', 'age': 35, 'city': 'Chicago', 'score': 62}, {'name': 'John', 'age': 30, 'city': 'New York', 'score': 75}, {'name': 'Eva', 'age': 25, 'city': 'Los Angeles', 'score': 80}]

# sort_descending_score = sorted(students, key=lambda student: student["score"], reverse=True)
# print(sort_descending_score)
# # [{'name': 'Eva', 'age': 25, 'city': 'Los Angeles', 'score': 80}, {'name': 'John', 'age': 30, 'city': 'New York', 'score': 75}, {'name': 'Mike', 'age': 35, 'city': 'Chicago', 'score': 62}]


# 3 Sort products by price using a lambda.
# products = [
#     {"product": "apple", "price": 20, "stock": 200},
#     {"product": "pear", "price": 40, "stock": 400},
#     {"product": "banana", "price": 30, "stock": 300},
#     {"product": "orange", "price": 10, "stock": 100},
#     {"product": "pineapple", "price": 50, "stock": 500},
# ]

# sorted_products = sorted(products, key=lambda product:product["price"])
# print(sorted_products)
# #[{'product': 'orange', 'price': 10, 'stock': 100}, {'product': 'apple', 'price': 20, 'stock': 200}, {'product': 'banana', 'price': 30, 'stock': 300}, {'product': 'pear', 'price': 40, 'stock': 400}, {'product': 'pineapple', 'price': 50, 'stock': 500}]


# 4 Sort people by last name when each item is a dictionary containing first_name and last_name.
# users = [
#     {"first_name": "John", "last_name": "Doe"},
#     {"first_name": "Jane", "last_name": "Smith"},
#     {"first_name": "Jim", "last_name": "Beam"},
#     {"first_name": "Diana", "last_name": "Prince"},
# ]

# sorted_by_last_name = sorted(users, key=lambda user:user["last_name"])
# print(sorted_by_last_name)
# # {'first_name': 'Jim', 'last_name': 'Beam'}, {'first_name': 'John', 'last_name': 'Doe'}, {'first_name': 'Diana', 'last_name': 'Prince'}, {'first_name': 'Jane', 'last_name': 'Smith'}]


# 5 Write a normal named function for a sort key, then replace it with lambda. Compare when each is clearer.
# users = [
#     {"first_name": "John", "last_name": "Doe"},
#     {"first_name": "Jane", "last_name": "Smith"},
#     {"first_name": "Jim", "last_name": "Beam"},
#     {"first_name": "Diana", "last_name": "Prince"},
# ]

# def get_last_name(user):
#     return user["last_name"]

# sorted_by_last_name = sorted(users, key=get_last_name)
# print(sorted_by_last_name)
# # {'first_name': 'Jim', 'last_name': 'Beam'}, {'first_name': 'John', 'last_name': 'Doe'}, {'first_name': 'Diana', 'last_name': 'Prince'}, {'first_name': 'Jane', 'last_name': 'Smith'}]


# Part F - Applied challenge: Data cleanup
# 1 Start with a list of at least twelve messy dictionaries representing products: inconsistent name casing/spacing, category, price and stock.
products = [
    {"product": "milk", "category": "dairy", "price": 25, "stock": 100},
    {"product": "ORANGE", "category": "fruit", "price": 10, "stock": 0},
    {"product": "BREAD", "category": "bakery", "price": 35, "stock": 80},
    {"product": "CHICKEN", "category": "meat", "price": 90, "stock": 40},
    {"product": "APPLE", "category": "fruit", "price": 20, "stock": 200},
    {"product": "cheese", "category": "dairy", "price": 45, "stock": 0},
    {"product": "PINEAPPLE", "category": "fruit", "price": 50, "stock": 500},
    {"product": "BEEF", "category": "meat", "price": 120, "stock": 0},
    {"product": "croissant", "category": "bakery", "price": 30, "stock": 50},
    {"product": "banana", "category": "fruit", "price": 30, "stock": 300},
    {"product": "YOGURT", "category": "dairy", "price": 20, "stock": 150},
    {"product": "pork", "category": "meat", "price": 100, "stock": 0}
]

# 2 Create a cleaned list where names/categories are normalized. Use comprehensions where readable.
normalized_products = [
    {"product" : product["product"].strip().title(),
    "category" : product["category"],
    "price" : product["price"],
    "stock" : product["stock"]}
    for product in products]
# print(normalized_products)
# [{'product': 'Milk', 'category': 'dairy', 'price': 25, 'stock': 100}, {'product': 'Orange', 'category': 'fruit', 'price': 10, 'stock': 0}, {'product': 'Bread', 'category': 'bakery', 'price': 35, 'stock': 80}, {'product': 'Chicken', 'category': 'meat', 'price': 90, 'stock': 40}, {'product': 'Apple', 'category': 'fruit', 'price': 20, 'stock': 200}, {'product': 'Cheese', 'category': 'dairy', 'price': 45, 'stock': 0}, {'product': 'Pineapple', 'category': 'fruit', 'price': 50, 'stock': 500}, {'product': 'Beef', 'category': 'meat', 'price': 120, 'stock': 0}, {'product': 'Croissant', 'category': 'bakery', 'price': 30, 'stock': 50}, {'product': 'Banana', 'category': 'fruit', 'price': 30, 'stock': 300}, {'product': 'Yogurt', 'category': 'dairy', 'price': 20, 'stock': 150}, {'product': 'Pork', 'category': 'meat', 'price': 100, 'stock': 0}]


# 3 Create a list of in-stock products.
in_stock_products = [
    {"product" : product["product"].strip().title(),
    "category" : product["category"],
    "price" : product["price"],
    "stock" : product["stock"]}
    for product in normalized_products
    if product["stock"]> 0]

# print(in_stock_products)
# [{'product': 'Milk', 'category': 'dairy', 'price': 25, 'stock': 100}, {'product': 'Bread', 'category': 'bakery', 'price': 35, 'stock': 80}, {'product': 'Chicken', 'category': 'meat', 'price': 90, 'stock': 40}, {'product': 'Apple', 'category': 'fruit', 'price': 20, 'stock': 200}, {'product': 'Pineapple', 'category': 'fruit', 'price': 50, 'stock': 500}, {'product': 'Croissant', 'category': 'bakery', 'price': 30, 'stock': 50}, {'product': 'Banana', 'category': 'fruit', 'price': 30, 'stock': 300}, {'product': 'Yogurt', 'category': 'dairy', 'price': 20, 'stock': 150}]


# 4 Create a set of unique normalized categories.
unique_categories = set([product["category"] for product in products])
# print(unique_categories) # {'dairy', 'fruit', 'meat', 'bakery'}


# 5 Create a dictionary mapping product name to inventory value (price * stock).
inventory_value = [{"product": product["product"], "inv_value": product["price"]*product["stock"]} for product in normalized_products]
# print(inventory_value)
# [{'product': 'Milk', 'inv_value': 2500}, {'product': 'Orange', 'inv_value': 0}, {'product': 'Bread', 'inv_value': 2800}, {'product': 'Chicken', 'inv_value': 3600}, {'product': 'Apple', 'inv_value': 4000}, {'product': 'Cheese', 'inv_value': 0}, {'product': 'Pineapple', 'inv_value': 25000}, {'product': 'Beef', 'inv_value': 0}, {'product': 'Croissant', 'inv_value': 1500}, {'product': 'Banana', 'inv_value': 9000}, {'product': 'Yogurt', 'inv_value': 3000}, {'product': 'Pork', 'inv_value': 0}]


# 6 Sort products by inventory value from highest to lowest.
sorted_products = sorted(inventory_value, key=lambda product:product['inv_value'], reverse=True)
# print(sorted_products)
# [{'product': 'Pineapple', 'inv_value': 25000}, {'product': 'Banana', 'inv_value': 9000}, {'product': 'Apple', 'inv_value': 4000}, {'product': 'Chicken', 'inv_value': 3600}, {'product': 'Yogurt', 'inv_value': 3000}, {'product': 'Bread', 'inv_value': 2800}, {'product': 'Milk', 'inv_value': 2500}, {'product': 'Croissant', 'inv_value': 1500}, {'product': 'Orange', 'inv_value': 0}, {'product': 'Cheese', 'inv_value': 0}, {'product': 'Beef', 'inv_value': 0}, {'product': 'Pork', 'inv_value': 0}]


# 7 Use enumerate to print a ranked report.
# for position, product in enumerate(sorted_products, start=1):
    # print(f"{position}. {product["product"]}")
# 1. Pineapple
# 2. Banana
# 3. Apple
# 4. Chicken
# 5. Yogurt
# 6. Bread
# 7. Milk
# 8. Croissant
# 9. Orange
# 10. Cheese
# 11. Beef
# 12. Pork


# 8 Use zip to combine at least one pair of separate derived lists in a meaningful way.
names = ["John", "Jane", "Jim", "Diana"]
ages = [25, 30, 22, 28]

users = dict(zip(names, ages))
# print(users) # {'John': 25, 'Jane': 30, 'Jim': 22, 'Diana': 28}


# 9 Write both a deliberately over-complicated comprehension and a clearer alternative. Explain why the clearer version wins.
# over-complicated comprehension
print_products = [product["product"] for product in normalized_products if product["stock"] > 0 and product["price"] > 0]
# print(print_products)
# ['Milk', 'Bread', 'Chicken', 'Apple', 'Pineapple', 'Croissant', 'Banana', 'Yogurt']

# clearer alternative print a list with the products
result = []
for product in normalized_products:
    if product["stock"] > 0 and product["price"] > 0:
        result.append(product["product"])
# print(result)
# ['Milk', 'Bread', 'Chicken', 'Apple', 'Pineapple', 'Croissant', 'Banana', 'Yogurt']

# the clearer version is easier to read and understand, each line is self-explanatory and the code is more readable.

#TODO
# Part G - Stretch challenges
# 1 Flatten a simple list of lists using a comprehension.
list_of_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten_list = [number for list in list_of_list for number in list]
# print(flatten_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 2 Create a multiplication table structure using a nested comprehension, then decide whether the result is readable enough.
table = [
    [column * row for column in range(1, 6)]
    for row in range(1, 6)
]
# print(table)
# [[1, 2, 3, 4, 5],
# [2, 4, 6, 8, 10],
# [3, 6, 9, 12, 15],
# [4, 8, 12, 16, 20],
# [5, 10, 15, 20, 25]]


# 3 Given names and scores, create only passing student dictionaries in one readable comprehension.
names = ["John", "Jane", "Jim", "Diana"]
scores = [85, 62, 91, 78]
passing_students = [{"name":name, "score":score} for name, score in zip(names, scores) if score >= 70]
# print(passing_students)
# [{'name': 'John', 'score': 85}, {'name': 'Jim', 'score': 91}, {'name': 'Diana', 'score': 78}]


# 4 Use any() and all() to answer useful questions about a score list, after first solving them with loops.
scores = [85, 62, 91, 78]
is_positive = any(number > 0 for number in scores)
# print(is_positive) # True

big_numbers = all(number >= 50 for number in scores)
# print(big_numbers) # True


# 5 Create five examples where Pythonic syntax reduces boilerplate without reducing clarity.
numbers = [2, 13, 4, 6, 9, 8, 10, 11, 5, 12, 14, 7, 16, 18, 3, 20]
multiply_numbers = [number*2 for number in numbers]

sorted_numbers = sorted(numbers, key=lambda number:len(str(number)), reverse=True)

big_numbers = [number for number in numbers if number >= 10]

odd_number = any(number % 2 != 0 for number in numbers)

stringify_numbers = [str(number) for number in numbers]
