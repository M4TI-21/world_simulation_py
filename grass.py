from plant import Plant
from defines import *
from world import World

class Grass(Plant):
    def __init__(self, strength, initiative, age, x, y, prevX, prevY, world):
        super().__init__(strength, initiative, age, x, y, prevX, prevY, world)

    def __str__(self):
        return "Grass has been created."

    def getTypeName(self):
        return "Grass"

    def draw(self, board):
        board.create_rectangle(self.getX(), self.getY(), self.getX() + FIELD_SIZE, self.getY() + FIELD_SIZE, fill="green", outline="green", width="2")