# Part A
# # 1
# number = 1
# if number == 0:
#     print("This number is zero.")
# if number >= 1:
#     print("This is a positive number.")
# if number < 0:
#     print("This number is negative.")
# # This is a positive number.

# 2
# age = int(input("What is your age?: "))
# if age >= 30:
#     print("You are an adult.")
# elif age >= 20:
#     print("You are a pre-adult.")
# elif age > 13:
#     print("You are an adolescent.")
# else:
#     print("You are a child.")

# 3
# username = input("Enter your username: ")
# password = input("Enter your password: ")

# if username == "abc" and password == "123":
#     print("You have access!")
# else:
#     print("Enter the correct username and/or password!")

# 4
# score = 99

# if score >= 80:
#     print("Grade A")
# elif score >= 70:
#     print("Grade B")
# elif score >= 60:
#     print("Grade C")
# elif score >= 40:
#     print("Grade D")
# else:
#     print("Grade E")

# # 5
# order_total = 6000
# is_customer = False

# if order_total >= 5000 or is_customer:
#     print("Shipping is free!")
# else:
#     print("You should pay a shipping fee.")

# 6
# print(5 > 2) # True
# print(5 < 2) # False
# print(5 == 2) # False
# print(5 != 2) # True
# print(5 >= 2) # True
# print(5 <= 2) # False



# Part B (Truthy, Falsy and membership)
# 1
# # empty string
# name = ""
# if name:
#     print("We have a name")
# else:
#     print("The name is empty")
# # The name is empty

# #non-empty string
# name = "Anna"
# if name:
#     print("We have a name")
# else:
#     print("The name is empty")
# # We have a name

# # Zero
# is_valid = 0 # Falsy value
# if is_valid:
#     print("Valid!")
# else:
#     print("Invalid!")
# # Invalid -> because 0 is falsy

# # non-zero
# is_valid = 1 # Truthy value
# if is_valid:
#     print("Valid!")
# else:
#     print("Invalid!")
# # Valid -> because 1 is truthy

# # empty list
# shopping_list = [] # Falsy value
# if shopping_list:
#     print("The list is ready!")
# else:
#     print("Make your shopping list!")
# # Make your shopping list! -> because empty list is a falsy value

# # non-empty list
# shopping_list = ["rice", "tomato", "juice"] # Truthy value
# if shopping_list:
#     print("The list is ready!")
# else:
#     print("Make your shopping list!")
# # The list is ready! -> because non-empty list is a truthy value

# # 2
# language = input("Enter your language: ")
# supported_languages = ["Spanish", "English", "Swedish"]

# if language in supported_languages:
#     print("Your language is supported!")
# else:
#     print("Your language is not supported!")

# # 3
# banned_users = ["Darth Vader", "Sauron", "Voldemort" ]
# username = input("Enter your username: ")

# if username in banned_users:
#     print("Access denied!")
# else:
#     print(f"Hello, {username}!")

# 4
# is_logged_in = False
# print(is_logged_in) # False
# print(not is_logged_in) # True

# is_valid = True
# print(is_valid) # True
# print(not is_valid) # False

# is_open = True
# print(is_open) # True
# print(not is_open) # False


# Part C - For loops
# # 1
# names = ["Darth Vader", "Sauron", "Voldemort" ]

# for index, name in enumerate(names, start=1):
#     print(f"{index} Hello, {name}")

# # 2
# for number in range(1, 50):
#     if number % 2 == 0:
#         print(number)

# 3
# numbers = [1, 5, 10, 6]
# total = 0
# for number in numbers:
#     total = total + number
# print(total)

# 4
# numbers = [1, 5, 10, 6]
# largest_number = 0
# for number in numbers:
#     if number > largest_number:
#         largest_number = number

# print(largest_number)

# 5
# fruits = ["apple", "grape", "kiwi", "orange"]
# count = 0

# for fruit in fruits:
#     if len(fruit) > 5:
#         count = count + 1

# print(count)

# # 6
# scores = [85, 40, 64, 25, 41, 85, 96]
# passes = 0
# failures = 0

# for score in scores:
#     if score > 70:
#         passes = passes + 1
#     else:
#         failures = failures + 1

# print(passes)
# print(failures)


# # 7
# student = {
#     "name": "Eva",
#     "age": 25,
#     "course": "AI Developer"
# }

# for key, value in student.items():
#     print(value)

# for key, value in student.items():
#     print(key)

# for key, value in student.items():
#     print(f"{key} is {value}")


# Part D
# # 1
# for number in range(10, 0, -1):
#     print(number)

# # 2
# playlist = ["track1", "track2", "track3", "track4", "track5"]
# for index, element in enumerate(playlist, start=1):
#     print(index, element)

# # 3
# for x in range(1, 4):
#     for y in range(1, 5):
#         print(x, y)

# # 4
# for row in range(5):
#     for column in range(5):
#         print("*", end=" ") # end=" " keeps printing on the same line.
#     print() # moves to the next line after the 5 columns are finished.

# # for each row:
# #     for each column:
# #         print something on the same line
# #     move to the next line


# Part E
# # 1
# for i in range(10, -1, -1):
#     print(i)

# # 2
# correct_password = "123"
# password = input("Enter the password: ")

# while password != correct_password:
#     print("Incorrect password, try again!")
#     password = input("Enter the password: ")

# print("You have access!")

# # 3
# user_input = input("Hello, please write continue to ask again or quit to cancel: ")

# while user_input != "quit":
#     user_input = input("Hello, please write continue to ask again or quit to cancel: ")

# print("You choose to quit the program!")

