import pygame as pg
import os

class QuestionBox(pg.sprite.Sprite):
    def __init__(self, xcor, y_speed, text='Hello', ans='0', text_color=(0,0,0), bg_color=(255,255,255), filename='moon_1.png'):
        pg.sprite.Sprite.__init__(self)
        self.xcor = xcor
        self.ycor = -24
        self.height = 24
        self.speed = y_speed
        self.txt = text
        self.text_color, self.bg_color = text_color, bg_color
        self.answer = ans

        self.filename = filename
        self.base_path = os.path.dirname(__file__)
        self.file_path = os.path.join(self.base_path, 'assets', self.filename)

        # first create an image with the message
        self.f = pg.font.SysFont('arial', self.height)
        self.text_image = self.f.render(self.txt, True, self.text_color)
        self.text_rect = self.text_image.get_rect()

        # background image for question box
        self.image = pg.image.load(self.file_path)
        self.image = pg.transform.scale(self.image, (96, 32))
        self.rect = self.image.get_rect()

        # blit the question text image onto the background image
        self.image.blit(self.text_image, (self.rect.size[0]/2 - self.text_rect.size[0]/2, self.rect.size[1]/2 - self.text_rect.size[1]/2))
        self.rect.y = self.ycor
        self.rect.x = self.xcor

    def __str__(self):
        return self.txt

    def update(self):
        # change the filename and thus change everything to change the background image of the bottom most question
        self.file_path = os.path.join(self.base_path, 'assets', self.filename)
        self.image = pg.image.load(self.file_path)
        self.image = pg.transform.scale(self.image, (96, 32))
        self.rect = self.image.get_rect()
        self.image.blit(self.text_image, (self.rect.size[0]/2 - self.text_rect.size[0]/2, self.rect.size[1]/2 - self.text_rect.size[1]/2))
        
        # it seems that self.image.blit() operation would reset self.rect's position to (0,0), and we have to reassign rect's position.
        self.ycor += self.speed
        self.rect.y = self.ycor
        self.rect.x = self.xcor
