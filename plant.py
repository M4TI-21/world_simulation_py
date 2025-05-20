from organism import Organism
from abc import abstractmethod
from typing import Self
import random as rd

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
    
    @abstractmethod
    def copyOrganism(self, x, y) -> Self:
        pass  

    def action(self):
        sowSuccess = rd.randint(0, 4)
        if (sowSuccess):
            neighbouringPos = self.findNeighbouringPos(self.getX(), self.getY())

            if not neighbouringPos:
                self.world.addLog("No place to sow.")

            position = rd.randint(0, len(neighbouringPos) - 1)
            newX, newY = neighbouringPos[position]
            x = newX
            y = newY

            isFree = self.world.getOrganismPosition(x, y) == None

            if isFree:
                sowed_plant = self.copyOrganism(x, y)
                self.world.pushOrganism(sowed_plant)

    def collision(self, opponent):
        self.world.removeOrganism(self)
        self.world.addLog(f"{opponent.getTypeName()} ate {self.getTypeName()}")