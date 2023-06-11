import tkinter
from mazedata import MazeData


class MazeRenderer:
    def __init__(self, w: tkinter.Canvas, data: MazeData, row_size: int):
        self.w = w
        self.data = data
        self.row_size = row_size

    def clear(self):
        self.w.delete(tkinter.ALL)

    def draw(self):

        (walls_rows, walls_columns, doors_x, doors_y) = self.data.wall()

        a = 5
        b = 5
        for i in walls_rows:
            x = i[0]
            y = i[1]
            self.w.create_line(a + y * self.row_size, b + x * self.row_size, a + y * self.row_size,
                               b + x * self.row_size + self.row_size, width=5)

        for i in walls_columns:
            x = i[0]
            y = i[1]
            self.w.create_line(a + y * self.row_size, b + x * self.row_size, a + y * self.row_size + self.row_size,
                               b + x * self.row_size, width=5)

        for i in doors_x:
            x = i[0]
            y = i[1]
            self.w.create_line(a + y * self.row_size, b + x * self.row_size, a + y * self.row_size,
                               b + x * self.row_size + self.row_size, width=5,
                               fill="red")
        for i in doors_y:
            x = i[0]
            y = i[1]
            self.w.create_line(a + y * self.row_size, b + x * self.row_size, a + y * self.row_size + self.row_size,
                               b + x * self.row_size, width=5, fill="red")

    def get_robot_rectangle(self, position: (int, int)) -> (int, int, int, int):  # left, top, right, bottom
        return position[0] * self.row_size + 5, position[1] * self.row_size + 5, \
               (position[0] + 1) * self.row_size + 5, (position[1] + 1) * self.row_size + 5

    def gui(self):
        self.w.create_rectangle(508, 5, 1000, 506, fill="grey", width=3)

        self.w.create_rectangle(616, 43, 916, 83, fill="light grey", activefill="dark grey")
        self.w.create_text(766, 63, text="Level", font=('Helvetica 14'), state="disabled")

        self.w.create_rectangle(616, 169, 916, 209, fill="light grey", activefill="dark grey")
        self.w.create_text(766, 189, text="Load from file", font=('Helvetica 14'), state="disabled")

        self.w.create_rectangle(616, 295, 916, 335, fill="light grey", activefill="dark grey")
        self.w.create_text(766, 315, text="Robot placement", font=('Helvetica 14 '), state="disabled")

        self.w.create_rectangle(616, 400, 916, 460, fill="light green", activefill="light blue")
        self.w.create_text(766, 430, text="Start!", fill="green", font=('Helvetica 25 bold'), state="disabled")

    def is_start_button(self, position: (int, int)):
        return 616 < position[0] < 916 and 400 < position[1] < 460