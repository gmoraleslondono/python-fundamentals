# comparison
# print(5 > 2) # True
# print(5 < 2) # False
# print(5 == 2) # False
# print(5 != 2) # True
# print(5 >= 2) # True
# print(5 <= 2) # False

# number = 10 # assigning
# number == 10 # comparison

# print(1 == 1) # True
# print(1 == "1") # False
# print("1" == "1") # True

# combine multiple conditions (and, or, not)

# and (all have to be true)
# age = 16
# has_ticket = True
# print (age >= 18 and has_ticket) # False

# or (at least one has to be true)
# is_admin = True
# is_teacher = True
# print(is_admin or is_teacher) # True


# not (reverse the boolean value)
# is_logged_in = False
# print(is_logged_in) # False
# print(not is_logged_in) # True

# languages = ["Python", "Java", "C#"]
# print("Python" in languages) # True
# print("Rust" in languages) # False
# print("Python" not in languages) # False
# print("Rust" not in languages) # True


# Indentation
# if/elif/else

# age = 20
# if age >= 18:
#     print("Adult")

# age = 16
# if age >= 18:
#     print("Adult")
# else:
#     print("Under 18")

# score = 80
# if score >= 90:
#     print("Great A")
# elif score >= 80:
#     print("Grade B")
# elif score >= 70:
#     print("Grade C")
# else:
#     print("Bellow C")
# # Grade B


# Order matters
# score = 95
# if score >= 70:
#     print("Great C or higher")
# elif score >= 80:
#     print("Grade B or higher")
# elif score >= 90:
#     print("Grade C")
# # Great C or higher


# age = 16
# has_ticket = True
# if age >= 18 and has_ticket:
#     print("yuo may enter!")


# age = 20
# has_ticket = True
# if age >= 18:
#     if has_ticket:
#         print("yuo may enter!")
#     else:
#         print("You need a ticket!")
# else:
#     print("Entry denied, you are too young!")

# # 0, empty strings, empty list, None are Falsy values
# name = ""
# if name:
#     print("We have a name")
# else:
#     print("The name is empty")
# The name is empty



# loops
# languages = ["Python", "Java", "c#", "Javascript"]
# print(languages[0]) # Python
# print(languages[1]) # Java
# print(languages[2]) # c#
# print(languages[3]) # Javascript

# # for-loop
# languages = ["Python", "Java", "c#", "Javascript"]
# for language in languages:
#     print(language)
# # Python
# # Java
# # c#
# # Javascript

# # loop over string
# word = "Python"
# for character in word:
#     print(character)

# # P
# # y
# # t
# # h
# # o
# # n


# numbers = [3, 8, 12, 5, 20, 7]
# for number in numbers:
#     if number >= 10:
#         print(number) # 12 20



# numbers = [0, 1, 2, 3, 4, 5, 6, -6]
# for number in numbers:
#     if number % 2 == 0: # even numbers
#         print(number) # 0 2 4 6 -6

#loop over a dictionary (it loops over the keys)
# student = {
#     "name": "Eva",
#     "age": 25,
#     "course": "AI Developer"
# }

# for key in student:
#     print(key) # name age course

# for key in student:
#     print(student[key]) # Eva 25 AI Developer

# for key in student:
#     print(key, student[key]) # name Eva age 25 course AI Developer

# student = {
#     "name": "Eva",
#     "age": 25,
#     "course": {
#         "course1": "AI Developer",
#         "course2": "English"
#         }
# }

# for key in student:
#     print(student["course"]["course1"])



# item() key-value pairs
# student = {
#     "name": "Eva",
#     "age": 25,
#     "course": "AI Developer"
# }

# for key, value in student.items():
#     print(key, value) # name Eva age 25 course AI Developer



# loop over list
# students = [
#     {"name" : "Anna", "score": 85},
#     {"name" : "Bob", "score": 62},
#     {"name" : "Charlie", "score": 91}
# ]
# for student in students:
#     print(student["name"]) # Anna Bob Charlie


# students = [
#     {"name" : "Anna", "score": 85},
#     {"name" : "Bob", "score": 62},
#     {"name" : "Charlie", "score": 91}
# ]
# for student in students:
#     if student["score"] >= 70:
#         print(student["name"], "passed.")
# # Anna passed.
# # Charlie passed.


# range
# for number in range(5):
#     print(number) # 0 1 2 3 4


# for number in range(2, 10):
#     print(number) # 2 3 4 5 6 7 8 9

# for number in range(2, 10, 2):
#     print(number) # 2 4 6 8


# languages = ["Python", "Java", "C#"]

# # incorrect way to loop over a list
# for i in range(len(languages)):
#     print(languages[i])

# # correct way to loop over a list
# for language in languages:
#     print(language)


# languages = ["Python", "Java", "C#"]

# for index, language in enumerate(languages):
#     print(index, language)
# # 0 Python
# # 1 Java
# # 2 C#

# While-loop

# count = 1
# while count <= 5 :
#     print(count) # 1 2 3 4 5
#     # count = count + 1
#     count += 1


# break and continue

# numbers = [2, 4, 6, 7, 8, 10, 11]
# for number in numbers:
#     if number % 2 != 0:
#         print("Found an odd number:", number) # Found an odd number: 7
#         break

# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#     if number == 3:
#         continue
#     print(number) # 1 2 4 5 -> 3 is skipped and it continue


