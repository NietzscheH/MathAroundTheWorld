import pygame as pg

class AnswerTypein(pg.sprite.Sprite):
    def __init__(self, text_color=(33,206,153), bg_color=(255,255,255)):
        pg.sprite.Sprite.__init__(self)
        self.text_color = text_color
        self.bg_color = bg_color
        self.keys = {
            45: '-',
            46: '.',
            48: '0',
            49: '1',
            50: '2',
            51: '3',
            52: '4',
            53: '5',
            54: '6',
            55: '7',
            56: '8',
            57: '9',
        }
        self.result = ''
        self.image = pg.font.SysFont('arial', 45).render(self.result, True, self.text_color)
        self.rect = pg.Rect(10, 745, 1180, 45)

    def __str__(self):
        return self.result

    def update(self, k):
        if k == 8 and len(self.result) != 0:
            self.result = self.result[:-1]
        elif k == 45 and len(self.result) != 0:
            pass
        else:
            self.result += self.keys.get(k, '')
        self.image = pg.font.SysFont('arial', 45).render(self.result, True, self.text_color)
