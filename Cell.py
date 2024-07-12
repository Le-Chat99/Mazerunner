from Point import *


class Cell:
    def __init__(self, x1,x2,y1,y2,win, left= True,right=True,top=True,bottom=True):
        self.has_left_wall=left
        self.has_right_wall=right
        self.has_top_wall=top
        self.has_bottom_wall=bottom
        self._x1=x1
        self._x2=x2
        self._y1=y1
        self._y2=y2
        self._win=win
        self.visited=False

    def Draw(self, fill_color):
        if self.has_left_wall:
            p1=Point(self._x1, self._y1)
            p2=Point(self._x1, self._y2)
            Line(p1,p2).draw(self._win.canvas, fill_color)
        else:
            p1=Point(self._x1, self._y1)
            p2=Point(self._x1, self._y2)
            Line(p1,p2).draw(self._win.canvas, "white")
        
        if self.has_right_wall:
            p1=Point(self._x2, self._y1)
            p2=Point(self._x2, self._y2)
            Line(p1,p2).draw(self._win.canvas, fill_color)
        else:
            p1=Point(self._x2, self._y1)
            p2=Point(self._x2, self._y2)
            Line(p1,p2).draw(self._win.canvas, "white")
        
        if self.has_top_wall:
            p1=Point(self._x1, self._y1)
            p2=Point(self._x2, self._y1)
            Line(p1,p2).draw(self._win.canvas, fill_color)
        else:
            p1=Point(self._x1, self._y1)
            p2=Point(self._x2, self._y1)
            Line(p1,p2).draw(self._win.canvas, "white")
        
        if self.has_bottom_wall:
            p1=Point(self._x1, self._y2)
            p2=Point(self._x2, self._y2)
            Line(p1,p2).draw(self._win.canvas, fill_color)
        else:
            p1=Point(self._x1, self._y2)
            p2=Point(self._x2, self._y2)
            Line(p1,p2).draw(self._win.canvas, "white")
    def draw_move(self, to_cell, undo=False):
        if undo:
            fill_color="gray"
        else:
            fill_color="red"
        x1= (self._x1 + self._x2)/2
        y1= (self._y1 + self._y2)/2
        x2= (to_cell._x1 + to_cell._x2)/2
        y2= (to_cell._y1 + to_cell._y2)/2
        p1=Point(x1,y1)
        p2=Point(x2,y2)
        Line(p1,p2).draw(self._win.canvas,fill_color)