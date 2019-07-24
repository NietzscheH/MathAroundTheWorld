import pygame as pg

class QuestionBox:
    def __init__(self, xcor, y_speed, scre, text='Hello', text_color=(0,0,0), bg_color=(255,255,255)):
        self.x = xcor
        self.y = None
        self.h = None
        self.s = y_speed
        self.txt = text
        self.win = scre
        self.screen_size = self.win.get_rect().size
        self.text_color = text_color
        self.bg_color = bg_color

        # first create an image with the message
        f = pg.font.SysFont(None, 24)
        self.msg_image = f.render(self.txt, True, self.bg_color, self.text_color)
        # then create a rect object of that image
        self.msg_image_rect = self.msg_image.get_rect()
        self.h = self.msg_image_rect.size[1]
        self.y = -self.h

    def _drawMyself_(self):
        # draw a plain black box
        pg.draw.rect(self.win, self.color, (self.x, self.y, self.w, self.h))
        self.y += self.s

    def drawMyself(self):
        # create a box with message
        self.msg_image_rect.topleft = (self.x, self.y)
        # display the image in the rect object and show them on the screen
        self.win.blit(self.msg_image, self.msg_image_rect)

        self.y += self.s
