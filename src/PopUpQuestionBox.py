import pygame as pg
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import textwrap

class PopUpQuestionBox:
    def __init__(self, score=1):
        pg.init()
        self.score = score
        self.problems = {
            3: {'problem': 'How many intersections are there between cos(x) and sin(x) on the closed interval [0, 2π]?', 'ans': '2'},
            20: {'problem': 'What is the derivative of y = arctan(x^2)?', 'ans': '2x/(1+x^4)'},
            50: {'problem': 'What is the volume bounded by z = 2 - (x^2 + y^2)^(1/2) and z = 0 ?', 'ans': ['8π/3', '8pi/3']}
        }

        self.image = pg.Surface((500,500), pg.SRCALPHA)
        self.image.fill((92,167,186,30))

        self.wrapped_problem = textwrap.wrap(self.problems[self.score]['problem'], 38)
        for i in self.wrapped_problem:
            self.text_image = pg.font.SysFont('arial', 24).render(i, True, (0,0,0))
            self.image.blit(self.text_image, (50,50+50*self.wrapped_problem.index(i)))
        self.rect = self.image.get_rect()
        self.rect.center = (512,384)

    def draw(self):
        if self.score == 3:
            x = np.arange(0, 6.5, 0.1)
            y, z = np.sin(x), np.cos(x)

            plt.plot(x, y)
            plt.plot(x, z)
            plt.title('Blue line is sin(x)')
            plt.show()
        elif self.score == 20:
            x = np.arange(-10, 10, 0.1)
            x_sqr = np.power(x, [2 for i in x])
            y, z = np.arctan(x), np.arctan(x_sqr)

            plt.plot(x, y)
            plt.plot(x, z)
            plt.title('Blue line is arctan(x) and orange one arctan(x^2)')
            plt.show()
        elif self.score == 50:
            fig = plt.figure()
            ax = Axes3D(fig)
            X = np.arange(-3, 3, 0.1)
            Y = np.arange(-3, 3, 0.1)
            X, Y = np.meshgrid(X, Y)
            Z = 2 - np.sqrt(X ** 2 + Y ** 2)

            ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
            ax.contourf(X, Y, Z, zdir='z', offset=0, cmap=plt.get_cmap('gray'))
            ax.set_zlim(-2, 2)
            plt.title('The gray surface is z = 0')
            plt.show()

'''
test = PopUpQuestionBox(50)
test.draw()
'''