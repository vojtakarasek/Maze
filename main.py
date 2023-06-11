from tkinter import *
from mazedata import MazeData
from mazerenderer import MazeRenderer
from maze import Maze
from mazerobot import MazeRobot

main_tk = Tk()

w = Canvas(main_tk, width=1000, height=506)
w.pack()
row_size = 50


data = MazeData("level3.txt")
renderer = MazeRenderer(w, data, row_size)
renderer.gui()
robot = MazeRobot((0,0), row_size, data)

maze = Maze(robot, renderer, data)
maze.draw(w)
w.after(200, maze.update, w)



mainloop()
