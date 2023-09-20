from abc import ABC, abstractmethod
class Employee(ABC):

    @abstractmethod
    def donate(self):
        pass
class Donation(Employee):
    def donate(self):
        a = input("How much would you like to donate: ")

amounts = []
ben = Donation()
b = ben.donate()
amounts.append(b)
vasil = Donation()
v = vasil.donate()
amounts.append(v)
print(amounts)