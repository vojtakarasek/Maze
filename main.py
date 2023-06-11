from tkinter import *
from mazedata import MazeData
from mazerenderer import MazeRenderer
from maze import Maze
from mazerobot import MazeRobot

root = Tk()

w = Canvas(root, width=1000, height=506)
w.pack()

data = MazeData("level3.txt")
renderer = MazeRenderer(w, data, 500 / data.get_row_count())

robot = MazeRobot((0, 0), data)

maze = Maze(robot, renderer, data)
maze.draw(w)


renderer.gui()
root.bind("<Button-1>", lambda event: maze.on_click(event, w))

mainloop()
