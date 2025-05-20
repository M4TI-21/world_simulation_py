from organism import Organism
from abc import abstractmethod

class Animal(Organism):
    def __init__(self, strength, initiative, age, x, y, prevX, prevY, world):
        super().__init__(strength, initiative, age, x, y, prevX, prevY, world)

    def __str__(self):
        return "Animal has been created."
    
    @abstractmethod
    def getTypeName(self):
        pass

    @abstractmethod
    def draw(self):
        pass
