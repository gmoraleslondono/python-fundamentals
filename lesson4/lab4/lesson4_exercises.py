# Part A - Function fundamentals
#1 - write functions
# def greet():
#     print("Hello!")

# greet() # Hello!
# greet() # Hello!

# def show_course_name():
#     print("Python - AI and ML")

# show_course_name() # Python - AI and ML
# show_course_name() # Python - AI and ML

# def print_separator():
#     print("--------------------")

# print_separator() # --------------------
# print_separator() # --------------------


# 2 - write functions with parameters
# def greet_person(name):
#     print("Hello", name)

# greet_person("Cecilia") # Hello Cecilia

# def introduce(name: str, city: str) -> None:
#     """
#     Introduce a person by name and city.
#     :param name: str - The name of the person.
#     :param city: str - The city where the person lives.
#     :return: None - This function does not return a value.
#     """
#     print(f"I am {name} and I live in {city}")

# introduce("Cecilia", "Stockholm") # I am Cecilia and I live in Stockholm

# 3 - write functions that return
# Add
# def add(a: int, b: int) -> int:
#     """
#     Add two numbers.
#     :param a: int - The first number.
#     :param b: int - The second number.
#     :return: int - The sum of the two numbers.
#     """
#     return a + b

# result = add(1, 2)
# print(result) # 3

# Subtract
# def subtract(a: int, b: int) -> int:
#     """
#     Subtract two numbers.
#     :param a: int - The first number.
#     :param b: int - The second number.
#     :return: int - The difference of the two numbers.
#     """
#     return a - b

# result = subtract(5, 3)
# print(result) # 2

# Multiply
# def multiply(a: int, b: int) -> int:
#     """
#     Multiply two numbers.
#     :param a: int - The first number.
#     :param b: int - The second number.
#     :return: int - The product of the two numbers.
#     """
#     return a * b

# result = multiply(2, 3)
# print(result) # 6

# Divide
# def divide(a: int, b: int) -> float:
#     """
#     Divide two numbers.
#     :param a: int - The first number.
#     :param b: int - The second number.
#     :return: float - The quotient of the two numbers.
#     """
#     return a / b

# result = divide(10, 2)
# print(result) # 5.0

# 4 - Parameter vs argument
# def greet(name): # name is the parameter
#     print("Hello", name)

# greet("Cecilia") # Hello Cecilia -  Cecilia is the argument

# 5 - Use returned value
# def calculate_area(width, height):
#     return width * height

# def cost_per_area(width, height, cost):
#     return calculate_area (width, height) * cost

# result = cost_per_area(15, 2, 1500)
# print(result) # 45000


# Part B - Return values
# 1 - Return boolean
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     return False

# print(is_even(3)) # False
# print(is_even(6)) # True


# 2 - return largest value
# def get_larger(a, b):
#     if a > b:
#         return a
#     return b

# print(get_larger(2, 6)) # 6
# print(get_larger(12, 4)) # 12

# 3 - conditionals
# def classify_score(score):
#     if score >= 50:
#         return "PASS"
#     return "FAIL"

# print(classify_score(20)) # FAIL
# print(classify_score(80)) # PASS

# 4 - return formatted string
# def full_name(first_name, last_name):
#     return first_name + " " + last_name

# print(full_name("Cecilia", "Morales")) # Cecilia Morales

# 5 return calculation
# def calculate_discount(price, percent):
#     return price - price*(percent/100)

# print(calculate_discount(1000, 20)) # 800.0

# 6
# # function with print
# def add_with_print(a, b):
#     print(a + b) # 8

# result = add_with_print(5, 3)
# print("Result:", result) # Result: None - because the function does not return a value

# # function with return
# def add_with_print(a, b):
#     return a + b

# result = add_with_print(5, 3)
# print("Result:", result) # Result: 8

# Part C - Defaults and keyword arguments
# 1
# def greet(name, greeting='Hello'):
#     return greeting + " " + name

# print(greet("Cecilia", "Hi")) # Hi Cecilia
# print(greet("Cecilia")) # Hello Cecilia
# print(greet(greeting="Hej", name="Cecilia")) # Hej Cecilia - This doesn't throw error because it is explicit what parameter it is
# # print(greet(greeting="Hej", "Cecilia")) # This will throw an error since it will keep the same order as in the parameters
# # print(greet()) # This will throw an error because the function is expecting some parameters to be passed

# 2
# def calculate_price(price, quantity=1, discount=0):
#     if discount == 0:
#         return price*quantity
#     return (price * quantity) - discount

# # print(calculate_price(1000, 2, 20)) # 1980
# print(calculate_price(500)) # 500
# print(calculate_price(price=200, quantity=10, discount=50)) # 1950

