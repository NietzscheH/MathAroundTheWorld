import pygame as pg
from QuestionBox import QuestionBox as QB
from MenuButton import MenuButton
from AnswerTypein import AnswerTypein
import random


class Controller:
    def __init__(self):
        # initialize a screen
        pg.init()
        self.screen = pg.display.set_mode((1200, 800))
        pg.display.set_caption('A nice try')
        self.mouse_x, self.mouse_y = None, None

        self.questions = pg.sprite.Group()
        self.count = 0
        self.lives = 3
        self.density = 1000
        self.speed = 0.2
        self.start_button = MenuButton(self.screen)
        self.start_game = False
        self.ans = pg.sprite.Group()
        self.ans.add(AnswerTypein())
        
    def createQuestionBox(self):
        '''
            this method creates a questions box object and put it in a sprite group.
        '''
        x = random.randrange(50, 751)
        self.questions.add(QB(x, self.speed))
        self.count += 1

    def deleteOutscreenBox(self):
        '''
            this method deletes box objects that are out of the screen/ touching the bottom
        '''
        for sp in self.questions:
            if sp.y > self.screen.get_rect().size[1] - sp.h - 70:
                self.questions.remove(sp)

    def menu(self):
        '''
            show the start button on the screen
        '''
        self.screen.fill((200,200,200))
        if self.isOver(self.start_button.rect):
            self.start_button.isOver()
        else:
            self.start_button.notOver()
        self.screen.blit(self.start_button.image, self.start_button.rect)
    
    def isOver(self, rect):
        '''
            this method checks if mouse is over the rect
        '''
        if rect.center[0] - rect.size[0]/2 < self.mouse_x < rect.center[0] + rect.size[0]/2 and rect.center[1] - rect.size[1]/2 < self.mouse_y < rect.center[1] + rect.size[1]/2:
            return True
        else:
            return False

    def startGame(self, d):
        '''
            start dropping boxes down
        '''
        self.screen.fill((255,255,255))
        if d == self.density: # the bigger the density is, the slower the game goes
            self.createQuestionBox()
            d = 0
        d += 1
            
        self.questions.draw(self.screen)
        self.questions.update()
        self.deleteOutscreenBox()
        return d

    def typeAns(self):
        '''
            take users' keyboard input and show it onscreen
        '''
        self.ans.draw(self.screen)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                    pg.quit()
            elif event.type == pg.KEYDOWN:
                key_num = event.key
                self.ans.update(key_num)

    def mainloop(self):
        # loop it, or say, run it
        d = 1000
        while True:
            self.mouse_x, self.mouse_y = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit() #sys.exit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if self.start_button.rect.collidepoint(self.mouse_x, self.mouse_y):
                        self.start_game = True
            
            if self.start_game:
                d = self.startGame(d)
                self.typeAns()
            else:
                self.menu()


            pg.display.update()


