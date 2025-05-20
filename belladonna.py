from plant import Plant
from defines import *
from world import World

class Belladonna(Plant):
    def __init__(self, strength, initiative, age, x, y, prevX, prevY, world):
        super().__init__(strength, initiative, age, x, y, prevX, prevY, world)

    def getTypeName(self):
        return "Belladonna"

    def copyOrganism(self, x, y):
        return self.__class__(99, 0, 0, x, y, 0, 0, self.world)

    def draw(self, board):
        board.create_rectangle(self.getX(), self.getY(), self.getX() + FIELD_SIZE, self.getY() + FIELD_SIZE, fill="blue", outline="blue", width="2")

    def collision(self, opponent):
        self.world.removeOrganism(opponent)
        self.world.removeOrganism(self)
        self.world.addLog(f"{opponent.getTypeName()} was killed by Belladonna")