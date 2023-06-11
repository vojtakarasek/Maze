import tkinter

from mazedata import MazeData


class MazeRobot:
    def __init__(self):
        # direction
        self.delta_x = 1
        self.delta_y = 0
        # position
        self.position_x = 1
        self.position_y = 1

    def update_position(self, data: MazeData):
        self.position_x += self.delta_x
        self.position_y += self.delta_y

    def get_position(self) -> (int, int):
        return self.position_x, self.position_y

    def draw(self, canvas: tkinter.Canvas, left: int, right: int, top: int, bottom: int):
        canvas.create_rectangle(left, top, right, bottom)
