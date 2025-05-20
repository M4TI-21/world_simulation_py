from organism import Organism
from abc import abstractmethod
from world import World
import random as rd
from typing import Self

class Animal(Organism):
    def __init__(self, strength, initiative, age, x, y, prevX, prevY, world):
        super().__init__(strength, initiative, age, x, y, prevX, prevY, world)

    def __str__(self):
        return "Animal has been created."
    
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
        self.setPrevPosition(self.getX, self.getY)

        neighbouringPos = self.findNeighbouringPos(self.getX(), self.getY())

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


    def collision(self, opponent):
        pass