from animal import Animal
from defines import *
import random as rd

class Turtle(Animal):
    def __init__(self, strength, initiative, age, x, y, prevX, prevY, world):
        super().__init__(strength, initiative, age, x, y, prevX, prevY, world)

    def getTypeName(self) -> str:
        return "Turtle"
    
    def copyOrganism(self, x, y):
        return self.__class__(2, 1, 0, x, y, 0, 0, self.world)

    def draw(self, board):
        board.create_oval(self.getX(), self.getY(), self.getX() + FIELD_SIZE, self.getY() + FIELD_SIZE, fill="green", outline="green", width="2")

    def action(self):
        moveSuccess = rd.randint(0, 3)
        if moveSuccess == 0:
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
            opponentStrength = opponent.getStrength()

            if opponentStrength < 5:
                self.world.addLog(f"{opponent.getTypeName()} was reflected by Turtle")
                opponent.setPosition(opponent.getPrevX(), opponent.getPrevY())
                return
            else:
                selfStrength = self.getStrength()
                if selfStrength >= opponentStrength:
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
