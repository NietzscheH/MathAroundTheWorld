import pygame as pg
from QuestionBox import QuestionBox as QB
import random


class Controller:
    def __init__(self):
        self.screen = None
        self.question_list = []
        self.count = 0
        self.lives = 3
        self.density = 1500
        self.speed = 0.05
        
    def createQuestionBox(self):
        # create objects here
        x = random.randrange(50, 751)
        self.question_list.append(QB(x, self.speed, self.screen))
        self.count += 1
    
    def deleteOutscreenBox(self):
        # delete boxes that are out of the screen
        for i in self.question_list[:]:
            if i.y > i.screen_size[1]-i.h:
                self.question_list.remove(i)
                self.count -= 1

    def initialize(self):
        # initialize a screen
        pg.init()
        self.screen = pg.display.set_mode((800, 600))
        pg.display.set_caption('A nice try')
    
    def runGame(self):
        # loop it, or say, run it
        d = 1000
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit() #sys.exit()
            
            self.screen.fill((255, 255, 255))

            if d == self.density: # the bigger the density is, the slower the game goes
                self.createQuestionBox()
                d = 0
            d += 1
            
            for i in self.question_list:
                i.drawMyself()
            self.deleteOutscreenBox()

            pg.display.update()


