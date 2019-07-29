import pygame as pg

class QuestionBox(pg.sprite.Sprite):
    def __init__(self, xcor, y_speed, text='Hello', ans='0', text_color=(0,0,0), bg_color=(255,255,255)):
        pg.sprite.Sprite.__init__(self)
        self.xcor = xcor
        self.ycor = -36
        self.height = 36
        self.speed = y_speed
        self.txt =text
        self.text_color, self.bg_color = text_color, bg_color
        self.answer = ans

        # first create an image with the message
        self.f = pg.font.SysFont(None, self.height)
        self.image = self.f.render(self.txt, True, self.text_color, self.bg_color)
        # then create a rect object of that image
        self.rect = self.image.get_rect()
        self.rect.y = self.ycor
        self.rect.x = self.xcor

    def __str__(self):
        return self.txt

    def update(self):
        self.ycor += self.speed
        self.rect.y = self.ycor
        self.image = self.f.render(self.txt, True, self.text_color, self.bg_color) # create an image again to change the background color of the bottom most one
        #print(self.y, self.rect.y)
