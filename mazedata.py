class MazeData:

    def __init__(self, file_name):
        with open(file_name, "r") as input:
            file_content = input.read()
            self.data = eval(file_content)

    def wall(self) -> ([(int, int)], [(int, int)], [(int, int)]):
        walls_rows = []
        walls_columns = []
        doors_x = []
        doors_y = []
        wall_x = 0

        for _ in self.data[0]:
            wall_y = 0
            for i in self.data[0][wall_x]:
                if i == 1:
                    walls_rows.append((wall_x, wall_y))
                elif i == 2:
                    doors_x.append((wall_x, wall_y))

                wall_y += 1
            wall_x += 1

        wall_y = 0
        for _ in self.data[1]:
            wall_x = 0
            for i in self.data[1][wall_y]:
                if i == 1:
                    walls_columns.append((wall_x, wall_y))
                elif i == 2:
                    doors_y.append((wall_x, wall_y))

                wall_x += 1
            wall_y += 1
        # print(walls_rows, walls_columns, doors_x, doors_y)
        return walls_rows, walls_columns, doors_x, doors_y

    def is_wall(self, r_pos):
        r_pos_x = r_pos[0]
        r_pos_y = r_pos[1]
        left = False
        right = False
        top = False
        bottom = False
        door_l = False
        door_r = False
        door_t = False
        door_b = False
        if self.data[0][r_pos_y][r_pos_x] == 1:
            left = True
        elif self.data[0][r_pos_y][r_pos_x] == 2:
            door_l = True

        if self.data[0][r_pos_y][r_pos_x + 1] == 1:
            right = True
        elif self.data[0][r_pos_y][r_pos_x + 1] == 2:
            door_r = True

        if self.data[1][r_pos_x][r_pos_y] == 1:
            top = True
        elif self.data[1][r_pos_x][r_pos_y] == 2:
            door_t = True

        if self.data[1][r_pos_x][r_pos_y + 1] == 1:
            bottom = True
        elif self.data[1][r_pos_x][r_pos_y + 1] == 2:
            door_b = True
        # print(left, right, top, bottom,",",door_l, door_r, door_t, door_b)
        return left, right, top, bottom, door_l, door_r, door_t, door_b

    def get_row_count(self):
        return len(self.data[1])
