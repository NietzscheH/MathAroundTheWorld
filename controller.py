import pygame as pg
from QuestionBox import QuestionBox as QB
import random


class Controller:
    def __init__(self):
        self.screen = None
        self.question_list = []
        self.count = 0
        self.lives = 3
        self.density = 2000
        self.speed = 0.02
        
    def createQuestionBox(self, x=150, s=0.02):
        # create objects here
        x = random.randrange(50, 751)
        self.question_list.append(QB(x, s, self.screen))
        self.count += 1
        
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

            if d == self.density:
                self.createQuestionBox()
                d = 0
            d += 1

            for i in self.question_list:
                i.drawMyself()

            pg.display.update()


