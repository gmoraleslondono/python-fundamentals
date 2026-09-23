# Lab 8

# Part A - Mutable default arguments
# 1. Create a BadTeam class with name and a default parameter members=[]. Add an add_member()
# method.
# 2. Create two BadTeam objects without providing a members list. Add a member to only one team and
# print both lists. Explain in a comment what happened.
# 3. Create a corrected Team class using None as the default value and create a new list inside __init__.
# 4. Repeat the test with two Team objects and show that each object now has its own list.

# Solution:
# 1
class BadTeam():
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add_member(self, member):
        self.members.append(member)

# 2
badTeam1 = BadTeam("baddies")
badTeam2 = BadTeam("just bad")

badTeam1.add_member("Juan")
# print(badTeam1.members) # ['Juan']
# print(badTeam2.members) # ['Juan']
# Both objects have same members list, since they inherit from BadTeam sharing same list

# 3
class Team():
    def __init__(self, name, members=None):
        self.name = name
        if members is None:
            self.members = []
        else:
            self.members = members

    def add_member(self, member):
        self.members.append(member)

# 4
badTeam1 = Team("baddies")
badTeam2 = Team("just bad")

badTeam1.add_member("Juan")
# print(badTeam1.members) # ['Juan']
# print(badTeam2.members) # []


# Part C - Inheritance fundamentals
# 1. Create a base class Account with owner and balance.
# 2. Create SavingsAccount(Account) with an additional interest_rate attribute.
# 3. Use super() so SavingsAccount reuses the initialization from Account.
# 4. Create at least two objects and print their attributes.
# 5. Write the "is-a" statement that explains why this inheritance relationship makes sense

# Solution:
# 1
class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self,  owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

saving1 = SavingsAccount("Anna", 100, 1)
# print(saving1.owner) # Anna
# print(saving1.balance) # 100
# print(saving1.interest_rate) # 1

saving1 = SavingsAccount("Peter", 80, 0.25)
# print(saving1.owner) # Peter
# print(saving1.balance) # 80
# print(saving1.interest_rate) # 0.25

# SavingsAccount is an Account -> yes. So it makes sense that the child class SavingsAccount inherit from parent class Account


# Part E - super() and shared initialization
# 1. Create a base class Device with brand and year.
# 2. Add useful shared initialization logic inside Device, for example validation that year cannot be negative and an attribute such as is_active=True.
# 3. Create Laptop(Device) with one additional attribute such as ram_gb. Use super().
# 4. Create another Device subclass with its own additional attribute and use super() again.
# 5. Demonstrate that both subclasses receive the shared initialization logic from Device without duplicating it.

# Solution:
class Device():
    is_active = True

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

        if year < 0:
            raise ValueError("Year can not be negative value")

class Laptop(Device):
    def __init__(self, brand, year, ram_gb):
        super().__init__(brand, year)
        self.ram_gb = ram_gb

class Tv(Device):
    def __init__(self, brand, year, inches):
        super().__init__(brand, year)
        self.inches = inches

laptop1 = Laptop("mac", 2026, 128)
tv1 = Tv("lg", 2025, 25)

# print(laptop1.brand) # mac
# print(laptop1.is_active) # True
# print(tv1.brand) # lg
# print(tv1.is_active) # True


# Part F - Method overriding
# 1. Create a base class Notification with a method send() that returns a general message.
# 2. Create EmailNotification(Notification) and SMSNotification(Notification).
# 3. Override send() in both subclasses so each returns a different message.
# 4. Create one object from each class and call send() on all of them.
# 5. Explain in a comment which method is used when send() is called on each object.

# Solution:

class Notification:
    def send(self):
         return f"Message sent!"

class EmailNotification(Notification):
    def send(self):
        return f"Email sent!"

class SMSNotification(Notification):
    def send(self):
        return f"SMS sent!"

new_email = EmailNotification()
new_sms = SMSNotification()

#In this case the new_email is calling the send() method inside the EmailNotification class, because it override the method from the parent class
# print(new_email.send()) # Email sent!

# In this case the new_sms object is using the send() method inside SMSNotification class, because it override the method from the parent class
# print(new_sms.send()) # SMS sent!


# Part G - Override and still use the base method
# 1. Create a base class Report with a method get_summary() that returns a general report summary.
# 2. Create SalesReport(Report) and override get_summary().
# 3. Inside the overridden method, call the base implementation using super() and add SalesReport-specific information.
# 4. Create a SalesReport object and print the final result.

# Solution:
class Report:
    def get_summary(self):
        return "This is the general report summary"

class SalesReport(Report):
    def get_summary(self):
            base_report = super().get_summary()
            return f"{base_report} + the sales report."

sales_report1 = SalesReport()
print(sales_report1.get_summary()) # This is the general report summary + the sales report.
