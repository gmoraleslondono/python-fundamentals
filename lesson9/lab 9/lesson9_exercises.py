# Lab 9 Exercises

# Part A - Polymorphism
# 1. Create three classes: EmailNotification, SMSNotification and PushNotification.
# 2. Give all three classes a method called send(), but make each method return a different message.
# 3. Create one object from each class and store them in the same list.
# 4. Loop through the list and call send() on every object.
# 5. In a comment, explain why the loop does not need to know the exact class of each object.

# Solution:

class EmailNotification:
    def send(self):
        return "Email Sent!"

class SMSNotification:
    def send(self):
        return "SMS Sent!"

class PushNotification:
    def send(self):
        return "Message Sent!"

email = EmailNotification()
sms = SMSNotification()
general_notification = PushNotification()

notifications = [email, sms, general_notification]

# for notification in notifications:
#     print(notification.send())
# Email Sent!
# SMS Sent!
# Message Sent!

# the list doesn't need to contain elements from the exact same class because Python is flexible and can work with objects of different type

# Part C - Duck typing
# 1. Create two unrelated classes, for example Printer and Screen. Do not use inheritance between them.
# 2. Give both classes a method called display_status().
# 3. Create objects from both classes and store them in the same list.
# 4. Loop through the list and call display_status() on each object.
# 5. In a comment, explain why this works even though the classes do not share a base class.


# Solution:

class Printer:
    def display_status(self):
        return "Printer status"

class Screen:
    def display_status(self):
        return "Screen status"

printer1 = Printer()
printer2 = Printer()

screen1 = Screen()
screen2 = Screen()

appliances = [printer1, screen1, printer2, screen2]

# for appliance in appliances:
#     print(appliance.display_status())
# Printer status
# Screen status
# Printer status
# Screen status

# the list doesn't need to contain elements from the exact same class because Python is flexible and can work with objects of different type

# Part E - __str__
# 1. Create a Product class with name and price.
# 2. Create one Product object and print it before defining __str__. Observe the result.
# 3. Add __str__ so printing the Product gives a useful human-readable description.
# 4. Create at least three Product objects and print them.
# 5. Use str() on one Product object, store the result in a variable and print its type.

# Solution:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}"

product1 = Product("orange", 500)
# print(product1) # <__main__.Product object at 0x101168c20>
# print(str(product1)) # orange - 500

product2 = Product("apple", 200)
product3 = Product("grapes", 400)

# print(str(product2)) # apple - 200
# print(str(product3)) # grapes - 400

text= str(product2)
# print(type(text)) # <class 'str'>


# Part G - Inheritance or composition?
# 1. Create CPU with a model attribute.
# 2. Create Computer with brand and a CPU object. Use composition, not inheritance.
# 3. Create a CPU object and pass it to a Computer object.
# 4. Print the computer brand and CPU model through the Computer object.
# 5. In comments, explain why "Computer HAS-A CPU" makes more sense than "Computer IS-A CPU".
# 6. For each pair below, write whether you would most likely use inheritance (IS-A) or composition (HAS-A): Car / Engine, Manager / Employee, Course / Teacher, Phone / Device.

# Solution:

class CPU:
    def __init__(self, model):
        self.model = model

class Computer:
    def __init__(self, brand, CPU):
        self.brand = brand
        self.CPU = CPU

cpu1 = CPU("intel")
cpu2 = CPU("AMD")

computer1 = Computer("mac", cpu1 )
# print(computer1.brand) # mac
# print(computer1.CPU.model) # intel
# this is a relationship "Has A" because a computer has a CPU -> composition
# it is not inheritance because a CPU is not a computer or vice versa.

# Car / Engine -> composition: a Car "HAS A" Engine
# Manager / Employee -> inheritance: a Manager "IS A" employee
# Course / Teacher -> composition: a Course "HAS A" Teacher
# Phone / Device -> inheritance: a Phone "IS A" Device