# 3
# def create_profile(name, city="Unknown", active=True):
#     return {"name" : name, "city" : city, "active" : active}

# result = create_profile("Cecilia", "Stockholm", False)
# print(result) # {'name': 'Cecilia', 'city': 'Stockholm', 'active': False}

# 4
# def subtract(number1, number2):
#     return number1 - number2

# result = subtract(number2=3, number1=10)
# print(result) # 7

# 5
# def introduce(name, age):
#     print("Name:", name)
#     print("Age:", age)

# introduce(36, "Ada") # Name: 36, Age: Ada - It is invalid because Python always takes the order of the arguments as the same in the parameters

# Part D - Functions and collections
# 1
# numbers = [1, 2, 3, 4, 5]

# def calculate_total(numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     return total

# print(calculate_total(numbers)) # 15

# 2
# numbers = [1, 2, 3, 4, 5]

# def count_even(numbers):
#     count = 0
#     for number in numbers:
#         if number % 2 == 0:
#             count += 1
#     return count

# print(count_even(numbers)) # 2

# 3
# words = ["airplane", "yes", "no", "class", "studies" ]

# def get_long_word(words, minimum_length):
#     long_words = []
#     for word in words:
#         if len(word) >= minimum_length:
#             long_words.append(word)
#     return long_words

# result = get_long_word(words, 5)
# print(result) # ['airplane', 'class', 'studies']

# 4
# students = [
#     {"name": "John", "age": 30, "city": "New York"},
#     {"name": "Eva", "age": 25, "city": "Los Angeles"},
#     {"name": "Mike", "age": 35, "city": "Chicago"}
# ]

# def find_student(students, name):
#     for student in students:
#         if student["name"] == name:
#             return student
#             break
#     return

# result = find_student(students, "Eva")
# print(result)

# 5
# students = [
#     {"name": "John", "age": 30, "city": "New York", "score": 75},
#     {"name": "Eva", "age": 25, "city": "Los Angeles", "score": 59},
#     {"name": "Mike", "age": 35, "city": "Chicago", "score": 35}
# ]

# def average_score(students):
#     sum = 0
#     count = 0
#     for student in students:
#         sum += student["score"]
#         count += 1
#     return sum / count

# print(average_score(students)) # 56.333333333333336

# 6
# users = [
#     {"name": "John", "age": 30, "city": "New York", "active": True},
#     {"name": "Eva", "age": 25, "city": "Los Angeles", "active": False},
#     {"name": "Mike", "age": 35, "city": "Chicago", "active": True}
# ]

# def get_active_users(users):
#     active = []
#     for user in users:
#         if user["active"] == True:
#             active.append(user)
#     return active

# result = get_active_users(users)
# print(result) # [{'name': 'John', 'age': 30, 'city': 'New York', 'active': True}, {'name': 'Mike', 'age': 35, 'city': 'Chicago', 'active': True}]

# Part E - Decomposition
# 1
# def Celsius_to_Fahrenheit(temperature_celsius):
#     temperature_fahrenheit = (temperature_celsius * 9/5) + 32
#     return temperature_fahrenheit

# def classify(temp):
#     if temp <= 64:
#         return "Cold"
#     elif temp <= 79:
#         return "Warm"
#     else:
#         return "Hot"

# result = classify(Celsius_to_Fahrenheit(30))
# print(result) # Hot

# 2
# def calc_subtotal(quantity, price):
#     return quantity * price

# def calc_discount(subtotal, discount):
#     return subtotal * discount/100

# def calc_total(subtotal, discount ):
#     return subtotal - discount

# def order(quantity, price, discount):
#     subtotal = calc_subtotal(quantity, price)
#     discount = calc_discount(subtotal, discount)
#     total = calc_total(subtotal, discount)
#     return total

# result = order(1, 100, 20)
# print(result) # 80

# 3 - Choose any earlier exercise with repeated code and refactor it into at least three functions.
# convert temperature from Celsius to Fahrenheit

def Celsius_to_Fahrenheit(temperature_celsius):
    return fahrenheit_formula(temperature_celsius)

def fahrenheit_formula(temp):
    return multiply_by_9_5(temp) + add_32()

def multiply_by_9_5(temp):
    return temp * 9/5

def add_32():
    return 32

# print(Celsius_to_Fahrenheit(30)) # 86.0

# 4 - Create a clear section at the bottom of your file where you call the functions you have created.
# Look at the bottom main() function line 470.

def main():
    print(f"30°C is {Celsius_to_Fahrenheit(30)}°F") # 86.0


