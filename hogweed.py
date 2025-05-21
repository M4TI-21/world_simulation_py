from plant import Plant
from animal import Animal
from defines import *
import random as rd

class Hogweed(Plant):
    def __init__(self, strength, initiative, age, x, y, prevX, prevY, world):
        super().__init__(strength, initiative, age, x, y, prevX, prevY, world)

    def getTypeName(self):
        return "Hogweed"
    
    def copyOrganism(self, x, y):
        return self.__class__(10, 0, 0, x, y, 0, 0, self.world)

    def draw(self, board):
        board.create_rectangle(self.getX(), self.getY(), self.getX() + FIELD_SIZE, self.getY() + FIELD_SIZE, fill="white", outline="white", width="2")

    def action(self):
        sowSuccess = rd.randint(0, 4)
        neighbouringPos = self.findNeighbouringPos(self.getX(), self.getY())
        if sowSuccess == 0:

            if not neighbouringPos:
                self.world.addLog("No place to sow.")
                return

            position = rd.randint(0, len(neighbouringPos) - 1)
            newX, newY = neighbouringPos[position]

            isFree = self.world.getOrganismPosition(newX, newY) == None

            if isFree:
                sowed_plant = self.copyOrganism(newX, newY)
                self.world.pushOrganism(sowed_plant)

        for pos in neighbouringPos:
            x, y = pos

            target = self.world.getOrganismPosition(x, y)
            if target and isinstance(target, Animal) and target.getTypeName() != "Cybersheep":
                self.world.removeOrganism(target)
                self.world.addLog(f"{target.getTypeName()} was killed by Hogweed")



    def collision(self, opponent):
        if opponent.getTypeName() == "Cybersheep":
            opponent.action()
        else:
            self.world.removeOrganism(self)
            self.world.removeOrganism(opponent)
            self.world.addLog(f"{opponent.getTypeName()} was killed by Hogweed")