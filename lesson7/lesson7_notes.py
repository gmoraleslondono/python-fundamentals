# oop

# Recap of previous class
# dictionary is a collection of key-value pairs
# methods used to perform operations on the data

student = {
    "name": "John",
    "score": 100,
    "active": True
}

# print(student)

def get_status(student):
    if student["score"] >= 60:
        return "Pass"
    else:
        return "Fail"

# print(get_status(student))

# ------------------------------------------------------------

# Relationship between data and behavior
# class : definition or blue print of an object
# object: a concrete instance of the class, instance created from the class

# student = class
# object : john, jane, jim


# first class
class Student: #(Student, BankAccount)
    pass  # class body empty

student1 = Student() # student1 is an instance of the Student class

# print(type(student1)) # class Student
# print(student1) # <__main__.Student object at 0x0000020268000000>

student2 = Student() # student2 is another instance of the Student class

# print(student1 is student2) # False they are different object even though they are the same class

# ------------------------------------------------------------

# Class

# Adding information manually

class Student:
    pass

student1 = Student()
student1.name = "John" # name is an instance attribute
student1.score = 100

# print(student1.name) # John
# print(student1.score) # 100


# object state : values assigned to the object (name, score)

student2 = Student()
student2.name = "Jane"
student2.score = 80

# print(student2.name) # Jane
# print(student2.score) # 80

# print(student1.name, student1.score) # John 100
# print(student2.name, student2.score) # Jane 80


student3 = Student()
student3.name = "Jim"

# print(student3.score) # will get an error because it expects to receive name, score an active

# ------------------------------------------------------------


# __init__ method: is a special method that is called when an object is created

class Student:
    def __init__(self, name, score): # self refers to the specific object that is being created (student1 or student2 ... etc)
        self.name = name
        self.score = score

student1 = Student("John", 100) # self -> student1 -> name = John, score = 100
# print(student1.name, student1.score)

student2 = Student("Jane", 80) # self -> student2 -> name = Jane, score = 80
# print(student2.name, student2.score)

# ------------------------------------------------------------


# class Student:
#     def __init__(self, name, score): # name and score are parameters, self refers to the specific object (student1 or student2 ... etc)
#         self.name = name # name stores the value of the name parameter
#         self.score = score # score stores the value of the score parameter

class Student:
    def __init__(self, student_name, student_score):
        self.name = student_name
        self.score = student_score


student1 = Student("John", 100) # self -> student 1 -> name = John, score = 100
# print(student1.name, student1.score)


# default values

class Student:
    def __init__(self, name, score = 0, active = True):
        self.name = name
        self.score = score
        self.active = active

student1 = Student("John", 100)
student2 = Student("Jane")

# print(student1.name, student1.score, student1.active)
# print(student2.name, student2.score, student2.active)


# keyword arguments

student3 = Student(
    name = "Jim",
    score = 60,
    active = False
)

# print(student3.name, student3.score, student3.active)

# ------------------------------------------------------------


# objects behavior : are the methods of the object

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def introduce(self):
        print(f"Hello, my name is {self.name}")

student1 = Student("John", 100)
# student1.introduce()

student2 = Student("Jane", 80)
# student2.introduce()

# introduce is a method of the Student class, it is being use for each student object referring to the self.name

# ------------------------------------------------------------


# Class method that returns a value get_status

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_status(self):
        if self.score >= 70:
            return "Pass"
        return "Fail"

# student1 = Student("John", 80)
# print(student1.get_status())

# student2 = Student("Jane", 62)
# print(student2.get_status())


# Class method that change the state of the object update_score

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def update_score(self, new_score):
        self.score = new_score

# student1 = Student("John", 100)
# print(student1.score)
# student1.update_score(80)
# print(student1.score)


# Class method validation and exceptions update_score

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def update_score(self, new_score):
        if new_score < 0 or new_score > 100:
            raise ValueError("Score must be between 0 and 100")
        self.score = new_score


# student = Student("John", 100)
# student.update_score(150) # ValueError: Score must be between 0 and 100
# print(student.score)


# Another example change the state of the object deposit()

class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

# account = BankAccount("John", 100)
# print(account.balance) # 100

# account.deposit(500)
# print(account.balance) # 600


# ------------------------------------------------------------

# Instance attributes (belong to a specific object)

class Student:
    def __init__(self, name):
        self.name = name

student1 = Student("Ada")
student1 = Student("Grace")

student1.name = "Ada Lovelace"

# print(student1.name) # Ada Lovelace
# print(student2.name) # Grace


# class attributes : value shared by all objects created from the same class

class Student:
    school = "Lexicon" # class attribute

    def __init__(self, name):
        self.name = name # instance attribute

student1 = Student("Ada")
student2 = Student("Grace")

# print(student1.school) # Lexicon
# print(student2.school) # Lexicon
# print(Student.school) # Lexicon


# changing the class attribute

Student.school = "AI Academy"

# print(student1.school) # AI Academy
# print(student2.school) # AI Academy
# print(Student.school) # AI Academy


# one object gets their own school attribute
# class attributes -> shared class level data
# instance attributes -> data belongs to an individual object

student1.school = "Another school"

# print(student1.school) # Another school
# print(student2.school) # AI Academy
# print(Student.school) # AI Academy


# Another example of class attributes

class Product:
    tax_rate = 0.25

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_with_tax(self):
        return self.price + (self.price * self.tax_rate)

# product1 = Product("Laptop", 1000)
# print(product1.price_with_tax()) # 1250

# product2 = Product("Phone", 500)
# print(product2.price_with_tax()) # 625


# ------------------------------------------------------------

# collection of objects: list of objects at the same time

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_status(self):
        if self.score >= 70:
            return "Pass"
        return "Fail"

students = [
    Student("John", 85),
    Student("Jane", 62),
    Student("Jim", 91)
]

# for student in students:
#     print(
#         student.name,
#         student.score,
#         student.get_status()
#         )

# John 85 Pass
# Jane 62 Fail
# Jim 91 Pass

# list comprehension
passed_students = [student for student in students if student.score >= 70]

# for student in passed_students:
#     print(student.name) # John, Jim

# ------------------------------------------------------------

# attribute can refer to another object

class Teacher:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

teacher = Teacher("John")
course = Course("Python foundation", teacher)

# print(course.name) # Python foundation
# print(course.teacher.name) # John



# ------------------------------------------------------------

class Student:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, name):
        self.name = name
        self.students = [] # internal variable (only accessible within the class)

    def add_student(self, student):
        self.students.append(student)

course = Course("Python foundation")

student1 = Student("John")
student2 = Student("Jane")

course.add_student(student1)
course.add_student(student2)

# for student in course.students:
#     print(student.name) # John, Jane


