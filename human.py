from animal import Animal
from defines import *
from turtle1 import Turtle
class Human(Animal):
    def __init__(self, strength, initiative, age, x, y, prevX, prevY, world):
        super().__init__(strength, initiative, age, x, y, prevX, prevY, world)
        self.ability_active = 0
        self.ability_cooldown = 0
        world.addLog("Human has been created")

    def getTypeName(self) -> str:
        return "Human"
    
    def copyOrganism(self, x, y):
        return self.__class__(5, 4, 0, x, y, 0, 0, self.world)

    def draw(self, board):
        board.create_rectangle(self.getX(), self.getY(), self.getX() + FIELD_SIZE, self.getY() + FIELD_SIZE, fill="black", outline="black", width="2")

    def humanMovement(self, key):
        field = FIELD_SIZE
        x = self.getX()
        y = self.getY()
        newX, newY = x, y
        if key == "UP":
            if y - field >= 0:
                newY -= field
            else:
                return False, [0, 0]
        elif key == "DOWN":
            if y + field < BOARD_SIZE - field:
                newY += field
            else:
                return False, [0, 0]
        elif key == "RIGHT":
            if x + field < BOARD_SIZE - field:
                newX += field
            else:
                return False, [0, 0]
        elif key == "LEFT":
            if x - field < BOARD_SIZE - field:
                newX -= field
            else:
                return False, [0, 0]
            
        return True, [newX, newY]

    def action(self, key=None):
        self.setPrevPosition(self.getX(), self.getY())

        if not key:
            return

        if key.lower() == "a":
            if self.ability_active == 0 and self.ability_cooldown == 0:
                self.ability_active = 5
                self.ability_cooldown = 5
                self.world.addLog("Human activated special ability")
                neighbourPos = self.findNeighbouringPos(self.getX(), self.getY())
                self.specialAbility(neighbourPos)
                return
            else:
                self.world.addLog("Ability is not ready yet. " + self.abilityStatus())
                return
            
        success, new_pos = self.humanMovement(key)
        if success:
            newX, newY = new_pos
            neighbourPos = self.findNeighbouringPos(self.getX(), self.getY())
            self.specialAbility(neighbourPos)

            met_organism = self.world.getOrganismPosition(newX, newY)

            if self.ability_active == 0 and met_organism and met_organism != self:
                if met_organism.getTypeName() != self.getTypeName():
                    self.setPosition(newX, newY)
                    self.collision(met_organism)
            elif self.ability_active > 0 and met_organism:
                self.world.addLog(f"Human defeated {met_organism.getTypeName()}")
                self.world.removeOrganism(met_organism)
                self.setPosition(newX, newY)
            else:
                self.setPosition(newX, newY)

        if self.ability_active > 0:
            self.ability_active -= 1
        elif self.ability_cooldown > 0:
            self.ability_cooldown -= 1

    def collision(self, opponent):
        isOppAnimal = isinstance(opponent, Animal)
        opponentType = opponent.getTypeName()
        
        if isOppAnimal:
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

    def specialAbility(self, positions):
        if self.ability_active > 0:
            for pos in positions:
                x, y = pos
                target = self.world.getOrganismPosition(x, y)
                if target and target != self:
                    self.world.removeOrganism(target)
                    if isinstance(target, Animal):
                        self.world.addLog(f"{target.getTypeName()} was killed by Human")
                    else:
                        self.world.addLog(f"{target.getTypeName()} was destroyed by Human")

    def abilityStatus(self):
        if self.ability_active > 0:
            return f"Ability active for {self.ability_active} more turns"
        elif self.ability_cooldown > 0:
            return f"Ability available in {self.ability_cooldown} turns"
        else:
            return "Press 'A' to activate special ability"

    def isAbilityActive(self):
        return self.ability_active > 0
    
    def getAbilityActive(self):
        return self.ability_active

    def setAbilityActive(self, isActive):
        self.ability_active = isActive
    
    def getAbilityCooldown(self):
        return self.ability_cooldown

    def setAbilityCooldown(self, isCooldown):
        self.ability_cooldown = isCooldown