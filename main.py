import makeMaze
import Pathfinder
from PIL import Image
from Grid import Grid


Input = "maze.png"
Output = "output.png"



maze = makeMaze.make(Input)
#lines = file.readlines()
#aze = []

#for i in lines:
#    maze.append([])
#    for j in i.strip():
#        maze[-1].append(j)

grid = Grid(len(maze), len(maze[0]))

grid.grid = maze

path = Pathfinder.aStar(grid.grid, grid.find("x"), grid.find("o"), "#")

img = Image.open("maze.png")
for i in path:
    img.putpixel((i[1], i[0]), (0, 255, 0))
img.save(Output)