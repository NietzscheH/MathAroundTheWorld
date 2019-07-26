import pygame as pg

class MenuButton():
    def __init__(self, screen, black=(0,0,0), white=(255,255,255)):
        self.black = black
        self.white = white
        f = pg.font.SysFont(None, 60)
        self.image = f.render('Start', True, self.black)
        self.rect = self.image.get_rect()
        self.win = screen
        self.rect.center = self.win.get_rect().center

    def __str__(self):
        return str(self.rect.center)

    def isOver(self):
        self.image = pg.font.SysFont(None, 60).render('Start', True, self.white)

    def notOver(self):
        self.image = pg.font.SysFont(None, 60).render('Start', True, self.black)
