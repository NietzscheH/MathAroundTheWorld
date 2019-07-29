import pygame as pg

class ScoreBoard(pg.sprite.Sprite):
    def __init__(self, pos=(10,45), size=24, color=(0,0,0)):
        pg.sprite.Sprite.__init__(self)
        self.score = 0
        self.size = size
        self.color = color
        self.image = pg.font.SysFont('arial', self.size).render(str(self.score), True, self.color, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        
    def update(self):
        self.score += 1
        self.image = pg.font.SysFont('arial', self.size).render(str(self.score), True, self.color, (255, 255, 255))
