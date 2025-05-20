from animal import Animal
from defines import *
from world import World

class Cybersheep(Animal):
    def __init__(self, strength, initiative, age, x, y, prevX, prevY, world):
        super().__init__(strength, initiative, age, x, y, prevX, prevY, world)

    def getTypeName(self) -> str:
        return "Cybersheep"
    
    def copyOrganism(self, x, y):
        return self.__class__(11, 4, 0, x, y, 0, 0, self.world)

    def draw(self, board):
        board.create_oval(self.getX(), self.getY(), self.getX() + FIELD_SIZE, self.getY() + FIELD_SIZE, fill="pink", outline="pink", width="2")