# # 4
# number = int(input("Please enter a number to continue, otherwise 0 to cancel: "))
# total = 0

# while number != 0:
#     total = total + number
#     number = int(input("Please enter a number to continue, otherwise 0 to cancel: "))

# print("You have cancelled the program!")
# print(total)

# # 5
# secret_number = 5
# guessed_number = int(input("Please guess the secret number from 0 to 10: "))

# while guessed_number != secret_number:
#     if guessed_number > 5:
#         print("The number is too high!")
#     elif guessed_number < 5:
#         print("The number is too low!")

#     guessed_number = int(input("Please guess the secret number from 0 to 10: "))

# print("You have found the number!")

# Part F - break and continue
# # 1
# for number in range(1, 100):
#     if number % 7 == 0 and number % 9 == 0:
#         print(number) # 63
#         break

# 2
# names = ["Darth Vader", "Sauron", "", "Voldemort", "", "Gloria" ]
# for name in names:
#     if len(name) == 0:
#         continue
#     print(name) # Darth Vader Sauron Voldemort Gloria

# 3
# names = ["Darth Vader", "Sauron", "Voldemort", "Gloria" ]
# my_name = input("Enter your name: ")

# for name in names:
#     print(name)
#     if my_name in names:
#         print("Found!")
#         break
# else:
#     print("Not found!")

# 4
# numbers = [1, 0, 5, -4, 10, -20, 12, -8, 7, 999, 5, -15, 6]

# for number in numbers:
#     if number < 0:
#         continue
#     elif number == 999:
#         break
#     print(number) # 1 0 5 10 12 7

# Part G - Challenge: Console study tracker
# 1
# study_sessions = [
#     {"subject": "Python", "minutes": 60},
#     {"subject": "English", "minutes": 30},
#     {"subject": "JavaScript", "minutes": 45},
#     {"subject": "Python", "minutes": 90},
#     {"subject": "Math", "minutes": 40},
#     {"subject": "HTML", "minutes": 30},
#     {"subject": "CSS", "minutes": 50},
#     {"subject": "English", "minutes": 35},
#     {"subject": "Python", "minutes": 75},
#     {"subject": "JavaScript", "minutes": 60}
# ]

# # 2
# total_minutes = 0
# for session in study_sessions:
#     total_minutes = total_minutes + session["minutes"]

# print(total_minutes) # 515

# 3
# total_minutes_by_subject = {}

# for session in study_sessions:
#     subject = session["subject"]
#     minutes = session["minutes"]

#     if subject not in total_minutes_by_subject:
#         total_minutes_by_subject[subject] = minutes
#     else:
#         total_minutes_by_subject[subject] = total_minutes_by_subject[subject] + minutes

# print(total_minutes_by_subject)

# {'subject': 'Python', 'minutes': 60}
# {'subject': 'English', 'minutes': 30}
# {'subject': 'JavaScript', 'minutes': 45}
# {'subject': 'Python', 'minutes': 90}
# {'subject': 'Math', 'minutes': 40}
# {'subject': 'HTML', 'minutes': 30}
# {'subject': 'CSS', 'minutes': 50}
# {'subject': 'English', 'minutes': 35}
# {'subject': 'Python', 'minutes': 75}
# {'subject': 'JavaScript', 'minutes': 60}


# # 4 -  Find the longest session
# longest_session = {}

# for session in study_sessions:

#     if not longest_session:
#         longest_session = session

#     elif session["minutes"] > longest_session["minutes"]:
#         longest_session = session

# print(longest_session) # {'subject': 'JavaScript', 'minutes': 120}

# 5 - sessions longer than 45
# for session in study_sessions:
#     if session["minutes"] > 45:
#         print(session)

# {'subject': 'Python', 'minutes': 60}
# {'subject': 'Python', 'minutes': 90}
# {'subject': 'CSS', 'minutes': 50}
# {'subject': 'Python', 'minutes': 75}
# {'subject': 'JavaScript', 'minutes': 60}

# # 6 - user menu to view all sessions, view total time, filter by subject or quit
# menu = input("Select to view all sessions (all), view total time (time), filter by subject (filter) or quit (q): ")

# if menu  == "all":
#     print(study_sessions)
# elif menu == "time":
#     total_minutes = 0
#     for session in study_sessions:
#         total_minutes = total_minutes + session["minutes"]
#     print(total_minutes) # 515
# elif menu == "filter":
#     name = input("Enter the subject name: ")
#     for session in study_sessions:
#         if name in session.values():
#             print(session)
#             break
#     else:
#         print("Subject not found!")
# elif menu == "q":
#     print("Program closed!")
# else:
#     print("Invalid command")

# Part H - Stretch challenge
# # 1 - Find the multiples of 3 -> Fizz 5 -> Buzz Both -> FizzBuzz
# for number in range(1, (100+1)):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# # 2 - Count vowels
# sentence = "Python is fun"
# vowels = ["a", "e", "i", "o", "u"]
# vowels_count = 0
# for char in sentence:
#     if char in vowels:
#         vowels_count = vowels_count + 1
# print(vowels_count) # 3

# # 3 - Find duplicates
# numbers = [1, 0, 5, -4, 10, 6, 12, -8, 7, 1, 5, -4, 6]

# duplicates = set()
# for number in numbers:
#     if numbers.count(number) > 1:
#         duplicates.add(number)
# print(duplicates) # {1, -4, 5, 6}

# # 4 - Text histogram: for each number in [3, 5, 2] print that many *
# numbers = [3, 5, 2]
# for number in numbers:
#     print("*" * number)


