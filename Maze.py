from Cell import *
from window import *
import time
import random


class Maze:
    def __init__(
            self, 
            x1, 
            y1, 
            num_rows, 
            num_cols, 
            cell_size_x, 
            cell_size_y,
            win
            ):
        self.x1=x1
        self.y1=y1
        self.num_rows=num_rows
        self.num_cols=num_cols
        self.cell_size_x=cell_size_x
        self.cell_size_y=cell_size_y
        self.win=win
        self._create_cells()
    def _create_cells(self):
        self._cells=[]
        for i in range(self.num_cols):
            rows=[]
            for j in range(self.num_rows):
                x1=self.x1+(self.cell_size_x*i)
                x2=x1+self.cell_size_x
                y1=self.y1+(self.cell_size_y*j)
                y2=y1+self.cell_size_y
                C=Cell(x1,x2,y1,y2,self.win)
                rows.append(C)
            self._cells.append(rows)
                
    def _draw_cell(self,i,j):
        cell = self._cells[i][j]
        cell.Draw("black")
        self._animate()
    def _animate(self):
        self.win.redraw()
        time.sleep(0.00001)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall=False
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall=False
    def _break_walls_r(self,i,j):
        self._cells[i][j].visited=True
        while True:
            potential_neighbors = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
            valid_neighbors = []
            for ni, nj in potential_neighbors:
                if 0 <= ni < len(self._cells) and 0 <= nj < len(self._cells[0]):
                    if not self._cells[ni][nj].visited:
                        valid_neighbors.append([ni, nj])
        

            if not valid_neighbors:
                self._draw_cell(i, j)
                return
            
            D = random.choice(valid_neighbors)
            
            if D==[i+1,j]:
                self._cells[i][j].has_right_wall=False
                self._cells[i+1][j].has_left_wall=False
            if D==[i-1,j]:
                self._cells[i-1][j].has_right_wall=False
                self._cells[i][j].has_left_wall=False
            if D==[i,j+1]:
                self._cells[i][j].has_bottom_wall=False
                self._cells[i][j+1].has_top_wall=False
            if D==[i,j-1]:
                self._cells[i][j-1].has_bottom_wall=False
                self._cells[i][j].has_top_wall=False
            self._break_walls_r(D[0],D[1])

                    
            
