from abc import *

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def haul(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass
    
class Dog(Animal):
    def haul(self):
        print('멍멍')
    def eat(self):
        print('잡식')

d1 = Dog()
d1.haul()