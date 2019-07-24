import pygame as pg

class QuestionBox:
    def __init__(self, xcor, y_speed, scre, width=30, height=20, color=(0,0,0)):
        self.x = xcor
        self.y = -height
        self.s = y_speed
        self.w = width
        self.h = height
        self.win = scre
        self.color = color
    
    def drawMyself(self):
        pg.draw.rect(self.win, self.color, (self.x, self.y, self.w, self.h))
        self.y += self.s
