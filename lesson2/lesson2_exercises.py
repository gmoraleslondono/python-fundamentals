#Part A - List
# #1
# languages = ["Python", "Java", "C#", "R", "Julia", "Javascript", "Go", "Kotlin", "Ruby"]
# print(languages[0])
# print(languages[-1])
# print(languages[2])
# print(languages[-2])

# #2
# languages = ["Python", "Java", "C#", "R", "Julia", "Javascript", "Go", "Kotlin", "Ruby"]
# print(languages[0:3])
# print(languages[3:5])
# print(languages[5:len(languages)])
# print(languages[::-1])

# #3
# languages = ["Python", "Java", "C#", "R", "Julia", "Javascript", "Go", "Kotlin"]
# languages.append("Rust")
# print(languages)
# languages.insert(1, "Ruby")
# print(languages)
# languages.remove("R")
# print(languages)
# languages.pop()
# print(languages)

# #4
# numbers = [9, 8, 7, 6, 5, 4, 3]
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

#5
# numbers = [9, 1, 8, 2, 7, 6, 5, 4, 3]
# numbers.sort()
# print(numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers.reverse()
# print(numbers) # [9, 8, 7, 6, 5, 4, 3, 2, 1]
# new_numbers = sorted(numbers)
# print(new_numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# The difference between sort() and sorted() is that sort() modify the origin list while the sorted() doesn't modify the source list

# # 6
# # reference issue
# list_a = [1, 2, 3]
# list_b = list_a

# list_b. append(4)
# print(list_a) # [1, 2, 3, 4]
# print(list_b) # [1, 2, 3, 4]

# #solve reference issue
# list_a = [1, 2, 3]
# list_b = list_a.copy()

# list_b. append(4)
# print(list_a) # [1, 2, 3]
# print(list_b) # [1, 2, 3, 4]

# #Part B
# #1
# rbg_value = (1.5, 1, 1.2)
# r, b, g = rbg_value
# print(r) # 1.5
# print(b) # 1
# print(g) # 1.2

# #2
# person = ("Anna", 30, "Stockholm")
# name, age, city = person
# print(f"She is {name}, she is {age} years old and lives in {city}") # She is Anna, she is 30 years old and lives in Stockholm

# #3
# coordinates = (1.34, 0.23)
# print(coordinates[0]) # 1.34
# coordinates[0] = 2
# print(coordinates) # Throws error
# # The tuples values can be accessed but not modified. a Tuple is immutable

# # Part C
# # 1
# courses = ["Math", "English", "Art", "Math", "Sports", "Art"]
# print(len(courses)) # 6
# courses_set = set(courses)
# print(courses_set) # {'Math', 'English', 'Sports', 'Art'}
# print(len(courses_set)) # 4

# # 2
# front_developer = {"communication", "CSS", "UX", "Javascript", "Python"}
# back_developer = {"Python", "communication", "SQL", "Database"}
# #similar skills
# similar_skills = front_developer & back_developer
# print(similar_skills) # {'communication', 'Python'}
# #skill only the first has
# front_particular_skills = front_developer - back_developer
# print(front_particular_skills) # {'UX', 'CSS', 'Javascript'}

# # 3
# front_developer = {"communication", "CSS", "UX", "Javascript", "Python"}
# front_developer.add("UI")
# print(front_developer) # {'Python', 'Javascript', 'UI', 'communication', 'UX', 'CSS'}
# front_developer.remove("Python")
# print(front_developer) # {'Javascript', 'UI', 'communication', 'UX', 'CSS'}

# # 4
# A set is better than a list when you need to get unique values, for example in a shopping list.

# # Part D
# # 1 (Dictionary)
# laptop = {
#     "brand" : "Apple",
#     "model" : 2021,
#     "RAM" : "128Gb",
#     "storage" : "2T",
#     "price" : 15000
# }

# print(laptop["brand"])
# print(laptop["model"])
# print(laptop["RAM"])
# print(laptop["storage"])
# print(laptop["price"])

# # 2
# # Modify price
# laptop["price"] = 15500
# print(laptop["price"])

# # Add a new key
# laptop["operating_system"] = "Mac"
# print(laptop)

