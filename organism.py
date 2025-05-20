from abc import abstractmethod

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
    
    @abstractmethod
    def draw(self):
        pass
    
    def setPosition(self, newX, newY):
        self.prevX = self.x
        self.prevY = self.y
        self.x = newX
        self.y = newY

    def increaseAge(self):
        self.age += 1
