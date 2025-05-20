from plant import Plant
from defines import *
from world import World

class Guarana(Plant):
    def __init__(self, strength, initiative, age, x, y, prevX, prevY, world):
        super().__init__(strength, initiative, age, x, y, prevX, prevY, world)

    def __str__(self):
        return "Guarana has been created."

    def getTypeName(self):
        return "Guarana"

    def draw(self, board):
        board.create_rectangle(self.getX(), self.getY(), self.getX() + FIELD_SIZE, self.getY() + FIELD_SIZE, fill="red", outline="red", width="2")