# Part F - Applied challenge: Event registration processor
# 1. Create functions to normalize a participant name, validate an age range using boolean return values, calculate a registration fee based on age/student status, and create a participant dictionary.

def normalize_name(name):
    return name.strip().title() # strip() removes whitespace from the beginning and end of the string, title() converts the first letter of each word to uppercase

def validate_age(age):
    return 18 <= age <= 100 # return True if age is between 18 and 100, otherwise return False

def calculate_registration_fee(age, is_student):
    if is_student:
        return 50
    elif age < 25:
        return 75
    else:
        return 100

def create_participant(name, age, is_student):
    participant = {
        "name": normalize_name(name),
        "age": age,
        "student": is_student,
        "registration_fee": calculate_registration_fee(age, is_student)
    }

    return participant

# 2. Create at least eight participant dictionaries using your functions.

participants = [
    create_participant("Gloria Morales", 30, True),
    create_participant("Anna Smith", 25, False),
    create_participant("John Doe", 35, False),
    create_participant("Jane Juice", 20, True),
    create_participant("Jim Beam", 22, False),
    create_participant("Anna Stefan", 49, True),
    create_participant("Jack Sparrow", 55, False),
    create_participant("Thomas Adan", 20, True),
    create_participant("Mat Hans", 18, True)
]

# 3. Write a function that receives the participant list and returns the total expected registration revenue.

def calculate_total_registration_revenue(list):
    total_revenue = 0
    for participant in list:
        total_revenue += participant["registration_fee"]
    return total_revenue

# print(calculate_total_registration_revenue(participants)) # 650

# 4. Write a function that returns only student participants.

def students_participants(list):
    students = []
    for participant in list:
        if participant["student"]:
            students.append(participant)
    return students

# print(students_participants(participants)) # [{'name': 'Gloria Morales', 'age': 30, 'student': True, 'registration_fee': 50}, {'name': 'Jane Juice', 'age': 20, 'student': True, 'registration_fee': 50}, {'name': 'Anna Stefan', 'age': 49, 'student': True, 'registration_fee': 50}, {'name': 'Thomas Adan', 'age': 20, 'student': True, 'registration_fee': 50}, {'name': 'Mat Hans', 'age': 18, 'student': True, 'registration_fee': 50}]

# 5. Write a function that returns the oldest participant.

def oldest_participant(list):
    oldest = {}
    for participant in list:
        if not oldest:
            oldest = participant
        if participant["age"] > oldest["age"]:
            oldest = participant
    return oldest

# print(oldest_participant(participants)) # {'name': 'Jack Sparrow', 'age': 55, 'student': False, 'registration_fee': 100}

# 6. Write a function that creates a readable summary string for one participant.

def summary(participant):
    if participant["student"]:
        return f"{participant['name']} is {participant['age']} years old and is a student."
    else:
        return f"{participant['name']} is {participant['age']} years old and is not a student."

# print(summary(participants[0])) # Gloria Morales is 30 years old and is a student.

# 7. Keep input/output responsibilities separate from calculation functions as much as possible. ✅

# Part G - Stretch challenges

# 1. write a function that returns min and max from a list, return 2 values
# def max_and_min(list):
#     max_val= 0
#     min_val= 0
#     for val in list:
#         if val > max_val:
#             max_val = val
#         elif val < min_val:
#             min_val = val
#     return max_val, min_val

# print(max_and_min([1, 3, 5, 9, -2])) # (9, -2)

# 2 - check a palindrome word
# def is_palindrome(word):
#     if word == word[::-1]:
#         return True
#     return False

# print(is_palindrome("level")) # True
# print(is_palindrome("one")) # False

# 3 - write a function that count characters frequencies and return a dictionary

# def count_characters(word):
#     frequency = {}
#     for char in word:
#         if char in frequency:
#             frequency[char] += 1
#         else:
#             frequency[char] = 1
#     return frequency

# print(count_characters("hello")) # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# 4 - Write a function that receives a list of numbers and returns a new dictionary with keys positive, negative and zero containing counts

# def count_numbers(list):
#     counts = {"positive": 0, "negative": 0, "zero": 0}
#     for number in list:
#         if number == 0:
#             counts["zero"] += 1
#         elif number > 0:
#             counts["positive"] += 1
#         elif number < 0:
#             counts["negative"] += 1
#     return counts

# print(count_numbers([1, 1, 0, -8, -6 , 0, 6, 0])) # {'positive': 3, 'negative': 2, 'zero': 3}

# 5 - Add light type hints and short docstring to at least five functions.
# Done in lines 28, 41, 54, 67, 80


# -------
# Call the main function to execute the program.
# main()
