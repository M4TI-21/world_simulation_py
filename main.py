import tkinter as tk
from defines import *
from world import World

root = tk.Tk()
root.title("Mateusz Hann - 203308")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.configure(bg="black")
root.resizable(False, False)

board = tk.Canvas(root, width=WINDOW_HEIGHT, height=WINDOW_HEIGHT, bg="lightgreen", highlightthickness=0)
board.pack(side="left")

log_console = tk.Text(root, width=40, height=40, bg="black", fg="white", state="disabled")
log_console.pack(side="right", fill="y")

#grid
def drawGrid():
  for x in range(0, WINDOW_HEIGHT, FIELD_SIZE):
    board.create_line(x, 0, x, WINDOW_HEIGHT, fill="green")
  for y in range(0, WINDOW_HEIGHT, FIELD_SIZE):
    board.create_line(0, y, WINDOW_HEIGHT, y, fill="green")

game = World(log_console=log_console)

game.addNewOrganism("Hogweed")
game.addNewOrganism("Hogweed")
game.addNewOrganism("Hogweed")

game.addNewOrganism("Cybersheep")

game.addNewOrganism("Human")

game.drawWorld(board)
drawGrid()

# key press defines
organism_types = {
  "1": "Wolf", 
  "2": "Sheep", 
  "3": "Fox", 
  "4": "Turtle", 
  "5": "Antelope", 
  "q": "Cybersheep",
  "6": "Grass", 
  "7": "Sow thistle", 
  "8": "Guarana", 
  "9": "Belladonna", 
  "0": "Hogweed"
}

def addOrgOnClick(e):
  x = e.x // FIELD_SIZE
  y = e.y // FIELD_SIZE
  game.addOrganismOnClick(x, y, board)

root.bind("<Button-1>", addOrgOnClick)

def humanMovement(e):
  key = e.keysym

  if key in organism_types:
    game.selectOrganism(organism_types[key])
  elif key == "space" and (not game.human or not game.human.isAlive or game.hasHumanMoved()):
    game.makeTurn(board)
    board.delete("all")
    game.drawWorld(board)
  elif key == "a":
    game.handleSpecialAbility("a")
    game.drawWorld(board)
  elif key == "s":
     game.saveGame()
  elif key == "l":
     game.loadGame()
     board.delete("all")
     game.drawWorld(board)

  elif key == "Up":
      game.handleHumanMovement("UP", board)
  elif key == "Down":
      game.handleHumanMovement("DOWN", board)
  elif key == "Left":
      game.handleHumanMovement("LEFT", board)
  elif key == "Right":
      game.handleHumanMovement("RIGHT", board)
  drawGrid()

root.bind("<Key>", humanMovement)

root.mainloop()