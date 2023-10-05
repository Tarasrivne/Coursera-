from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self,weight):
        pass

    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def sleep(self):
        pass

    def number_of_sleep_an_hours(self):
        print(f"dog sleeps four {self.sleep()}")


class Dog(Animal):

    def eat(self):
        print('meat')

    def sleep(self):
        print('10 hours')
        return '10 hours'
class Husky(Dog):

    def size(self):
        print('15 inc')


h = Husky(44)
h.size()
dog = Dog(44)
dog.eat()
dog.sleep()
dog.number_of_sleep_an_hours()
print(dog.weight)

