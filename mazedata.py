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
        #print(walls_rows, walls_columns, doors_x, doors_y)
        return walls_rows, walls_columns, doors_x, doors_y

    def is_wall(self):
        r_pos = (0,0)
        r_pos_a = r_pos[0]
        r_pos_b = r_pos[1]
        left = False
        right = False
        top = False
        bottom = False

        if (r_pos_a, r_pos_b) in walls_rows:
            left = True
        if (r_pos_a, r_pos_b) in walls_columns:
            top = True
        if (r_pos_a + 1, r_pos_b) in walls_rows:
            right = True
        if (r_pos_a, r_pos_b + 1) in walls_columns:
            bottom = True

        return left, right, top, bottom

