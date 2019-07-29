import pygame as pg

class AnswerTypein(pg.sprite.Sprite):
    def __init__(self, text_color=(33,206,153), bg_color=(100,100,100)):
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
        self.res = None
        self.image = pg.font.SysFont('arial', 45).render(self.result, True, self.text_color)
        self.rect = pg.Rect(10, 713, 1004, 45)

        self.bg_image = pg.Surface((1004, 45))
        self.bg_image.fill(self.bg_color)
        self.bg_rect = self.bg_image.get_rect()
        self.bg_rect.topleft = (10, 713)

    def __str__(self):
        return self.result

    def update(self, k):
        self.res = None
        if k == 8 and len(self.result) != 0: # backspace key
            self.result = self.result[:-1]
        elif k == 45 and len(self.result) != 0: # minus key; prevent users type in minus if there is number typed in already
            pass
        elif k == 13: # return key (or enter key)
            self.res = self.result
            self.result = ''
        else:
            self.result += self.keys.get(k, '') # if the key is not a number, add nothing
        self.image = pg.font.SysFont('arial', 45).render(self.result, True, self.text_color)

    def submit(self):
        return self.res
