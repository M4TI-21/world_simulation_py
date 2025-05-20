from organism import Organism
from abc import abstractmethod

class Plant(Organism):
    def __init__(self, strength, initiative, age, x, y, prevX, prevY, world):
        super().__init__(strength, initiative, age, x, y, prevX, prevY, world)

    def __str__(self):
        return "Plant has been created."
    
    @abstractmethod
    def getTypeName(self) -> str:
        pass

    @abstractmethod
    def draw(self, board):
        pass
