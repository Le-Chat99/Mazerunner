from window import *
from Point import *
from Cell import *
from Maze import *


win = Window(800, 600)

num_cols = 12
num_rows = 10
m1 = Maze(50, 50, num_rows, num_cols, 25, 25,win)
m1._break_entrance_and_exit()
win.wait_for_close()