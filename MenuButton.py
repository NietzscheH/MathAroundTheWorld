import pygame as pg

class MenuButton():
    def __init__(self, text, pos=(600, 400), black=(0,0,0), white=(255,255,255)):
        self.black = black
        self.white = white
        f = pg.font.SysFont(None, 60)
        self.image = f.render(text, True, self.black)
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def __str__(self):
        return str(self.rect.center)

    def isOver(self):
        self.image = pg.font.SysFont(None, 60).render('Start', True, self.white)

    def notOver(self):
        self.image = pg.font.SysFont(None, 60).render('Start', True, self.black)
