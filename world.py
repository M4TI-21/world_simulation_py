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
        new_organism = None
        match type:
            case "Grass":
                from grass import Grass
                new_organism = Grass(0, 0, 0, 0, 0, 0, 0, self)
                self._organisms.append(new_organism)
            case "Sow_thistle":
                from sow_thistle import SowThistle
                new_organism = SowThistle(0, 0, 0, 0, 0, 0, 0, self)
                self._organisms.append(new_organism)
            case "Guarana":
                from guarana import Guarana
                new_organism = Guarana(0, 0, 0, 0, 0, 0, 0, self)
                self._organisms.append(new_organism)
            case "Belladonna":
                from belladonna import Belladonna
                new_organism = Belladonna(99, 0, 0, 0, 0, 0, 0, self)
                self._organisms.append(new_organism)
            case "Hogweed":
                from hogweed import Hogweed
                new_organism = Hogweed(10, 0, 0, 0, 0, 0, 0, self)
                self._organisms.append(new_organism)
            case "Sheep":
                from sheep import Sheep
                new_organism = Sheep(4, 4, 0, 0, 0, 0, 0, self)
                self._organisms.append(new_organism)
            case "Wolf":
                from wolf import Wolf
                new_organism = Wolf(9, 5, 0, 0, 0, 0, 0, self)
                self._organisms.append(new_organism)
            case "Fox":
                from fox import Fox
                new_organism = Fox(3, 7, 0, 0, 0, 0, 0, self)
                self._organisms.append(new_organism)
            case "Turtle":
                from turtle1 import Turtle
                new_organism = Turtle(2, 1, 0, 0, 0, 0, 0, self)
                self._organisms.append(new_organism)
            case "Antelope":
                from antelope import Antelope
                new_organism = Antelope(4, 4, 0, 0, 0, 0, 0, self)
                self._organisms.append(new_organism)
            case "Cybersheep":
                from cybersheep import Cybersheep
                new_organism = Cybersheep(11, 4, 0, 0, 0, 0, 0, self)
                self._organisms.append(new_organism)

        position = self.findPositions()

        if new_organism != None:
            new_organism.setPosition(position[0], position[1])
            self.addLog(f"{new_organism.getTypeName()} has been added.")

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