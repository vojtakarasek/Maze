from tkinter import *

hlavni = Tk()

w = Canvas(hlavni, width=506, height=506)
w.pack()

# creating table 10x10
a = 5
b = 5
for x in range(11):
    w.create_line(5, a, 505, b)
    a += 50
    b += 50
a = 5
b = 5
for x in range(11):
    w.create_line(a, 5, b, 505)
    a += 50
    b += 50


class MazeData:

    def __init__(self, file_name):
        with open(file_name, "r") as input:
            file_content = input.read()
            self.data = eval(file_content)

    def wall(self):
        walls = []
        doors = []
        wall_x = 0
        wall_y = 0

        for _ in self.data[0]:
            for i in self.data[0][wall_x]:
                if i == 1:
                    walls.append((wall_x, wall_y))  
                elif i == 2:
                    doors.append((wall_x, wall_y))
                
                if wall_y < len(self.data[0]):
                    wall_y += 1
                else:
                    pass    
            wall_x += 1

        for _ in self.data[1]:
            for i in self.data[1][wall_y]:
                if i == 1:
                    walls.append((wall_x, wall_y))
                elif i == 2:
                    doors.append((wall_x, wall_y))
                
                if wall_x < len(self.data[1]):
                    wall_x += 1
                else:
                    pass
            if wall_y < len(self.data[1]):
                wall_y += 1
            else:
                pass  
        print(walls, doors)



    #def is_wall(self, row, column, direction): bool  #direction l,t,r,b
        #first_array_idx = 0
        #if (direction in ['t', 'b']):
            #first_array_idx = 1
        #return data[first_array_idx][]

#class Render:
    #def __init__(self):
        #pass

    #def draw(self)
        


# class Robot:


# class Transformator:

data = MazeData("cisla.txt").wall()
mainloop()