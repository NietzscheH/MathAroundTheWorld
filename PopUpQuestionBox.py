import pygame as pg

class PopUpQuestionBox:
    def __init__(self, score):
        self.problems = {
            3: {'problem': 'What is the derivative of sin(x)?', 'ans': 'cos(x)'}
        }

        self.image = pg.Surface((500,500), pg.SRCALPHA)
        self.image.fill((92,167,186,100))
        self.text_image = pg.font.SysFont('arial', 24).render(self.problems[score]['problem'], True, (0,0,0))
        self.image.blit(self.text_image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (512,384)
