import random as rd
import tkinter as tk
from defines import *

class World:
    logs = []
    round_number = 1
    selected_organism = None
    human = None

    def __init__(self, log_console=None):
        self._organisms = []        # _name means - private
        self._human_moved = True
        self.log_console = log_console      # logs

    def addLog(self, log):
        self.logs.append(log)
        if self.log_console:
            self.log_console.config(state="normal")     # unlock editing of console
            for log in self.logs:
                self.log_console.insert(tk.END, log + "\n")     # display added message

            self.log_console.see(tk.END)
            self.log_console.config(state="disabled")   # disable editing

    def drawWorld(self, board):
        for organism in self._organisms:
            organism.draw(board)

    def addNewOrganism(self, type):
        new_organism = None
        match type:
            case "Grass":
                from grass import Grass
                new_organism = Grass(0, 0, 0, 0, 0, 0, 0, self)
            case "Sow_thistle":
                from sow_thistle import SowThistle
                new_organism = SowThistle(0, 0, 0, 0, 0, 0, 0, self)
            case "Guarana":
                from guarana import Guarana
                new_organism = Guarana(0, 0, 0, 0, 0, 0, 0, self)
            case "Belladonna":
                from belladonna import Belladonna
                new_organism = Belladonna(99, 0, 0, 0, 0, 0, 0, self)
            case "Hogweed":
                from hogweed import Hogweed
                new_organism = Hogweed(10, 0, 0, 0, 0, 0, 0, self)
            case "Sheep":
                from sheep import Sheep
                new_organism = Sheep(4, 4, 0, 0, 0, 0, 0, self)
            case "Wolf":
                from wolf import Wolf
                new_organism = Wolf(9, 5, 0, 0, 0, 0, 0, self)
            case "Fox":
                from fox import Fox
                new_organism = Fox(3, 7, 0, 0, 0, 0, 0, self)
            case "Turtle":
                from turtle1 import Turtle
                new_organism = Turtle(2, 1, 0, 0, 0, 0, 0, self)
            case "Antelope":
                from antelope import Antelope
                new_organism = Antelope(4, 4, 0, 0, 0, 0, 0, self)
            case "Cybersheep":
                from cybersheep import Cybersheep
                new_organism = Cybersheep(11, 4, 0, 0, 0, 0, 0, self)
            case "Human":
                from human import Human
                new_organism = Human(5, 4, 0, 0, 0, 0, 0, self)
                self.human = new_organism

        if new_organism != None:
            self._organisms.append(new_organism)
            position = self.findPositions()
            new_organism.setPosition(position[0], position[1])
            self.addLog(f"{new_organism.getTypeName()} has been added.")

    def makeTurn(self, board):
        self.addLog(f"---- Turn {self.round_number} has started ----")
        for organism in self._organisms:
            if organism.isAlive:
                if organism.getTypeName() == "Human" and self.human:
                    self.addLog(self.human.abilityStatus())
                else:
                    organism.action()

                organism.increaseAge()

        self.removeDeadOrganisms()
        self.addLog(f"---- Turn {self.round_number} has ended ----")
        self.addLog("Press 'S' to save the game.")
        self.addLog("Press 'L' to load saved game.")
        self.addLog("Press Spacebar to continue.")

        self.round_number += 1
        self.setHumanMoved(False)
        self.drawWorld(board)
        
    def getOrganismPosition(self, x, y):
        for organism in self._organisms:
            if organism.getX() == x and organism.getY() == y:
                return organism
        return

    def getOrganisms(self):
        return self._organisms

    def findPositions(self):
        while True:
            # generate random coordinates
            randX = rd.randint(0, (BOARD_SIZE // FIELD_SIZE) - 1)
            randY = rd.randint(0, (BOARD_SIZE // FIELD_SIZE) - 1)

            x = randX * FIELD_SIZE
            y = randY * FIELD_SIZE

            # check if they are occupied
            isOcuppied = self.getOrganismPosition(x, y) != None
            if isOcuppied:
                continue
            else:
                return [x, y]
            
    def removeOrganism(self, organism):
        if organism.getTypeName() == "Human":
            if self.human and self.human.isAbilityActive():
                return
        organism.kill()

    def removeDeadOrganisms(self):
        self._organisms = [org for org in self._organisms if org.isAlive]

    def pushOrganism(self, organism):
        self._organisms.append(organism)
        self.addLog(f"{organism.getTypeName()} has been added.")

    def selectOrganism(self, type):
        self.selected_organism = type
        self.addLog(f"Selected organism: {type}")

    def addOrganismOnClick(self, x, y, board):
        if not self.selected_organism:
            self.addLog("No organism selected")
            return

        x *= FIELD_SIZE
        y *= FIELD_SIZE
        organism = self.getOrganismPosition(x, y)
        if organism:
            self.addLog("Field already occupied")
            return
        else:
            self.addNewOrganism(self.selected_organism)
            new_organism = self._organisms[-1]
            if new_organism.getTypeName() == self.selected_organism:
                new_organism.setPosition(x, y)

        self.drawWorld(board)


    def hasHumanMoved(self):
        return self._human_moved
    
    def setHumanMoved(self, moved):
        self._human_moved = moved

    def handleHumanMovement(self, key, board):
        if self.human and self.human.isAlive and not self.hasHumanMoved():
            self.human.action(key)
            board.delete("all")
            self.drawWorld(board)
            self.setHumanMoved(True)

    def handleSpecialAbility(self, key):
        if self.human and self.human.isAlive and not self.hasHumanMoved():
            self.human.action(key)

    def saveGame(self):
        try:
            with open("save.txt", "w") as file:
                for organism in self._organisms:
                    if organism.getTypeName() == "Human":
                        file.write(f"{organism.getTypeName()} {organism.getStrength()} {organism.getInitiative()} {organism.getAge()} "
                                f"{organism.getX()} {organism.getY()} {organism.getAbilityActive()} {organism.getAbilityCooldown()}\n")
                    else:
                        file.write(f"{organism.getTypeName()} {organism.getStrength()} {organism.getInitiative()} {organism.getAge()} "
                                f"{organism.getX()} {organism.getY()}\n")
            self.addLog("Game has been saved")
        except Exception as e:
            self.addLog("Error while saving game")
            print(e)


    def loadGame(self):
        import os
        if not os.path.exists("save.txt"):
            self.addLog("There is no saved game")
            return

        self._organisms.clear()
        self.human = None

        try:
            with open("save.txt", "r") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue

                    data = line.split()

                    type_name = data[0]
                    strength = int(data[1])
                    initiative = int(data[2])
                    age = int(data[3])
                    x = int(data[4])
                    y = int(data[5])

                    new_organism = None

                    if type_name == "Sheep":
                        from sheep import Sheep
                        new_organism = Sheep(strength, initiative, age, x, y, 0, 0, self)
                    elif type_name == "Wolf":
                        from wolf import Wolf
                        new_organism = Wolf(strength, initiative, age, x, y, 0, 0, self)
                    elif type_name == "Fox":
                        from fox import Fox
                        new_organism = Fox(strength, initiative, age, x, y, 0, 0, self)
                    elif type_name == "Turtle":
                        from turtle1 import Turtle
                        new_organism = Turtle(strength, initiative, age, x, y, 0, 0, self)
                    elif type_name == "Antelope":
                        from antelope import Antelope
                        new_organism = Antelope(strength, initiative, age, x, y, 0, 0, self)
                    elif type_name == "Cybersheep":
                        from cybersheep import Cybersheep
                        new_organism = Cybersheep(strength, initiative, age, x, y, 0, 0, self)
                    elif type_name == "Grass":
                        from grass import Grass
                        new_organism = Grass(strength, initiative, age, x, y, 0, 0, self)
                    elif type_name == "Sow_thistle":
                        from sow_thistle import SowThistle
                        new_organism = SowThistle(strength, initiative, age, x, y, 0, 0, self)
                    elif type_name == "Guarana":
                        from guarana import Guarana
                        new_organism = Guarana(strength, initiative, age, x, y, 0, 0, self)
                    elif type_name == "Belladonna":
                        from belladonna import Belladonna
                        new_organism = Belladonna(strength, initiative, age, x, y, 0, 0, self)
                    elif type_name == "Hogweed":
                        from hogweed import Hogweed
                        new_organism = Hogweed(strength, initiative, age, x, y, 0, 0, self)
                    elif type_name == "Human":
                        from human import Human
                        ability_active = int(data[6])
                        ability_cooldown = int(data[7])
                        human = Human(strength, initiative, age, x, y, 0, 0, self)
                        human.setAbilityActive(ability_active)
                        human.setAbilityCooldown(ability_cooldown)
                        new_organism = human
                        self.human = human

                    if new_organism:
                        self.pushOrganism(new_organism)

            self.turnNumber = 1
            self.addLog("Game has been loaded")

        except Exception as e:
            self.addLog("Error while loading game.")