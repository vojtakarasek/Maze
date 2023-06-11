import tkinter

from mazerobot import MazeRobot
from mazerenderer import MazeRenderer
from mazedata import MazeData


class Maze:

    def __init__(self, robot: MazeRobot, renderer: MazeRenderer, data: MazeData):
        self.robot = robot
        self.renderer = renderer
        self.data = data

    def draw(self, canvas: tkinter.Canvas):
        self.renderer.clear()
        self.renderer.draw()
        self.renderer.gui()
        position = self.robot.get_position()
        left, right, top, bottom = self.renderer.get_robot_rectangle(position)
        self.robot.draw(canvas, left, top, right, bottom)

    def update(self, canvas: tkinter.Canvas):
        self.robot.update_position()
        self.draw(canvas)
        canvas.after(100, self.update, canvas)

    def on_click(self, data, canvas):
        if self.renderer.is_start_button((data.x, data.y)):
            self.update(canvas)
