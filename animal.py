from organism import Organism
from abc import abstractmethod
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
        self.setPrevPosition(self.getX(), self.getY())

        neighbouringPos = self.findNeighbouringPos(self.getX(), self.getY())

        if not neighbouringPos:
            self.world.addLog("No place to move.")
            return

        position = rd.randint(0, len(neighbouringPos) - 1)
        newX, newY = neighbouringPos[position]

        met_organism = self.world.getOrganismPosition(newX, newY)

        if met_organism and met_organism != self:
            if met_organism.getTypeName() == self.getTypeName():
                neighbouringPos.pop(position)
                if not neighbouringPos:
                    self.world.addLog("No space for new animal")
                    return
                else:
                    position = rd.randint(0, len(neighbouringPos) - 1)
                    newX, newY = neighbouringPos[position]

                    new_animal = self.copyOrganism(newX, newY)
                    self.world.pushOrganism(new_animal)
                    return
            else:
                self.collision(met_organism)
        
        if not met_organism or met_organism.getTypeName() != self.getTypeName():
            self.setPosition(newX, newY)

    def collision(self, opponent):
        isOppAnimal = isinstance(opponent, Animal)
        opponentType = opponent.getTypeName()
        
        if isOppAnimal:
            # do opponents collision if it's a turtle
            if  opponentType == "Turtle":
                opponent.collision(self)
                return
            if self.getStrength() >= opponent.getStrength():
                self.world.removeOrganism(opponent)
                self.world.addLog(f"{self.getTypeName()} defeated {opponent.getTypeName()}")
            else:
                self.world.removeOrganism(self)
                self.world.addLog(f"{opponent.getTypeName()} defeated {self.getTypeName()}")
        else:
            if opponentType == "Belladonna" or opponentType == "Hogweed":
                self.world.removeOrganism(self)
                self.world.removeOrganism(opponent)
                self.world.addLog(f"{self.getTypeName()} was killed by {opponent.getTypeName()}")
            elif opponentType == "Guarana":
                opponent.collision(self)
            else:
                self.world.removeOrganism(opponent)
                self.world.addLog(f"{self.getTypeName()} ate {opponent.getTypeName()}")