# Lab 7

# Part A - Classes and objects
# 1. Create a Book class with title, author and pages. Create at least four Book objects and print their attributes.
# 2. Create a Laptop class with brand, model, ram_gb and price. Create three separate objects and change the price of one object.
# 3. Create two objects with the same attribute values. Use is to check whether they are the same object.
# 4. Add a default value to at least one __init__ parameter.
# 5. Create one object using keyword arguments.

# Solution:

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
# 1. Extend your Book class with an is_long() method that returns True if the book has more than 300 pages.
# 2. Create a BankAccount class with owner and balance. Add a deposit() method that changes the balance.
# 3. Add a withdraw() method. Prevent withdrawals that would make the balance negative by raising a ValueError.
# 4. Create a Task class with title and completed=False. Add complete() and reopen() methods.
# 5. Create at least two objects from one of your classes and show that changing the state of one object does not change the other

# Solution:

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
# 1. Create a Product class with name and price as instance attributes.
# 2. Add a class attribute called tax_rate that is shared by all Product objects.
# 3. Add a price_with_tax() method that returns the price including tax.
# 4. Create at least three Product objects and print their prices with tax.
# 5. Change Product.tax_rate and show how it affects the Product objects.
# 6. Give one Product object its own tax_rate. Print the tax rate from that object, another Product object and the Product class.

# Solution:

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

# print(product1.tax_rate) # 0.5
# print(product2.tax_rate) # 0.88
# print(Product.tax_rate) # 0.88


# Part F - Applied challenge: Course manager
# 1. Build a small course management program using Student, Teacher and Course classes.
# 2. Student should contain at least name and score.
# 3. Student should have a method that returns "PASS" or "FAIL".
# 4. Teacher should contain at least a name.
# 5. Course should contain a name, a Teacher object and a list of Student objects.
# 6. Add methods for adding a student and showing how many students are currently in the course.
# 7. Add a method that returns a list containing only the students who passed.
# 8. Add validation somewhere in your program using ValueError. Choose a validation that makes sense.
# 9. Create at least five Student objects, one Teacher object and one Course object. Demonstrate that your methods work.
# 10. Print a simple course summary containing the course name, teacher name, number of students and the names of the students who passed.


# Solution:
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

        if self.score < 0 or self.score > 100:
            raise ValueError("The score must be a number between 0 and 100.")

    def grades(self):
        if self.score >= 70:
            return "PASS"
        return "FAIL"

class Teacher:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, name, teacher, students=None):
        self.name = name
        self.teacher = teacher
        self.students = students if students is not None else []

    def add_student(self, student):
        self.students.append(student)
        return len(self.students)

    def count_students(self):
        return len(self.students)

    def passed_students(self):
        passed = []
        for student in self.students:
            if student.grades() == "PASS":
                passed.append(student)
        return passed

student1 = Student("Anna", 80)
student2 = Student("Pedro", 70)
student3 = Student("Pablo", 45)
student4 = Student("Juan", 62)
student5 = Student("Edo", 87)
student6 = Student("Sara", 35)

teacher1 = Teacher("Roberto")

course1 = Course("Python", teacher1, [student1, student2, student3, student4, student5])

# print(course1.count_students()) # 5
# print(course1.add_student(student6)) # 6

# for student in course1.students:
#     print(student.name) # Anna Pedro Pablo Juan Edo Sara

# for student in course1.passed_students():
#     print(student.name) # Anna Pedro Edo


def course_summary(course):
    print("--------------------")
    print("Course Summary")
    print("--------------------")
    print(f"Course: {course.name}")
    print(f"Teacher: {course.teacher.name}")
    print(f"Number of students: {course.count_students()}")
    print(f"Name of students that passed: ")
    for position, student in enumerate(course.passed_students(), start=1):
        print(position, student.name)

course_summary(course1)
