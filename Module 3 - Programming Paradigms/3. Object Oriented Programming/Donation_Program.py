from abc import ABC, abstractmethod 

class Employee (ABC):

    @abstractmethod
    def donate(self):
        pass

class Donation(Employee):
    
    def donate(self):
        a = input("How much would you like to donate: ")
        return a
    
amounts = []

john = Donation()
amounts.append(john.donate())

jane = Donation()
amounts.append(jane.donate())

total = 0

for x in amounts:
    total += int(x)

print("Total Donated Amount: " + str(total))