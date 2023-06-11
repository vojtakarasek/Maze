from tkinter import *
from mazedata import MazeData
from mazerenderer import MazeRenderer
from maze import Maze

from mazerobot import MazeRobot

main_tk = Tk()

w = Canvas(main_tk, width=1000, height=506)
w.pack()
rows_number = 0
columns_number = 0
row_size = 125

def draw_grid():
    # creating table
    coordinate_a = 5
    coordinate_b = 5

    for x in range(11):
        w.create_line(5, coordinate_a, 505, coordinate_b)
        coordinate_a += row_size
        coordinate_b += row_size
    coordinate_a = 5
    coordinate_b = 5
    for x in range(11):
        w.create_line(coordinate_a, 5, coordinate_b, 505)
        coordinate_a += row_size
        coordinate_b += row_size


# class Robot:

data = MazeData("level1.txt")
renderer = MazeRenderer(w, data, row_size)
renderer.gui()
robot = MazeRobot()

maze = Maze(robot, renderer, data)
maze.update(w)  # inside is replanned to update again after 1 sec


mainloop()
