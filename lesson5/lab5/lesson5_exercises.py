# Lab 5 - Functions and Scope

# Part A - Scope
# 1 - Create a global variable course_name and a function that creates a local variable with the same name. Print both and explain the result.

# curse_name = "Python - AI and ML"

# def local_scope():
#     curse_name = "Machine Learning"
#     print(curse_name)

# local_scope() # Machine Learning
# print(curse_name) # Python - AI and ML
#  # local scope is only available inside the function, while global scope is available everywhere in the file

 # 2 - Create a function with a local counter and show that it does not remain available outside the function.
# def print_sentence(sentence):
#     count = 0
#     for char in sentence:
#         count += 1
#     print(count) # 13
#     print(sentence)

# print_sentence("Hello, world!") # 13 Hello, world!
# # print(count) # NameError: name 'count' is not defined - count is a local variable inside the function


# 3 - Create a function that attempts to modify a global numeric variable without global. Observe/describe the problem, then rewrite the design to return the new value instead.

# def modify_global_variable():
#     number += 1
#     return number
# print(modify_global_variable())
# # Problem: The function does not modify the global variable, because it is not declared

# number = 0
# def modify_global_variable():
#     new_number = number + 1
#     return new_number

# print(modify_global_variable()) # 1


# 4- Create a nested function and demonstrate a simple enclosing-scope lookup.

# def outer():
#     message = "outer message"
#     def inner():
#         print(message)
#     inner()
# outer() # outer message
# # inner() # NameError: name 'inner' is not defined out side the function


# 5 -Create examples that avoid shadowing built-ins such as list, str, sum and max.

# list = [1, 2, 3, 4, 5] -> numbers = [1, 2, 3, 4, 5]
# str = "Hello, world!" -> text = "Hello, world!"
# sum = 1 + 2 + 3 + 4 + 5 -> total = 1 + 2 + 3 + 4 + 5
# max = max(1, 2, 3, 4, 5) -> highest = max(1, 2, 3, 4, 5)


#Part B - *args
# 1 -Write add_all(*numbers) returning the sum without sum().
# def add_all(*numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     return total

# print(add_all(1, 2, 3)) # 6
# print(add_all(1, 2, 3, 6)) # 12


# 2 - Write average(*numbers). Decide what should happen when no numbers are supplied.

# def average(*numbers):
#     if numbers:
#         print(numbers)
#     else:
#         print("There are not numbers to calculate average")

# average() # There are not numbers to calculate average
# average(1, 2, 3) # (1, 2, 3)


# 3 - Write longest_word(*words) returning the longest word.

# def longest_word(*words):
#     longest = ""
#     for word in words:
#         if len(word) > len(longest):
#             longest = word
#     return longest

# print(longest_word("amor", "advance", "Python", "language")) # language


# 4- Write build_sentence(separator, *words) returning one joined string.
# def build_sentence(separator, *words):
#     sentence = ""
#     for word in words:
#         if sentence:
#             sentence = sentence + separator + word
#         else:
#             sentence = word
#     return sentence

# print(build_sentence("-", "python", "is", "fun")) # python-is-fun


# 5 - Write describe_scores(student_name, *scores) returning name, number of scores and average.

# def describe_scores(student_name, *scores):
#     number_scores = 0
#     sum_scores = 0
#     for score in scores:
#         number_scores += 1
#         sum_scores += score

#     average = sum_scores/number_scores

#     return student_name, number_scores, average

# print(describe_scores("Mateo", 25, 75, 85, 90, 45, 60)) # ('Mateo', 6, 63.333333333333336)


#Part C - Positional unpacking
# 1 - Create a list [10, 20, 30] and unpack it into a function expecting three positional parameters.
# numbers = [10, 20, 30]

# def add(a, b, c):
#     print(a, b, c) # 10 20 30
#     return a + b + c

# print(add(*numbers)) # 60


# 2 - Create a tuple containing first_name, last_name, city and call a function using *tuple.
# person = ("Cecilia", "Morales", "Stockholm")

# def introduction(first_name, last_name, city):
#     print(f"Personal data: {first_name}, {last_name}, {city}")

# introduction(*person) # Personal data: Cecilia, Morales, Stockholm


# 3 - Use starred assignment: first, *middle, last = values. Test with several list lengths.
# def add(first, *middle, last = 1):
#     total = 0
#     for element in middle:
#         total += element
#     print(first) # 0
#     print(last) # 1
#     print(total) # 5
#     return first + total + last

