# Class 2 - 09-09-2026

# # List (Mutable)

# numbers = [10, 20, 30, 40, 50]

# print(numbers)
# print(numbers[0])
# print(numbers[-1])
# print(numbers[1:4]) # [20, 30, 40] print numbers from position 1 to 3
# print(numbers[:3]) # [10, 20, 30] print numbers from position 0 to 3
# print(numbers[2:]) # [30, 40, 50] print numbers from position 2 to the end
# print(numbers[::2]) # [10, 30, 50] print every second numbers starting from the position 0
# print(numbers[::-1]) # [50, 40, 30, 20, 10] print list inverted

# # mixed types list
# mixed = [10, "python", True, 3.14]
# print(mixed)

# # list contain other list
# matrix_like = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix_like)
# print(matrix_like[1][1]) # 5 should print the value in the position 1, inside the list on position 1


# # mutability
# names = ["Aladin", "Grace", "Alan"]
# print(names)
# names[1] = "Guido"
# print(names)

# # List methods
# languages = ["Python", "Java", "c#"]
# print(languages) # ['Python', 'Java', 'c#']

# # append -> add element to the end
# languages.append("Javascript")
# print(languages) # ['Python', 'Java', 'c#', 'Javascript']

# # insert -> add element ina specific position
# languages.insert(1, "Go") 
# print(languages) # ['Python', 'Go, 'Java', 'c#', 'Javascript']

# # remove -> remove a specific element by value (returns the modified list)
# languages.remove("Java")
# print(languages) # ['Python', 'Go', 'c#', 'Javascript']

# # pop -> remove a specific element by index or the last element if no index is provided (returns the removed item)
# languages = ["Python", "Java", "c#"]

# removed_languages = languages.pop() # c#
# removed_languages = languages.pop(1) # Java
# print(languages)
# print(removed_languages)


# languages = ["Python", "Java", "c#", "Javascript"]
# print(len(languages)) # 4 size of the list
# print("Python" in languages) # True check if the list contains something specific
# print("Rust" in languages) # False

# # sort
# numbers = [5, 2, 9, 1, 7]
# numbers.sort() # change the original list
# print(numbers)

# numbers.reverse() # reverse the order of the list
# print(numbers)

# # sorted vs sort
# numbers = [5, 2, 9, 1, 7]
# new_numbers = sorted(numbers) # never change the original list source
# print(new_numbers)
# print(numbers)

# # copy
# list_a = [1, 2, 3]
# list_b = list_a

# list_b.append(4)
# print(list_a) # [1, 2, 3, 4]
# print(list_b) # [1, 2, 3, 4]

# list_a = [1, 2, 3]
# list_b = list_a.copy()

# list_b.append(4)
# print(list_a) # [1, 2, 3]
# print(list_b) # [1, 2, 3, 4]


# Tuples -> immutable ordered collection. You can access it, but not reassign it
# coordinates = (10, 20)
# print(coordinates[0]) # 10
# print(coordinates[1]) # 20
# coordinates[0] = 99 # will throw an error

# coordinates = (10, 20)
# x, y = coordinates
# print(x) # 10
# print(y) # 20

# person = ("Ada", 38, "Stockholm")
# name, age, city = person
# # age, city = person # it expect to math the number of values in the tuple. Throw error
# print(name) # "Ada"
# print(age) # 38
# print(city) # "Stockholm"


# a = 10
# b = 20
# a, b = b, a
# print(a) # 20
# print(b) # 10


# sets
# numbers = {1, 2, 2, 2, 3, 3, 4}
# print(numbers) # {1, 2, 3, 4}

# names = ["Anna","bob", "Anna", "Charlie", "bob"]
# unique_user = set(names)
# print(unique_user ) # {'Anna', 'Charlie', 'bob'}


# languages = {"Python", "Java", "c#"}
# languages.add("Go")
# print(languages) #languages = {'Python', 'c#', 'Java', 'Go'}

# languages.remove("Java")
# print(languages) #languages = {'Python', 'c#', 'Go'}

# print(languages[0]) # Throw error set doesnt have index assigned



# set operations
# backend_languages = {"Python", "Java", "C#"}
# data_languages = {"Python", "R", "Julia"}

# print(backend_languages & data_languages) # intersection {'Python'} find the duplicated
# print(backend_languages | data_languages) # union {'Julia', 'Python', 'C#', 'Java', 'R'} combine all, taking unique values
# print(backend_languages - data_languages) # difference {'C#', 'Java'} Find the ones that doesn't exist in the second set

# empty_collection = {}
# print(type(empty_collection)) # <class 'dict'>
# empty_set = set()
# print(type(empty_set)) # <class 'set'>

# Loop over a set
# for e in my_set:



# Dictionary (key-value)

# person = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }

# print(person)
# print(person["name"])  # Accessing value by key
# print(person["age"])   # Accessing value by key

#(change values)
# person = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }

# person["age"] = 31
# print(person) # person = {'name': 'John', 'age': 31, 'city': 'New York'}

# person["language"] = "Python"  # Adding a new key-value pair
# print(person)

# Duplicates
# person = {
#     "name": "John",
#     "name": "Eva",
# }
# print(person)  # Output: {'name': 'Eva'} - The last value for the duplicate key is retained

#Access keys that doesnt exist
# person = {
#     "name": "John",
#     "age": 30,
# }

# print(person["city"]) ## This will raise a KeyError because "city" does not exist in the dictionary
# print(person.get("city"))  # Output: None - get() returns the default value if the key doesn't exist
# print(person.get("city", "unknown"))  # Output: unknown - get() returns the default value if the key doesn't exist


# person = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }

# print(person.keys())    # Output: dict_keys(['name', 'age', 'city']) - Returns a view of the keys in the dictionary
# print(person.values())  # Output: dict_values(['John', 30, 'New York']) - Returns a view of the values in the dictionary
# print(person.items())   # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')]) - Returns a view of the key-value pairs in the dictionary



# students = [
#     {"name": "John", "age": 30, "city": "New York"},
#     {"name": "Eva", "age": 25, "city": "Los Angeles"},
#     {"name": "Mike", "age": 35, "city": "Chicago"}
# ]

# how to get Evas age
# print(students[1]["age"])  # Output: 25 - Accessing the age of the second student (Eva) in the list of dictionaries

# list inside a dictionary
# students = [
#     {"name": "John", "age": 30, "city": "New York"},
#     {"name": "Eva", "age": 25, "city": "Los Angeles", "hobbies": ["reading", "traveling", "swimming"]},
#     {"name": "Mike", "age": 35, "city": "Chicago"}
# ]

# # get the second hobbie
# print(students[1]["hobbies"][1]) # "traveling"
