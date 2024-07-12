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
        time.sleep(0.0001)
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
    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited=False    
    def solve(self):
        return self._solve_r(0,0)
    def _solve_r(self,i,j):
        self._animate()
        self._cells[i][j].visited=True
        if i==len(self._cells)-1 and j==len(self._cells[0])-1:
            return True
        potential_neighbors = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
        for ni,nj in potential_neighbors:
            if self._can_move(i,j,ni,nj):
                self._draw_move(i, j, ni, nj)
                if self._solve_r(ni, nj):
                    return True
                self._draw_undo_move(i, j, ni, nj)
        return False
    def _draw_move(self,i,j,ni,nj):
        x1=self.x1+(self.cell_size_x*(i+1/2))
        y1=self.y1+(self.cell_size_y*(j+1/2))
        x2=self.x1+(self.cell_size_x*(ni+1/2))
        y2=self.y1+(self.cell_size_y*(nj+1/2))
        p1=Point(x1,y1)
        p2=Point(x2,y2)
        Line(p1,p2).draw(self.win.canvas, "blue")
    def _draw_undo_move(self,i,j,ni,nj):
        x1=self.x1+(self.cell_size_x*(i+1/2))
        y1=self.y1+(self.cell_size_y*(j+1/2))
        x2=self.x1+(self.cell_size_x*(ni+1/2))
        y2=self.y1+(self.cell_size_y*(nj+1/2))
        p1=Point(x1,y1)
        p2=Point(x2,y2)
        Line(p1,p2).draw(self.win.canvas, "white")

    def _can_move(self,i,j,ni,nj):
        if ni > len(self._cells)-1 or nj > len(self._cells[0])-1:
            return False

        if self._cells[ni][nj].visited:
            return False
        if self._cells[i][j].has_bottom_wall and nj-j==1:
            return False
        if self._cells[i][j].has_top_wall and j-nj==1:
            return False
        if self._cells[i][j].has_right_wall and ni-i==1:
            return False
        if self._cells[i][j].has_left_wall and i-ni==1:
            return False 
        return True