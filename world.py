from organism import Organism
import random as rd
from defines import *

class World:
    logs = []
    round_number = 0
    def __init__(self):
        self._organisms = []        #_name means - private

    def addLog(self, log):
        self.logs.append(log)

    def printLogs(self):
        for log in self.logs:
            print(log)

    def drawWorld(self, board):
        for organism in self._organisms:
            organism.draw(board)

        self.printLogs()
        
    def addNewOrganism(self, type):
        match type:
            case "Grass":
                from grass import Grass
                new_organism = Grass(0, 0, 0, 0, 0, 0, 0, self)
                self._organisms.append(new_organism)
            case "Sow thistle":
                from sow_thistle import SowThistle
                new_organism = SowThistle(0, 0, 0, 0, 0, 0, 0, self)
                self._organisms.append(new_organism)
            case "Guarana":
                from guarana import Guarana
                new_organism = Guarana(0, 0, 0, 0, 0, 0, 0, self)
                self._organisms.append(new_organism)

        position = self.findPositions()
        new_organism.setPosition(position[0], position[1])
        self.addLog(f"{new_organism.getTypeName()} has been created at position ({position[0]}, {position[1]})")

    def getOrganismPosition(self, x, y):
        for organism in self._organisms:
            if organism.getX() == x and organism.getY() == y:
                return organism
            else:
                return

    def findPositions(self):
        while True:
            # generate random coordinates
            randX = rd.randint(0, (BOARD_SIZE // FIELD_SIZE) - FIELD_SIZE)
            randY = rd.randint(0, (BOARD_SIZE // FIELD_SIZE) - FIELD_SIZE)

            x = randX * FIELD_SIZE
            y = randY * FIELD_SIZE

            # check if they are occupied
            isOcuppied = self.getOrganismPosition(x, y) != None
            if isOcuppied:
                continue
            else:
                return [x, y]