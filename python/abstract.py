from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def makesound(self):
        pass
class Lion(Animal):
    def makesound(self):
        print("Roar")
l=Lion()
l.makesound()