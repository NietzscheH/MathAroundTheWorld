import pygame as pg

class ScoreBoard(pg.sprite.Sprite):
    def __init__(self, score=0, pos=(22,57), size=24, color=(0,0,0)):
        pg.sprite.Sprite.__init__(self)
        self.score = score
        self.size = size
        self.color = color
        self.image = pg.font.SysFont('arial', self.size).render(str(self.score), True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        
    def update(self):
        self.score += 1
        self.image = pg.font.SysFont('arial', self.size).render(str(self.score), True, self.color)
