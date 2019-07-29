import pygame as pg

class MenuButton:
    def __init__(self, text, pos, size=60, defualt_color=(0,0,0), hover_color=(255,255,255)):
        self.defualt_color = defualt_color
        self.hover_color = hover_color
        self.text = text
        f = pg.font.SysFont(None, size)
        self.image = f.render(self.text, True, self.defualt_color)
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def __str__(self):
        return str(self.rect.center)

    def isOver(self):
        self.image = pg.font.SysFont(None, 60).render(self.text, True, self.hover_color)

    def notOver(self):
        self.image = pg.font.SysFont(None, 60).render(self.text, True, self.defualt_color)
