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