# print(add(0,1, 1, 1, 2)) # 6
# print(add(1, 1)) # 3
# print(add(1)) # 2


# 4 -Explain in comments the difference between * in a function definition and * in a function call.
# * in a function definition is used to collect the parameters into a tuple
# * in a function call is used to unpack the arguments - take the elements of a collection and pass them as separate values to the function


#Part D - **kwargs
# 1 - Write show_profile(**info) and iterate over all key/value pairs.
# def show_profile(**info):
#     for key, value in info.items():
#         print(f"{key} : {value}")

# show_profile(name="John", age=36, city="London", languages="Python")
# # name : John
# # age : 36
# # city : London
# # languages : Python


# 2 - Write create_user(username, **details) returning one dictionary containing username plus all supplied details.
# def create_user(username, **details): # ** collects keyword arguments into a dictionary.
#     user = {
#         "username": username,
#         **details # unpacks the dictionary's key-value pairs.
#     }
#     return user

# print(create_user("gmorales", email="john@example.com", phone="1234567890"))
# # {'username': 'gmorales', 'email': 'john@example.com', 'phone': '1234567890'}

# 3 - Write build_product(name, price, **metadata) returning a dictionary.
# def build_product(name, price, **metadata):
#     product = {
#         "name": name,
#         "price": price,
#         **metadata
#     }
#     return product

# print(build_product("orange", 15, weight = 0.5, country = "spain", ref = 14588, available = True))
# # {'name': 'orange', 'price': 15, 'weight': 0.5, 'country': 'spain', 'ref': 14588, 'available': True}


# 4 - Write a function that accepts **settings and returns only settings whose value is not None.
# def check_settings(**settings):
#     filtered_settings = {}
#     for key, value in settings.items():
#         if value is not None:
#             filtered_settings[key] = value
#     return filtered_settings

# print(check_settings(is_opened = True, is_closed = None, color = None, height = 15))
# # {'is_opened': True, 'height': 15}


# 5 - Call a normal named-parameter function using ** dictionary unpacking. Ensure dictionary keys match parameter names.
# person = {"name": "John", "age": 36, "city": "London"}

# def format_person_info(name, age, city):
#     return f"{name} is {age} years old and live in {city}"

# print(format_person_info(**person)) # John is 36 years old and live in London


#Part E - Combining parameters
# 1 - Create log_event(event_type, *messages, **metadata) returning a structured dictionary.
# def log_event(event_type, *messages, **metadata):
#     log_event_dic = {
#         "event_type": event_type,
#         "messages" : list(messages),
#         "metadata" : metadata
#     }
#     return log_event_dic

# print(log_event("login", "User logged in", "Login was successful", username="gmorales", ip_address="192.168.1.10", device="MacBook"))
# # {'event_type': 'login', 'messages': ['User logged in', 'Login was successful'], 'metadata': {'username': 'gmorales', 'ip_address': '192.168.1.10', 'device': 'MacBook'}}


# 2 - Create calculate_order(customer, *prices, **options). Support an optional discount and shipping fee in options.
# def calculate_order(customer, *prices, **options):
#     subtotal = sum(prices)
#     discount = options.get("discount", 0)
#     shipping = options.get("shipping", 0)

#     total = subtotal - discount + shipping
#     return {
#         "customer" : customer,
#         "total" : total
#     }

# print(calculate_order("Gloria", 10, 15, 20, discount=10, shipping=15)) # {'customer': 'Gloria', 'total': 50}
# print(calculate_order("Gloria", 10, 15, 20, discount=10)) # {'customer': 'Gloria', 'total': 35}
# print(calculate_order("Gloria", 10, 15, 20)) # {'customer': 'Gloria', 'total': 45}


# 3- Create a function where explicit named parameters would be clearer than **kwargs. Write both versions and compare readability in comments.
# Version 1: explicit named parameters
# This is clearer because we can see exactly what information the function expects.

# def create_profile(name, age, city, email):
#     return {
#         "name": name,
#         "age": age,
#         "city": city,
#         "email": email
#     }

# print(create_profile("Gloria", 30, "Stockholm", "gloria@example.com"))

# Version 2: using **kwargs
# This is more flexible, but less clear because we don't know which parameters the function expects.

