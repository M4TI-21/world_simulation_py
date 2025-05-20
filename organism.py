from abc import abstractmethod
from defines import *
class Organism:
    isAlive = True
    
    def __init__(self, strength, initiative, age, x, y, prevX, prevY, world):
        self.strength = strength
        self.initiative = initiative
        self.age = age
        self.x = x
        self.y = y
        self.prevX = prevX
        self.prevY = prevY
        self.world = world

    @abstractmethod
    def draw(self, board):
        pass
    
    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def collision(self, opponent):
        pass

    def getStrength(self):
        return self.strength
    
    def getInitiative(self):
        return self.initiative
    
    def getAge(self):
        return self.age
    
    def getX(self):
        return self.x
    
    def getY(self): 
        return self.y
    
    def getPrevX(self):
        return self.prevX
    
    def getPrevY(self):
        return self.prevY

    def setPosition(self, newX, newY):
        self.x = newX
        self.y = newY

    def setPrevPosition(self, x, y):
        self.prevX = x
        self.prevY = y

    def findNeighbouringPos(self, x, y):
        neighbouringPos = []
        field = FIELD_SIZE

        if x - field >= 0:
            neighbouringPos.append([x - field, y])
        if x + field <= BOARD_SIZE - field:
            neighbouringPos.append([x + field, y])
        if y - field >= 0:
            neighbouringPos.append([x, y - field])
        if y + field <= BOARD_SIZE - field:
            neighbouringPos.append([x, y + field])

        return neighbouringPos

    def increaseAge(self):
        self.age += 1