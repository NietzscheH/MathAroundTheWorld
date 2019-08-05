import pygame as pg
import numpy as np
import matplotlib.pyplot as plt

class PopUpQuestionBox:
    def __init__(self, score=1):
        pg.init()
        self.score = score
        self.problems = {
            1: {'problem': 'How many intersections are there between cos(x) and sin(x) on the closed interval [0, 2π]?', 'ans': '2'},
            15: {'problem': ''}
        }

        self.image = pg.Surface((500,500), pg.SRCALPHA)
        self.image.fill((92,167,186,30))
        self.text_image = pg.font.SysFont('arial', 24).render(self.problems[self.score]['problem'], True, (0,0,0))
        self.image.blit(self.text_image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (512,384)

    def draw(self):
        if self.score == 1:
            x = np.arange(0, 6.5, 0.1)
            y, z = np.sin(x), np.cos(x)

            plt.plot(x, y)
            plt.plot(x, z)
            plt.title('Blue line is sin(x)')
            plt.show()

'''
test = PopUpQuestionBox()
test.draw()
'''