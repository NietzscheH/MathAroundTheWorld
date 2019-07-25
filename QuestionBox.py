import pygame as pg

class QuestionBox(pg.sprite.Sprite):
    def __init__(self, xcor, y_speed, screen, text='Hello', text_color=(0,0,0), bg_color=(255,255,255)):
        pg.sprite.Sprite.__init__(self)
        self.x = xcor
        self.y = 0
        self.h = 30
        self.s = y_speed
        self.txt = text
        self.win = screen
        self.screen_size = self.win.get_rect().size
        self.text_color = text_color
        self.bg_color = bg_color

        # first create an image with the message
        f = pg.font.SysFont(None, 24)
        self.image = f.render(self.txt, True, self.bg_color, self.text_color)
        # then create a rect object of that image
        self.rect = self.image.get_rect()
        self.rect.y = self.y
        self.rect.x = self.x

    def update(self):
        '''
        # create a box with message
        self.msg_image_rect.topleft = (self.x, self.y)
        # display the image in the rect object and show them on the screen
        self.win.blit(self.msg_image, self.msg_image_rect)

        self.y += self.s
        '''
        if self.rect.y < 400: #self.screen_size[1] - self.h:
            #self.y += self.s
            self.rect.y += self.s
            print(self.rect.y)
        else:
            self.kill()
