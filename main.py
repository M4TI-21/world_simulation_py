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
game = World()

game.addNewOrganism("Grass")
game.addNewOrganism("Grass")
game.addNewOrganism("Grass")

game.drawWorld(board)

root.mainloop()
