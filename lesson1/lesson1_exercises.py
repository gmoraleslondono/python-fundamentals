# #Part A
# #1
# print("Cecilia Morales")
# print("Python - AI and ML")
# print("Goal- Learn Python fundamentals")

# #2
# name = "Cecilia"
# age = 30
# height = 1.65
# student = True

# print(name, type(name))
# print(age, type(age))
# print(height, type(height))
# print(student, type(student))

# #3
# print(age, type(age))
# age = "30"
# print(age, type(age))
# #It demostrates that python is a dynamically typed language, meaning that the type of a variable can change at runtime.

# #4
# number1 = 12
# number2 = 5
# print(f"a = {number1}, b = {number2}")
# print(f"a+b= {number1 + number2}")
# print(f"a-b= {number1 - number2}")
# print(f"a*b= {number1 * number2}")
# print(f"a/b= {number1 / number2}")
# print(f"a//b= {number1 // number2}")
# print(f"a%b= {number1 % number2}")
# print(f"a**b= {number1 ** number2}")

# #5
# #example str to int
# str_num = "10"
# int_num = int(str_num)

# #example int to str
# int_num2 = 20
# str_num2 = str(int_num2)

# #example in to float
# int_num3 = 30
# float_num = float(int_num3)

# #Part B
# #1
# current_year = 2026

# name = input("Enter your name: ")
# birth_year = int(input("Enter your birth year: "))

# age = current_year - birth_year

# print(f"{name}, your approximate age is: {age}")

# #2
# price = int(input("Enter the price of the product: "))
# discount_percentage = int(input("Enter the discount percentage: "))

# final_price = price - (price * discount_percentage / 100)
# print(f"The final price of the product is: ${final_price}")

# #3
# temperature_celsius = float(input("Enter the temperature in Celsius: "))
# temperature_fahrenheit = (temperature_celsius * 9/5) + 32
# print(f"The temperature in Fahrenheit is: {temperature_fahrenheit}")

# #4
# room_length = float(input("Enter the room length: "))
# room_width = float(input("Enter the room width: "))

# room_area = room_length * room_width
# room_perimeter = 2 * (room_length + room_width)

# print(f"The area of the room is: {room_area}")
# print(f"The perimeter of the room is: {room_perimeter}")

# #5 (Input validation for temperature)
# temperature_celsius = input("Enter the temperature in Celsius: ")

# if temperature_celsius.isdigit():
#     temperature_fahrenheit = (float(temperature_celsius) * 9/5) + 32
#     print(f"The temperature in Fahrenheit is: {temperature_fahrenheit}")
# else:
#     print("It is not a valid number.")

# #Part C
# #1
# sentence = "Hello, I am a sentence."
# print(len(sentence))
# print(sentence.upper())
# print(sentence.lower())
# print(sentence.replace(" ", ""))

# #2
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# print(f"{first_name} {last_name}")

# #3
# string = "python programming"
# print(string[0])
# print(string[-1])
# print(string[0:6])
# print(string[-11:])
# print(string[::-1])

# #4 (Username generator)
# first_name = input("Enter your first name: ").strip().lower()
# last_name = input("Enter your last name: ").strip().lower()
# username = first_name[0:3] + last_name[0:5]
# print(f"Your username is: {username}")

# #5(trim email)
# email = input("Enter your email: ").strip()
# domain = email.split("@")[-1]
# before_domain = email.split("@")[0]

# print(f"Email: {email}")
# print(f"Domain: {domain}")
# print(f"Before Domain: {before_domain}")

# #6
# sentence = "I want to learn Java"
# new_sentence = sentence.replace("Java", "Python")
# print(sentence)
# print(new_sentence)

# #Part D
# #1
# sentence = "python is fun"
# sentence[2] #"t"
# sentence[3:5] #"ho"
# sentence[6:9] #"is"
# sentence[-3:-2] #"f"
# sentence[:6] #"python"
# sentence[10:len(sentence)] #"fun"
# sentence[-8] #"n"
# sentence[:] #"python is fun"

