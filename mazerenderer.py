import tkinter
from tkinter import *
from mazedata import MazeData


class MazeRenderer:
    def __init__(self, w: tkinter.Canvas, data: MazeData, row_size: int):
        self.w = w
        self.data = data
        self.row_size = row_size

    def draw(self):

        (walls_rows, walls_columns, doors) = self.data.wall()

        a = 5
        b = 5
        for i in walls_rows:
            x = i[0]
            y = i[1]
            self.w.create_line(a + y * self.row_size, b + x * self.row_size, a + y * self.row_size, b + x * self.row_size + self.row_size, fill="red")

        for i in walls_columns:
            x = i[0]
            y = i[1]
            self.w.create_line(a + y * self.row_size, b + x * self.row_size, a + y * self.row_size + 55, b + x * self.row_size, fill="red")

        for i in doors:
            x = i[0]
            y = i[1]
            if len(doors) == 3:
                self.w.create_line(a + y * self.row_size, b + x * self.row_size, a + y * self.row_size, b + x * self.row_size + self.row_size,
                              fill="green")
            else:
                self.w.create_line(a + y * self.row_size, b + x * self.row_size, a + y * self.row_size + 55, b + x * self.row_size, fill="green")
