import pygame as pg
from os import path

class MenuButton_:
    def __init__(self, pos, default_pic, hover_pic):
        self.base_path = path.dirname(__file__)
        self.default_pic_path = path.join(self.base_path, 'assets', 'Buttons', default_pic)
        self.hover_pic_path = path.join(self.base_path, 'assets', 'Buttons', hover_pic)

        self.pos = pos
        self.image = pg.image.load(self.default_pic_path)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def __str__(self):
        return str(self.rect.center)

    def isOver(self):
        self.image = pg.image.load(self.hover_pic_path)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def notOver(self):
        self.image = pg.image.load(self.default_pic_path)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
