# Lab 7

# Part A - Classes and objects
# 1
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


book1 = Book("Harry Potter and the Philosopher's Stone", "J. K. Rowling", 223)
book2 = Book("Harry Potter and the Chamber of Secrets", "J. K. Rowling", 251)
book3 = Book("Harry Potter and the Prisoner of Azkaban", "J. K. Rowling", 317)

# print(book1.title) # Harry Potter and the Prisoner of Azkaban
# print(book2.author) # J. K. Rowling
# print(book3.pages) # 317

# 2
class Laptop:
    def __init__(self, brand, model, ram_gb, price):
        self.brand = brand
        self.model = model
        self.ram_gb = ram_gb
        self.price = price

laptop1 = Laptop("Mac", 2021, 128, 1500)
laptop2 = Laptop("Windows", 2026, 164, 1200)
laptop3 = Laptop("Axus", 2023, 128, 900)

# print(laptop1.price) # 1500
# laptop1.price = 1400
# print(laptop1.price) # 1400

# 3
# print(laptop1 is laptop2) # False

# 4
class Laptop:
    def __init__(self, brand, model, price, ram_gb = 128):
        self.brand = brand
        self.model = model
        self.ram_gb = ram_gb
        self.price = price

# 5
laptop4 = Laptop(
    brand = "Mac",
    model = 2026,
    price = 1800
)

# print(laptop4.brand, laptop4.model, laptop4.price, laptop4.ram_gb) # Mac 2026 1800 128
