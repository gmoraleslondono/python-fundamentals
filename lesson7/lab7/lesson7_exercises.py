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

# Part B - Methods and state
# 1
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self):
        if self.pages > 300:
            return True
        return False

book1 = Book("Harry Potter and the Philosopher's Stone", "J. K. Rowling", 223)
# print(book1.is_long()) # False

# 2 and 3
class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("No enough fonds")
        else:
            self.balance -= amount

# account1 = BankAccount("Anna", 800)
# print(account1.balance) # 800
# account1.deposit(100)
# print(account1.balance) # 900

# account1.withdraw(200)
# print(account1.balance) # 700
# account1.withdraw(900)
# print(account1.balance) # ValueError: No enough fonds

# 4
class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def complete(self):
       self.completed = True

    def reopen(self):
       self.completed = False

# 5
task1 = Task("Do dishes")
task2 = Task("Laundry")

# print(task1.completed) # False
# print(task2.completed) # False
# task1.completed = True
# print(task1.completed) # True
# print(task2.completed) # False

# Part C - Instance and class attributes
# 1, 2, 3
class Product:
    tax_rate = 0.25

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_with_tax(self):
        return self.price + (self.price * self.tax_rate)

# 4
product1 = Product(
    name = "orange",
    price = 500
)
# print(product1.price_with_tax()) # 625

product2 = Product(
    name = "apple",
    price = 200
)
# print(product2.price_with_tax()) # 250

product3 = Product(
    name = "kiwi",
    price = 350
)
# print(product3.price_with_tax()) # 437.5

# 5
Product.tax_rate = 0.88
# print(product1.price_with_tax()) # 940
# print(product2.price_with_tax()) # 376
# print(product3.price_with_tax()) # 658

# 6
product1.tax_rate = 0.5
# print(product1.price_with_tax()) # 750

print(product1.tax_rate) # 0.5
print(product2.tax_rate) # 0.88
print(Product.tax_rate) # 0.88