# # remove a key
# del laptop["model"]
# print(laptop)

# # remove a key
# laptop.pop("RAM")
# print(laptop)

# # 3
# print(laptop.get("color")) # None
# print(laptop.get("brand")) # Apple

# print(laptop["color"]) # Throw an error
# print(laptop["brand"]) # Apple

# # 4
# print(laptop.keys()) # dict_keys(['brand', 'model', 'RAM', 'storage', 'price'])
# print(laptop.values()) # dict_values(['Apple', 2021, '128Gb', '2T', 15000])

# # 5
# courses = {
#     "Math": 15,
#     "English": 5,
#     "Sports": 5,
#     "Art" : 10,
#     "Swedish": 5
# }

# hours = courses.values()
# print(hours) # dict_values([15, 5, 5, 10, 5])
# total_hours = sum(hours)
# print(total_hours) # 40


# Part E (Nested collections)
# 1
# books = [
#     {
#         "title": "1984",
#         "author": "George Orwell",
#         "pages": 328,
#         "available": True
#     },
#     {
#         "title": "The Hobbit",
#         "author": "J.R.R. Tolkien",
#         "pages": 310,
#         "available": True
#     },
#     {
#         "title": "Dune",
#         "author": "Frank Herbert",
#         "pages": 412,
#         "available": False
#     },
#     {
#         "title": "Harry Potter",
#         "author": "J.K. Rowling",
#         "pages": 309,
#         "available": True
#     },
#     {
#         "title": "The Alchemist",
#         "author": "Paulo Coelho",
#         "pages": 208,
#         "available": False
#     }
# ]

# print(books[2]["title"]) # Dune
# print(books[-1]["available"]) # False

# books[0]["gender"] = "Mystery"
# print(books) # [{'title': '1984', 'author': 'George Orwell', 'pages': 328, 'available': True, 'gender': 'Mystery'}, {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'pages': 310, 'available': True}, {'title': 'Dune', 'author': 'Frank Herbert', 'pages': 412, 'available': False}, {'title': 'Harry Potter', 'author': 'J.K. Rowling', 'pages': 309, 'available': True}, {'title': 'The Alchemist', 'author': 'Paulo Coelho', 'pages': 208, 'available': False}]

# departments = {
#     "finance" : ["Anna", "Jhon", "Paul"],
#     "HR" : ["Paula", "Irem"],
#     "Tech" : ["Cecilia", "Tomas", "Mateo"]
# }

# courses = [
#     {
#         "name" : "math",
#         "teacher" : "Anna",
#         "topics" : ["math1", "math2"]
#     },
#     {
#         "name" : "art",
#         "teacher" : "Eva",
#         "topics" : ["art1", "art2", "art3"]
#     },
#     {
#         "name" : "English",
#         "teacher" : "Luis",
#         "topics" : ["english1"]
#     }
# ]

# print(courses[2]["topics"][0]) # english1



# Part F (Applied challenge: Personal media catalogue)
# # 1
# books = [
#     {
#         "title": "1984",
#         "author": "George Orwell",
#         "pages": 328,
#         "available": True,
#         "info": ("book-001", 1949)
#     },
#     {
#         "title": "Animal Farm",
#         "author": "George Orwell",
#         "pages": 112,
#         "available": True,
#         "info": ("book-002", 1945)
#     },
#     {
#         "title": "Dune",
#         "author": "Frank Herbert",
#         "pages": 412,
#         "available": False,
#         "info": ("book-003", 1965)
#     },
#     {
#         "title": "Harry Potter",
#         "author": "J.K. Rowling",
#         "pages": 309,
#         "available": True,
#         "info": ("book-004", 1997)
#     },
#     {
#         "title": "The Alchemist",
#         "author": "Paulo Coelho",
#         "pages": 208,
#         "available": False,
#         "info": ("book-005", 1988)
#     },
#     {
#         "title": "The Martian",
#         "author": "Andy Weir",
#         "pages": 369,
#         "available": True,
#         "info": ("book-006", 2011)
#     },
#     {
#         "title": "Pride and Prejudice",
#         "author": "Jane Austen",
#         "pages": 279,
#         "available": False,
#         "info": ("book-007", 1813)
#     },
#     {
#         "title": "The Great Gatsby",
#         "author": "F. Scott Fitzgerald",
#         "pages": 180,
#         "available": True,
#         "info": ("book-008", 1925)
#     }
# ]

