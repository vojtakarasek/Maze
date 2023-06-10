class MazeData:

    def __init__(self, file_name):
        with open(file_name, "r") as input:
            file_content = input.read()
            self.data = eval(file_content)

    # def row_column_number(self):
    # global rows_number
    # rows_number = len(self.data[1])
    # global columns_number
    # columns_number = len(self.data[0])

    def wall(self) -> ([(int, int)], [(int, int)], [(int, int)]):
        walls_rows = []
        walls_columns = []
        doors = []
        wall_x = 0

        for _ in self.data[0]:
            wall_y = 0
            for i in self.data[0][wall_x]:
                if i == 1:
                    walls_rows.append((wall_x, wall_y))
                elif i == 2:
                    doors.append((wall_x, wall_y))

                wall_y += 1
            wall_x += 1

        wall_y = 0
        for _ in self.data[1]:
            wall_x = 0
            for i in self.data[1][wall_y]:
                if i == 1:
                    walls_columns.append((wall_x, wall_y))
                elif i == 2:
                    doors.append((wall_x, wall_y))

                wall_x += 1
            wall_y += 1
        print(walls_rows, walls_columns, doors)
        return walls_rows, walls_columns, doors

    # def is_wall(self, row, column, direction): bool  #direction l,t,r,b
    # first_array_idx = 0
    # if (direction in ['t', 'b']):
    # first_array_idx = 1
    # return data[first_array_idx][]
