from animal import Animal
from defines import *
from world import World
import random as rd

class Fox(Animal):
    def __init__(self, strength, initiative, age, x, y, prevX, prevY, world):
        super().__init__(strength, initiative, age, x, y, prevX, prevY, world)

    def getTypeName(self) -> str:
        return "Fox"
    
    def copyOrganism(self, x, y):
        return self.__class__(3, 7, 0, x, y, 0, 0, self.world)

    def draw(self, board):
        board.create_oval(self.getX(), self.getY(), self.getX() + FIELD_SIZE, self.getY() + FIELD_SIZE, fill="orange", outline="orange", width="2")

    def action(self):
        self.setPrevPosition(self.getX, self.getY)

        neighbouringPos = self.findNeighbouringPos(self.getX(), self.getY())
        safePos = []
        for pos in neighbouringPos:
            posX, posY = pos
            opponent = self.world.getOrganismPosition(posX, posY)
            if not opponent or opponent.getStrength() <= self.getStrength():
                safePos.append(pos)

        if not neighbouringPos:
            self.world.addLog("No place to move.")

        position = rd.randint(0, len(neighbouringPos) - 1)
        newX, newY = neighbouringPos[position]
        x = newX
        y = newY

        met_organism = self.world.getOrganismPosition(x, y)

        if met_organism and met_organism != self:
            if met_organism.getTypeName() == self.getTypeName():
                neighbouringPos.pop(position)
                if not neighbouringPos:
                    self.world.addLog("No space for new animal")
                    return
                else:
                    position = rd.randint(0, len(neighbouringPos) - 1)
                    newX = neighbouringPos[0]
                    newY = neighbouringPos[1]

                    new_animal = self.copyOrganism(newX, newY)
                    self.world.pushOrganism(new_animal)
                    return
            else:
                self.collision(met_organism)
        
        if not met_organism or met_organism.getTypeName() != self.getTypeName():
            self.setPosition(x, y)