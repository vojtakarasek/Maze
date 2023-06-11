import tkinter

from mazedata import MazeData


class MazeRobot:
    def __init__(self):
        # direction
        self.delta_x = 1
        self.delta_y = 0
        # position
        self.position_x = 0
        self.position_y = 0

    def update_position(self, data: MazeData):
        self.data = data
        left, right, top, bottom, door_l, door_r, door_t, door_b = self.data.is_wall((self.position_x, self.position_y))
        if door_l or door_r or door_t or door_b:
            if door_l is True:
                self.delta_x = -1
                self.delta_y = 0
            if door_r is True:
                self.delta_x = 1
                self.delta_y = 0
            if door_t is True:
                self.delta_x = 0
                self.delta_y = -1
            if door_b is True:
                self.delta_x = 0
                self.delta_y = 1
            return

        if self.delta_x == 1 and self.delta_y == 0 and right is False:
            self.position_x += self.delta_x
            self.position_y += self.delta_y
        if self.delta_x == 0 and self.delta_y == 1 and bottom is False:
            self.position_x += self.delta_x
            self.position_y += self.delta_y
        if self.delta_x == -1 and self.delta_y == 0 and left is False:
            self.position_x += self.delta_x
            self.position_y += self.delta_y
        if self.delta_x == 0 and self.delta_y == -1 and top is False:
            self.position_x += self.delta_x
            self.position_y += self.delta_y

        if self.delta_x == 1 and self.delta_y == 0 and right is True:
            self.delta_x = 0
            self.delta_y = 1
        if self.delta_x == 0 and self.delta_y == 1 and bottom is True:
            self.delta_x = -1
            self.delta_y = 0
        if self.delta_x == -1 and self.delta_y == 0 and left is True:
            self.delta_x = 0
            self.delta_y = -1
        if self.delta_x == 0 and self.delta_y == -1 and top is True:
            self.delta_x = 1
            self.delta_y = 0


    def get_position(self) -> (int, int):
        return self.position_x, self.position_y

    def draw(self, canvas: tkinter.Canvas, left: int, right: int, top: int, bottom: int):
        canvas.create_rectangle(left, top, right, bottom, fill="light blue")
