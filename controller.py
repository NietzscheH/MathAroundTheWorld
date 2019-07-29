import pygame as pg
from QuestionBox import QuestionBox as QB
from QuestionGenerator import QuestionGenerator as QG
from MenuButton import MenuButton
from AnswerTypein import AnswerTypein
from ScoreBoard_ import ScoreBoard as SB
from HealthIcon_ import HealthIcon as HI
import random


class Controller:
    def __init__(self):
        # initialize a screen
        pg.init()
        self.screen = pg.display.set_mode((1024, 768))
        pg.display.set_caption('Draft v1.3')
        self.mouse_x, self.mouse_y = None, None

        self.questions = pg.sprite.Group()
        self.count = 0 # currently has no use
        self.lives = 3
        self.score = 0
        self.density = 1500 # it means problems will be generated every 1000 frames
        self.speed = 0.08 # the speed of question boxes

        self.start_button = MenuButton('Start', self.screen.get_rect().center)
        self.ans_typein = AnswerTypein()
        self.ans = pg.sprite.Group()
        self.ans.add(self.ans_typein)

        self.score_board = SB()
        self.health_bar = HI()
        self.user_score = pg.sprite.Group()
        self.user_score.add(self.score_board)
        self.user_health = pg.sprite.Group()
        self.user_health.add(self.health_bar)
        self.STATE = 'menu'
        
    def createQuestionBox(self):
        '''
            this method creates a questions box object and put it in a sprite group.
        '''
        x = random.randrange(50, 974) # leave 50pixels on both sides
        problem_obj = QG()

        if self.score <= 10:
            problem = problem_obj.level_1()
            self.questions.add(QB(x, self.speed, problem[0], problem[1]))
            print(problem)
        else: self.questions.add(QB(x, self.speed))

    def deleteOutscreenBox(self):
        '''
            this method deletes box objects that are out of the screen/ touching the bottom
        '''
        for sp in self.questions:
            if sp.y > self.screen.get_rect().size[1] - sp.h - 65:
                self.questions.remove(sp)
                self.user_health.update()
                self.lives -= 1
            break # it only needs to run once per frame

    def drawMenu(self):
        '''
            show the start button on the screen
        '''
        self.screen.fill((135,206,250)) # sky blue
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
        
        for sp in self.questions:
            sp.bg_color = (0,255,255) # change the background color of the bottom most one
            break
        self.questions.update()
        self.questions.draw(self.screen)
        self.deleteOutscreenBox()
        return d

    def checkAns(self, ans_submitted):
        '''
            check answer submitted by users
        '''
        for sp in self.questions:
            if sp.answer == ans_submitted:
                self.user_score.update() # in update(), the score will + 1
                self.score += 1 # I create another instance variable (score) here because it's more convenient
                self.questions.remove(sp)
            break
        #print(self.score_board.score, self.lives)


    def menuLoop(self):
        self.mouse_x, self.mouse_y = pg.mouse.get_pos()
        self.drawMenu()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() #sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if self.start_button.rect.collidepoint(self.mouse_x, self.mouse_y):
                    self.STATE = 'game'
    
    def gameLoop(self, d):
        d = self.startGame(d)
        self.screen.blit(self.ans_typein.bg_image, self.ans_typein.bg_rect) # draw the background before drawing the text that users put in
        self.ans.draw(self.screen) # draw the text that users type in
        self.user_score.draw(self.screen) # draw the scoreboard
        self.user_health.draw(self.screen) # draw the health icon
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.KEYDOWN:
                key_num = event.key # event.key is a number corresponds to the key
                self.ans.update(key_num)
                ans_submitted = self.ans_typein.submit()
                if ans_submitted is None: pass
                else: self.checkAns(ans_submitted) # ans_submiited will not be None if users hit ENTER key with numbers typed in
        return d

    def mainloop(self):
        d = 1000
        # loop it, or say, run it
        while self.STATE == 'menu':
            self.menuLoop()
            pg.display.update()
        while self.STATE == 'game':
            d = self.gameLoop(d)
            pg.display.update()

