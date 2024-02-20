from abc import ABC, abstractmethod
class Employee(ABC):

    @abstractmethod
    def donate(self):
        pass
    @abstractmethod
    def receive(self):
        pass

class Donation(Employee):
    def donate(self):
        pass# a = input("How much would you like to donate: ")
    def receive(self):
        pass



amounts = []
ben = Donation()
b = ben.donate()
amounts.append(b)
vasil = Donation()
v = vasil.donate()
amounts.append(v)
print(amounts)