# unique_authors = set()

# for book in books:
#     unique_authors.add(book["author"])

# print(unique_authors) # {'George Orwell', 'Frank Herbert', 'F. Scott Fitzgerald', 'Paulo Coelho', 'Jane Austen', 'J.K. Rowling', 'J.R.R. Tolkien'}

# 5
# print(books[0]) # {'title': '1984', 'author': 'George Orwell', 'pages': 328, 'available': True, 'info': ('book-001', 1949)}
# print(books[0]["title"]) # 1984
# print(books[0]["info"][0]) # book-001
# print("George Orwell" in [book["author"] for book in books]) # True
# print(" " in books) # false
# print(books[2]["available"]) # False
# print(books[0].keys()) # dict_keys(['title', 'author', 'pages', 'available', 'info'])
# print(books[0].values()) # dict_values(['1984', 'George Orwell', 328, True, ('book-001', 1949)])
# print(books[0].items()) # dict_items([('title', '1984'), ('author', 'George Orwell'), ('pages', 328), ('available', True), ('info', ('book-001', 1949))])

# books[0]["genre"] = "Dystopian"
# print(books[0]) # {'title': '1984', 'author': 'George Orwell', 'pages': 328, 'available': True, 'info': ('book-001', 1949), 'genre': 'Dystopian'}

# # 6 - print summary catalogue
# print(books[0])
# print(books[1])
# print(books[2])
# print(books[3])
# print(books[4])
# print(books[5])
# print(books[6])
# print(books[7])


# Part G - Stretch Challenge
# # 1
# usernames1 = ["gloria", "maria", "john", "alex", "sofia"]
# usernames2 = ["john", "sofia", "david", "anna", "carlos"]

# # find duplicates
# duplicated_usernames = set(usernames1) & set(usernames2)
# print(duplicated_usernames) # {'john', 'sofia'}

# # find unique values
# unique_usernames = set(usernames1 + usernames2)
# print(unique_usernames) # {'alex', 'gloria', 'carlos', 'anna', 'john', 'sofia', 'david', 'maria'}

# # 2 - nested collection
# course_platform = {
#     "course1": {
#         "teacher": "teacher1",
#         "students": ["a", "b", "c", "d"],
#         "topics":[{"topic1": "1", "time": 10},{"topic2": "2", "time": 20}, {"topic3": "3", "time": 10}]
#     },
#     "course2": {
#         "teacher": "teacher2",
#         "students": ["a", "b", "c", "d"],
#         "topics":[{"topic1": "1", "time": 40}]
#     },
#     "course3": {
#         "teacher": "teacher3",
#         "students": ["a", "b", "c", "d"],
#         "topics":[{"topic1": "1", "time": 20},{"topic2": "2", "time": 20}]
#     }
# }

# # 3 - dictionary-based inventory
# products = {
#     "product1": {
#         "ref": "product1",
#         "stock": 10,
#         "price": 1000
#     },
#     "product2": {
#         "ref": "product2",
#         "stock": 8,
#         "price": 1200
#     },
#     "product3": {
#         "ref": "product3",
#         "stock": 4,
#         "price": 800
#     },
#     "product4": {
#         "ref": "product4",
#         "stock": 8,
#         "price": 150
#     },
#     "product5": {
#         "ref": "product5",
#         "stock": 2,
#         "price": 1100
#     }
# }

# # Update stock manually
# products["product1"]["stock"] = 15
# print(products["product1"]["stock"])

# products["product4"]["stock"] = 5
# print(products["product4"]["stock"])

# #calculate total units
# total_units = 0
# for product in products.values():
#     total_units = total_units + product["stock"]
# print(total_units)


# 4 - list vs tuple vs dictionary. Example
# list is used when a collection may change. Ex: adding, removing, accessing each element from a shopping list
# tuple is used when a collection should no change. Ex: coordinates
# dictionary is used when you want to associate a key with a value. Ex: Database

