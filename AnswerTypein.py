import pygame as pg

class AnswerTypein(pg.sprite.Sprite):
    def __init__(self, text_color=(33,206,153), bg_color=(214,213,183,100)):
        pg.sprite.Sprite.__init__(self)
        self.text_color = text_color
        self.bg_color = bg_color
        self.keys = {
            pg.K_MINUS: '-',
            pg.K_PERIOD: '.',
            pg.K_0: '0',
            pg.K_1: '1',
            pg.K_2: '2',
            pg.K_3: '3',
            pg.K_4: '4',
            pg.K_5: '5',
            pg.K_6: '6',
            pg.K_7: '7',
            pg.K_8: '8',
            pg.K_9: '9',
        }
        self.result = ''
        self.res = None
        self.image = pg.font.SysFont('arial', 45).render(self.result, True, self.text_color)
        self.rect = pg.Rect(10, 713, 1004, 45)

        self.bg_image = pg.Surface((1004, 45), pg.SRCALPHA) # without pg.SCRALPHA, the surface does not accept transparency
        self.bg_image.fill(self.bg_color)
        self.bg_rect = self.bg_image.get_rect()
        self.bg_rect.topleft = (10, 713)

    def __str__(self):
        '''
            Stringification of AnswerTypein object
            args: none
            return: ('str') the input typed by the user
        '''
        return self.result

    def update(self, k):
        '''
            Updates the Typein field with user input
            args: Pygame keyboard constant
            return: none
        '''
        self.res = None
        if k == pg.K_BACKSPACE and len(self.result) != 0: # backspace key
            self.result = self.result[:-1]
        elif k == pg.K_MINUS and len(self.result) != 0: # minus key; prevent users type in minus if there is number typed in already
            pass
        elif k == pg.K_RETURN: # return key (or enter key)
            self.res = self.result
            self.result = ''
        else:
            self.result += self.keys.get(k, '') # if the key is not a number, add nothing
        self.image = pg.font.SysFont('arial', 45).render(self.result, True, self.text_color)

    def submit(self):
        '''
            Returns the user's answer after the enter key has been pressed
            args: none
            return: ('str') the answer entered by the user
        '''
        return self.res
