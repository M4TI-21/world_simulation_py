import tkinter as tk
from defines import *
from world import World
from grass import Grass

root = tk.Tk()
root.title("Mateusz Hann - 203308")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.configure(bg="black")
root.resizable(False, False)

board = tk.Canvas(root, width=WINDOW_HEIGHT, height=WINDOW_HEIGHT, bg="lightgreen", highlightthickness=0)
board.pack(side="left")

#grid
for x in range(0, WINDOW_HEIGHT, FIELD_SIZE):
  board.create_line(x, 0, x, WINDOW_HEIGHT, fill="green")
for y in range(0, WINDOW_HEIGHT, FIELD_SIZE):
  board.create_line(0, y, WINDOW_HEIGHT, y, fill="green")

game = World()

game.addNewOrganism("Grass")
game.addNewOrganism("Grass")
game.addNewOrganism("Grass")
game.addNewOrganism("Sow_thistle")
game.addNewOrganism("Guarana")
game.addNewOrganism("Guarana")
game.addNewOrganism("Guarana")
game.addNewOrganism("Belladonna")
game.addNewOrganism("Belladonna")
game.addNewOrganism("Belladonna")
game.addNewOrganism("Hogweed")
game.addNewOrganism("Hogweed")
game.addNewOrganism("Hogweed")

game.addNewOrganism("Sheep")
game.addNewOrganism("Sheep")
game.addNewOrganism("Sheep")
game.addNewOrganism("Wolf")
game.addNewOrganism("Wolf")
game.addNewOrganism("Wolf")
game.addNewOrganism("Fox")
game.addNewOrganism("Fox")
game.addNewOrganism("Fox")
game.addNewOrganism("Turtle")
game.addNewOrganism("Turtle")
game.addNewOrganism("Turtle")
game.addNewOrganism("Antelope")
game.addNewOrganism("Antelope")
game.addNewOrganism("Antelope")
game.addNewOrganism("Cybersheep")

game.drawWorld(board)

root.mainloop()