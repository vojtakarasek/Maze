import tkinter
from mazedata import MazeData


class MazeRobot:
    def __init__(self, position: (int, int), data: MazeData):
        self.data = data
        # direction
        self.delta_x = 1
        self.delta_y = 0
        # position
        self.position = position
        self.visited = {(self.position[0], self.position[1])}
        self.rotation_number = 0

    def step(self):
        self.position = (self.position[0] + self.delta_x, self.position[1] + self.delta_y)
        self.rotation_number = 0

    def more_than_one_way(self):
        left, right, top, bottom, door_l, door_r, door_t, door_b = self.data.is_wall(
            (self.position[0], self.position[1]))
        if (not right and not left) or (not right and not top) or (not right and not bottom) or (
                not left and not top) or (not left and not bottom) or (
                not top and not bottom):
            return True

    def already_visited(self):
        if (self.position[0] + self.delta_x, self.position[1] + self.delta_y) in self.visited:
            return True

    def wall_ahead(self):
        left, right, top, bottom, door_l, door_r, door_t, door_b = self.data.is_wall(
            (self.position[0], self.position[1]))
        if self.delta_x == 1 and right:
            return True
        elif self.delta_x == -1 and left:
            return True
        elif self.delta_y == 1 and bottom:
            return True
        elif self.delta_y == -1 and top:
            return True

    def rotate(self):
        if self.delta_x == 1:
            self.delta_x = 0
            self.delta_y = 1
        elif self.delta_y == 1:
            self.delta_x = -1
            self.delta_y = 0
        elif self.delta_x == -1:
            self.delta_x = 0
            self.delta_y = -1
        elif self.delta_y == -1:
            self.delta_x = 1
            self.delta_y = 0
        self.rotation_number += 1

    def update_position(self):
        left, right, top, bottom, door_l, door_r, door_t, door_b = self.data.is_wall(self.position)
        self.visited.add(self.position)

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
        # movement
        if self.rotation_number == 5 and not self.wall_ahead():
            self.step()

        if self.rotation_number == 8 and not self.wall_ahead():
            self.step()

        elif not self.wall_ahead() and not (self.already_visited() and self.more_than_one_way()):
            self.step()
        # rotation
        if self.more_than_one_way() and self.already_visited():
            self.rotate()

        elif self.wall_ahead():
            self.rotate()

    def get_position(self) -> (int, int):
        return self.position

    def draw(self, canvas: tkinter.Canvas, left: int, right: int, top: int, bottom: int):
        canvas.create_rectangle(left, top, right, bottom, fill="light blue")
        row_size = bottom - top
        if self.delta_x == 1:  # right
            canvas.create_rectangle(left + (row_size / 2), top, right, bottom, fill="blue")
        if self.delta_x == -1:  # left
            canvas.create_rectangle(left, top, right - (row_size / 2), bottom, fill="blue")
        if self.delta_y == 1:  # bot
            canvas.create_rectangle(left, top + (row_size / 2), right, bottom, fill="blue")
        if self.delta_y == -1:  # top
            canvas.create_rectangle(left, top, right, bottom - (row_size / 2), fill="blue")
