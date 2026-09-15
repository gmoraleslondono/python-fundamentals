# Class 5 - Python fundamentals

#recap
# def calculate_total(price, quantity):
#     return price * quantity

# total = calculate_total(10, 2)
# print(total)
# parameters
# arguments
# order matters
# what is return doing? - it returns a value to the caller


# scope

# def greet():
#     message = "Hello from the function" # local variable - local scope
#     print(message)

# greet()
# print(message) # NameError: name 'message' is not defined (it is a local variable inside the function)

# message = "Hello from the global scope" # global scope
# def greet():
#     print(message) #It can access the global scope

# greet()


# message = "Global message"
# def greet():
#     message = "Local message"
#     print(message)

# greet() # Local message
# print(message) # Global message


# def greet(name): # name behave as a variable inside the function
#     message = "Hello " + name
#     print(message)

# greet("John") # Hello John

# print(name) # NameError: name 'name' is not defined (it is a local variable inside the function)
# scope is useful to use temporarily variables inside the function without polluting the global scope
# lookup rules: LEGB rule (Local, Enclosing, Global, Built-in) Python looks for variables in this order

# name = "Global Ada"

# def greet():
#     name = "Local Ada"
#     print(name)

# greet() # Local Ada
# print(name) # Global Ada


# numbers = [1, 2, 3]
# print(len(numbers)) # built-in function


# list = [1, 2, 3]
# print(list)

# new_list = list("Python") # 'list' object is not callable - built-in function will not be used as a variable name

# avoid using built-in function names as variable names: list str int print sum max min


# enclosing scope

# def outer():
#     message = "outer message"
#     def inner():
#         print(message)
#     inner()

# outer() # outer message


# counter = 0
# def increase_counter():
#     counter = 1
#     print("Inside:", counter) # 1

# increase_counter()
# print("Outside:", counter) # 0


# keyword "global" is used to modify the global variable inside the function

# counter = 0
# def increase_counter():
#     global counter
#     counter += 1

# increase_counter()
# print(counter) # 1


# counter2 = 0
# def increase_counter2(current_counter):
#     return current_counter + 1

# counter2 = increase_counter2(counter2)
# print(counter2) # 1


# x = 10
# def example():
#     x = 20
#     print("Inside: ", x)

# example() # Inside: 20
# print("Outside: ", x) # Outside: 10


# total = 100
# def add_tax():
#     total = total * 1.25 # total is a local variable inside the function, it will be treated as local variable
#     return total

# add_tax() # UnboundLocalError: cannot access local variable 'total'

# Rewrite the function without using global keyword
# pass global variable by value
# total = 100
# def add_tax(total):
#     total = total * 1.25
#     return total

# print(add_tax(total)) # 125.0

# pass global variable by reference
# total = 100
# def add_tax():
#     result = total * 1.25
#     return result

# print(add_tax()) # 125.0

# pass global variable by value
# total = 100
# def add_tax(amount):
#     return amount * 1.25

# total = add_tax(total)
# print(total) # 125.0


# *args - arbitrary number of arguments

# def add_number(a, b):
#     return a + b

# print(add_number(10, 20)) # 30

# def add_number(a, b, c):
#     return a + b + c

# print(add_number(10, 20, 30)) # 60

# def show_numbers(*args): # args is a tuple type
#     print(args)

# show_numbers(10, 20, 30) # (10, 20, 30)
# show_numbers(10, 20, 30, 40, 50) # (10, 20, 30, 40, 50)
# show_numbers(10) # (10)


# def show_names(*args):
#     for name in args:
#         print(name)

# show_names("John", "Jane", "Jim")


# def add_numbers(*args):
#     total = 0

#     for number in args:
#         total += number
#     return total

# print(add_numbers(10, 20, 30)) # 60
# print(add_numbers(1, 2, 3, 4, 5)) # 15


# def calculate_total(discount,*prices):
#     total = 0
#     for price in prices:
#         total += price
#     return total * (1 - discount)

# print(calculate_total(0.10, 100, 200, 300)) # 540

# useful when:
# the function should accept several positional values
# the exact number of values is not known in advance

# # Better:
# def calculate_area(width, height):
#     return width * height

# print(calculate_area(10, 20)) # 200

# # less clear:
# def calculate_area(*args):
#     return args[0] * args[1]

# print(calculate_area(10, 20)) # 200


# unpacking arguments

# def add_three(a, b, c):
#     return a + b + c

# numbers = [1, 2, 3]
# # print(add_three(numbers)) # doesn't work because numbers is a list, passed as 1 argument instead of 3 arguments
# # print(add_three(*numbers)) # 6 - unpacking the list into 3 arguments add_three(1, 2, 3)

# values = (5, 10, 15)
# # print(add_three(values)) # doesn't work because values is a tuple, passed as 1 argument instead of 3 arguments
# print(add_three(*values)) # 30 - unpacking the tuple into 3 arguments add_three(5, 10, 15)


# **kwargs - unknown numbers named arguments
# **kwargs to pass unknown number of named arguments

# some user only have name, while other have name, email, phone...
# we dont know the exact number of arguments in advance

# def show_user(**kwargs): # kwargs is a dictionary type (key value arguments)
#     print(kwargs)

# show_user(name="John", email="john@example.com", phone="1234567890") # {'name': 'John', 'email': 'john@example.com', 'phone': '1234567890'}
# show_user(name="Jane", email="jane@example.com") # {'name': 'Jane', 'email': 'jane@example.com'}
# show_user(name="Jim") # {'name': 'Jim'}


# def show_user(**kwargs):
#     print("Name:", kwargs["name"])
#     print("Email:", kwargs["email"])
#     print("Phone:", kwargs["phone"])

# show_user(name="John", email="john@example.com", phone="1234567890") # Name: John, Email: john@example.com, Phone: 1234567890
# show_user(name="Jane", email="jane@example.com") # NameError: 'phone' is not in kwargs

# def show_user(**kwargs):
#     print("Name:", kwargs.get("name","Unknown"))
#     print("Email:", kwargs.get("email","Unknown"))
#     print("Phone:", kwargs.get("phone","Unknown"))

# show_user(name="John", email="john@example.com", phone="1234567890") # Name: John, Email: john@example.com, Phone: 1234567890
# show_user(name="Jane", email="jane@example.com") # Name: Jane, Email: jane@example.com, Phone: Unknown


# def show_information(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# show_information(name="John", age=36, city="London", languages="Python")
# # Name: John, Age: 36, City: London, Languages: Python


# def create_user(username,**kwargs):
#     print(f"Creating user: {username}")

#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# create_user("John", age=36, city="London", languages="Python")
# # Creating user: John
# # Age: 36
# # City: London
# # Languages: Python

# unpack dictionary arguments
# def introduce(name, age, city):
#     print(name, age, city)

# person = {"name": "John", "age": 36, "city": "London"}

# # introduce(name=person["name"], age=person["age"], city=person["city"]) # John 36 London

# introduce(**person) # John 36 London - is the same as introduce(name=person["name"], age=person["age"], city=person["city"])


# *args + **kwargs - accept flexible number and types of arguments
# def example(required, *args, **kwargs):
#     print(f"Required: {required}")
#     print(f"Args: {args}")
#     print(f"Kwargs: {kwargs}")

# example("Hello", 10, 20, 30, name="John", active="True")
# Required: Hello
# Args: (10, 20, 30)
# Kwargs: {'name': 'John', 'active': 'True'}


