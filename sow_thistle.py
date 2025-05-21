from plant import Plant
from defines import *
import random as rd

class SowThistle(Plant):
    def __init__(self, strength, initiative, age, x, y, prevX, prevY, world):
        super().__init__(strength, initiative, age, x, y, prevX, prevY, world)

    def getTypeName(self):
        return "Sow_thistle"
    
    def copyOrganism(self, x, y):
        return self.__class__(0, 0, 0, x, y, 0, 0, self.world)

    def draw(self, board):
        board.create_rectangle(self.getX(), self.getY(), self.getX() + FIELD_SIZE, self.getY() + FIELD_SIZE, fill="yellow", outline="yellow", width="2")

    def action(self):
        for _ in range(3):
            sowSuccess = rd.randint(0, 4)
            if sowSuccess == 0:
                neighbouringPos = self.findNeighbouringPos(self.getX(), self.getY())

                if not neighbouringPos:
                    self.world.addLog("No place to sow.")
                    return

                position = rd.randint(0, len(neighbouringPos) - 1)
                newX, newY = neighbouringPos[position]

                isFree = self.world.getOrganismPosition(newX, newY) == None

                if isFree:
                    sowed_plant = self.copyOrganism(newX, newY)
                    self.world.pushOrganism(sowed_plant)