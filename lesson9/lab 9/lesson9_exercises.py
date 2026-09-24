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

for notification in notifications:
    print(notification.send())
# Email Sent!
# SMS Sent!
# Message Sent!

# the loop doesn't need to know the exact class because Python is flexible and can work with objects of different type

