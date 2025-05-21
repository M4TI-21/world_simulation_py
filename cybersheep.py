from animal import Animal
from defines import *
from world import World

class Cybersheep(Animal):
    def __init__(self, strength, initiative, age, x, y, prevX, prevY, world):
        super().__init__(strength, initiative, age, x, y, prevX, prevY, world)

    def getTypeName(self) -> str:
        return "Cybersheep"
    
    def copyOrganism(self, x, y):
        return self.__class__(11, 4, 0, x, y, 0, 0, self.world)

    def draw(self, board):
        board.create_oval(self.getX(), self.getY(), self.getX() + FIELD_SIZE, self.getY() + FIELD_SIZE, fill="pink", outline="pink", width="2")

    def action(self):
        self.setPrevPosition(self.getX(), self.getY())

        hogweeds = []
        for organism in self.world.getOrganisms():
            if organism.getTypeName() == "Hogweed" and organism.isAlive:
                hogweeds.append(organism)

        if hogweeds:
            min_distance = float("inf")
            target = None
            for hogweed in hogweeds:
                distance = abs(self.getX() - hogweed.getX()) + abs(self.getY() - hogweed.getY())
                if distance < min_distance:
                    min_distance = distance
                    target = hogweed

            if target:
                x = self.getX()
                y = self.getY()
                targetX = target.getX()
                targetY = target.getY()

                neighbouringPos = self.findNeighbouringPos(x, y)
                best_pos = None
                best_dist = min_distance

                for pos in neighbouringPos:
                    posX, posY = pos
                    dist = abs(posX - targetX) + abs(posY - targetY)
                    if dist < best_dist:
                        best_dist = dist
                        best_pos = pos

                if best_pos:
                    newX, newY = best_pos
                    met_organism = self.world.getOrganismPosition(newX, newY)

                    if met_organism:
                        self.collision(met_organism)
                    else:
                        self.setPosition(newX, newY)
                    return

        super().action()

    def collision(self, opponent):
        if opponent.getTypeName() == "Hogweed":
            self.world.removeOrganism(opponent)
            self.world.addLog(f"Cybersheep ate {opponent.getTypeName()}")
        else:
            super().collision(opponent)