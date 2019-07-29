import pygame as pg
import os

class HealthIcon(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.health = 3

        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, 'assets', 'heart_1.png')
        self.heart = pg.image.load(file_path)
        self.heart = pg.transform.scale(self.heart, (32, 32))

        self.image = pg.Surface((96, 32))
        self.image.fill((255,255,255))
        for i in range(self.health):
            self.image.blit(self.heart, (i*32,0))

        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 10)

    def update(self):
        self.health -= 1
        self.image = pg.Surface((96, 32))
        self.image.fill((255,255,255))
        for i in range(self.health):
            self.image.blit(self.heart, (i*32,0))
