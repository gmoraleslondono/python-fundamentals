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