# #2
# text = "Artificial Intelligence"
# slice1 = text[0:10]  # "Artificial" - first 10 characters
# slice2 = text[11:22]  # "Intelligenc" - characters from index 11 to 21
# slice3 = text[::2]  # "Atfca nelgne" - every second character
# slice4 = text[::-1]  # "ecnegilletnI laicifitrA" - the string reversed
# slice5 = text[-10:]  # "telligence" - last 10 characters
# slice6 = text[5:15]  # "icial Inte" - characters from index 5 to 14

#3
# The difference between .split() and .strip(), .replace() is that:

#.split() is used to split a string into a list based on a specified delimiter
# data = "apple, banana, orange"
# print(data.split(", ")) # splits the string into a list based on the delimiter ", "  // ['apple', 'banana', 'orange']

#.strip() is used to remove whitespace from the beginning and end of a string
# message1 = "   Hello, World!   "
# print(message1.strip()) # removes whitespace from both ends

#.replace() is used to replace occurrences of a specified substring with another substring within the string
# message2 = "Python is fun"
# print(message2.replace("fun", "powerful")) # replaces "fun" with "powerful"

# The in operator is used to check if a substring exists within a string, returning True or False.
# message3 = "Python is fun"
# print("fun" in message3)  # True
# print("boring" in message3)  # False


#4
# Explain string immutability in Python. Strings are immutable in Python, meaning that once a string is created, it cannot be changed or modified. Any operation that seems to modify a string actually creates a new string object. For example, if you try to change a character in a string using indexing, it will raise an error. Instead, you can create a new string by concatenating or slicing the original string.
# word = "python"
# word[0] = "J" # this will throw an error because strings are immutable
# print(word)

# word = "python"
# word = "J" + word[1:]
# print(word) # "Jython"


# #Part E
# #1 and 2
# first_name = input("Enter your first name: ").strip()
# last_name = input("Enter your last name: ").strip()
# city = input("Enter your city: ").strip()
# year_birth = input("Enter your year of birth: ").strip()
# favorite_programming_language = input("Enter your favorite programming language: ").strip()

# #3
# user_id = first_name[-3:len(first_name)] + year_birth

# #4
# print("------------------------------")
# print(f"First Name: {first_name}")
# print(f"Last Name: {last_name}")
# print(f"City: {city}")
# print(f"Year of Birth: {year_birth}")
# print(f"Favorite Programming Language: {favorite_programming_language}")
# print("------------------------------")
# print(f"Your user ID is: {user_id}")
# print("------------------------------")

# #5
# print(first_name[0] + last_name[0])
# full_name = first_name +last_name
# print(len(full_name))
# print(favorite_programming_language[::-1])
# print("------------------------------")

# #6
# print(type(year_birth))
# convert_int = int(year_birth)
# print(type(convert_int))
# print(city.upper())
# print("------------------------------")

# #F
# #1 (Seconds converter)
# total_seconds = int(input("Enter the total number of seconds: "))
# hours = total_seconds // 3600
# minutes = (total_seconds % 3600) // 60
# seconds = total_seconds % 60
# print(f"{hours} hours, {minutes} minutes, {seconds} seconds")

#TODO: no sure it is good approach
#2 (four digit integer, converting to string)
# four_digit_integer = 1234
# for digit in str(four_digit_integer):
#     print(f"Digit: {digit}")

# # (four digit integer, without convert to string)
# four_digit_integer = 9874
# digit1 = four_digit_integer // 1000
# digit2 = (four_digit_integer // 100) % 10
# digit3 = (four_digit_integer // 10) % 10
# digit4 = four_digit_integer % 10

# print(digit1)
# print(digit2)
# print(digit3)
# print(digit4)

#3(masking text with * except first and last two letters)
# text = "Python is awesome"
# result = ""

# for char in range(len(text)):
#     if char < 2 or char >= len(text) - 2:
#         result += text[char]
#     else:
#         result += "*"

# print(result)

# #4 (short predict before running examples, type conversion, slicing, and string methods)
# data_given = 1
# is_boolean = bool(data_given) # True

# text = "Python Programming"
# slice1 = text[7:len(text)]  # "Programming"
# slice2 = text + " " + text[:6] # Python Programming Python
# replacement = text.replace(" ", "❤️") #"Python❤️Programming"
# data = text.split(" ")  # ['Python', 'Programming']

# print(is_boolean)
# print(slice1)
# print(slice2)
# print(replacement)
# print(data)

