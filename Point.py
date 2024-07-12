from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

class Line:
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2
    def draw(self, Canvas, fill_color):
        x1=self.p1.x
        y1=self.p1.y
        x2=self.p2.x
        y2=self.p2.y
        Canvas.create_line(x1,y1,x2,y2, fill=fill_color,width=2)
