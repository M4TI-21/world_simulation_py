from animal import Animal
from defines import *
from world import World

class Sheep(Animal):
    def __init__(self, strength, initiative, age, x, y, prevX, prevY, world):
        super().__init__(strength, initiative, age, x, y, prevX, prevY, world)

    def getTypeName(self) -> str:
        return "Sheep"
    
    def copyOrganism(self, x, y):
        return self.__class__(4, 4, 0, x, y, 0, 0, self.world)

    def draw(self, board):
        board.create_oval(self.getX(), self.getY(), self.getX() + FIELD_SIZE, self.getY() + FIELD_SIZE, fill="white", outline="white", width="2")