# Lab 8

# Part A - Mutable default arguments
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

