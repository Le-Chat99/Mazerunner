from window import *
from Point import *
from Cell import *
from Maze import *

random.seed(0)

win = Window(800, 600)
num_cols = 35
num_rows = 25
m1 = Maze(50, 50, num_rows, num_cols, 20, 20,win)
m1._break_entrance_and_exit()
m1._break_walls_r(0,0)
m1._reset_cells_visited()
m1.solve()
win.wait_for_close()