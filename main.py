from tkinter import *

hlavni = Tk()

w = Canvas(hlavni, width=506, height=506)
w.pack()

#creating table 10x10
a = 5
b = 5
for x in range(11):
    w.create_line(5,a,505,b)
    a += 50
    b += 50
a = 5
b = 5
for x in range(11):
    w.create_line(a,5,b,505)
    a += 50
    b += 50

class Maze:
    def __init__(self):
        pass
 
    def walls(self, canvas):
        b = open("cisla.txt", "r")


    #def is_wall(x, y, direction): bool



#class Robot:


#class Transformator:

mainloop()
