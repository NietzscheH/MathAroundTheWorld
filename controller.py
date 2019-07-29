import pygame as pg
from QuestionBox import QuestionBox as QB
from QuestionGenerator import QuestionGenerator as QG
from MenuButton import MenuButton
from AnswerTypein import AnswerTypein
from ScoreBoard import ScoreBoard as SB
from HealthIcon import HealthIcon as HI
import random
from os import path


class Controller:
    def __init__(self):
        # initialize a screen
        pg.init()
        self.screen = pg.display.set_mode((1024, 768))
        pg.display.set_caption('Draft v1.4')
        self.mouse_x, self.mouse_y = None, None

        self.questions = pg.sprite.Group()
        self.count = 0 # currently has no use
        self.lives = 3
        self.score = 0
        self.density = 2500 # it means problems will be generated every 1000 frames
        self.speed = 0.1 # the speed of question boxes

        self.start_button = MenuButton('Start', self.screen.get_rect().center)
        self.again_button = MenuButton('Start Again', (512, 410), 60, (112,128,144))
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

        base_path = path.dirname(__file__)
        self.sound_effect = {
            'wrong': pg.mixer.Sound(path.join(base_path, 'assets', 'buzzer.wav')),
            'right': pg.mixer.Sound(path.join(base_path, 'assets', 'chime.wav')),
            'hit': pg.mixer.Sound(path.join(base_path, 'assets', 'clunk.wav'))
        }
        for i in self.sound_effect.keys():
            self.sound_effect[i].set_volume(0.15)
        
        
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
            if sp.ycor > self.screen.get_rect().size[1] - sp.height - 65:
                self.sound_effect['hit'].play()
                self.questions.remove(sp)
                self.user_health.update()
                self.lives -= 1
                if self.lives < 0:
                    self.STATE = 'end'
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
    
    def drawEnd(self):
        '''
            show the result page
        '''
        self.screen.fill((190,231,233))

        # display user's final score
        score_record = SB(self.score, (512,330), 60, (244,96,108))
        self.screen.blit(score_record.image, score_record.rect)

        if self.isOver(self.again_button.rect):
            self.again_button.isOver()
        else:
            self.again_button.notOver()
        self.screen.blit(self.again_button.image, self.again_button.rect)

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
            sp.bg_color = (160,238,225) # change the background color of the bottom most one
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
                self.sound_effect['right'].play()
                self.user_score.update() # in update(), the score will + 1
                self.score += 1 # I create another instance variable (score) here because it's more convenient
                self.questions.remove(sp)
            else:
                self.sound_effect['wrong'].play()
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

    def endLoop(self):
        self.mouse_x, self.mouse_y = pg.mouse.get_pos()
        self.drawEnd()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() #sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if self.again_button.rect.collidepoint(self.mouse_x, self.mouse_y):
                    self.STATE = 'game'

    def mainloop(self):
        # loop it, or say, run it
        while True: # without this loop, the game will exit automatically after clicking 'start again', because there is no codes after while STATE == 'end' loop
            d = 1000
            while self.STATE == 'menu':
                self.menuLoop()
                pg.display.update()
            while self.STATE == 'game':
                d = self.gameLoop(d)
                pg.display.update()
            while self.STATE == 'end':
                self.endLoop()
                pg.display.update()

            # reset everything
            self.questions.empty()
            self.ans_typein.result = ''
            self.ans_typein.update(0) # empty the type in box
            self.score, self.score_board.score = 0, -1
            self.user_score.update() # have to update to change the image
            self.lives, self.health_bar.health = 3, 4
            self.user_health.update() # same