# def create_profile_kwargs(**kwargs):
#     return kwargs

# print(create_profile_kwargs(name="Gloria", age=30, city="Stockholm", email="gloria@example.com"))

# Comparison:
# Explicit parameters are easier to read and understand when the function has a fixed set of expected values.
# **kwargs is more flexible when the number or names of the arguments can vary.


# 4- Create at least three calls to the same flexible function with substantially different numbers of arguments.
# def add_numbers(*args):
#     total = 0

#     for number in args:
#         total += number
#     return total

# print(add_numbers(10, 20, 30)) # 60
# print(add_numbers(1, 2, 3, 4, 5)) # 15
# print(add_numbers(1)) # 1
# print(add_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) # 66
# print(add_numbers(-1, -2, -3, -4, -5)) # -15


#Part F - Applied challenge: Report builder
# 1 Build a flexible report system without files. create_report(title, *sections, **metadata) should return a dictionary.
def create_report(title, *sections, **metadata):
    report = {
        "title" : title,
        "sections" : list(sections),
        "metadata" : metadata
    }
    return report

# 2 Each section can be a string or a small dictionary; choose and document your design.
sections = ["Introduction", "Methods", "Result", "Conclusion"] # sections is a list of strings

# 3 Metadata may include author, department, version, confidential and date.
metadata = {
    "author" : "Gloria Morales",
    "department": "plan1",
    "version": 1,
    "confidential": True,
    "date" : "2026-07-22"
}

report = create_report("Python Functions", *sections, **metadata )

# print(report)
# {'title': 'Python Functions', 'sections': ['Introduction', 'Methods', 'Result', 'Conclusion'], 'metadata': {'author': 'Gloria Morales', 'department': 'plan1', 'version': 1, 'confidential': True, 'date': '2026-07-22'}}


# 4 Write summarize_report(report) that returns a readable multi-line string.
def summarize_report(report):
    return(
        f"Report: {report["title"]}\n"
        f"Sections: {report["sections"]}\n"
        f"Author: {report["metadata"]["author"]}\n"
        f"Date: {report["metadata"]["date"]}"
    )

# print(summarize_report(report))
# Report: Python Functions
# Sections: ['Introduction', 'Methods', 'Result', 'Conclusion']
# Author: Gloria Morales
# Date: 2026-07-22


# 5 Write count_words(*sections) that counts words across all supplied textual sections.
def count_words(*sections):
    count = 0
    for section in sections:
        words = section.split()
        count += len(words)
    return count

print(count_words(*sections)) # 4


# 6 Use dictionary unpacking to create at least two reports from predefined metadata dictionaries.

sections2 = ["a", "b"]
metadata2 = {
    "author" : "Anna",
    "department": "plan1plan2",
    "version": 5,
    "confidential": False,
    "date" : "2021-01-21"
}

report2 = create_report("Python Functions", *sections2, **metadata2 )
# print(report2)
#{'title': 'Python Functions', 'sections': ['a', 'b'], 'metadata': {'author': 'Anna', 'department': 'plan1plan2', 'version': 5, 'confidential': False, 'date': '2021-01-21'}}

sections3 = ["j", "k", "l"]
metadata3 = {
    "author" : "Sara",
    "department": "abc",
    "version": 2,
    "confidential": True,
    "date" : "1988-12-16"
}

report3 = create_report("Python Functions", *sections3, **metadata3 )
# print(report3)
# {'title': 'Python Functions', 'sections': ['j', 'k', 'l'], 'metadata': {'author': 'Sara', 'department': 'abc', 'version': 2, 'confidential': True, 'date': '1988-12-16'}}

# 7 Demonstrate at least one case where your function deliberately ignores or handles a missing optional metadata field.
def show_metadata(**kwargs):
    print("Author:", kwargs.get("author","Unknown"))
    print("Email:", kwargs.get("email","Unknown"))

# show_metadata(**metadata)
# Author: Gloria Morales
# Email: Unknown

#TODO
#Part G - Stretch challenges
# 1 Write merge_settings(defaults, **overrides) returning a new dictionary without modifying defaults.
# 2 Write call_summary(function_name, *args, **kwargs) returning a string describing what would be called.
# 3 Write a flexible statistics function that returns count, total, average, min and max for *numbers. Implement the calculations manually where reasonable.
# 4 Create five 'predict the output' scope questions and verify your predictions.
