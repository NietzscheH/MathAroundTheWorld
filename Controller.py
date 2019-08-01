import pygame as pg
from QuestionBox import QuestionBox as QB
from QuestionGenerator import QuestionGenerator as QG
from MenuButton import MenuButton
from MenuButton_ import MenuButton_ as MB
from AnswerTypein import AnswerTypein
from ScoreBoard import ScoreBoard as SB
from HealthIcon import HealthIcon as HI
import random
from os import path


class Controller:
    def __init__(self):
        # initialize a screen
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((1024, 768))
        pg.display.set_caption('v2.0')
        self.mouse_x, self.mouse_y = None, None

        # some users' identities are created here
        self.questions = pg.sprite.Group()
        self.count = 0 # currently has no use
        self.lives = 3
        self.score = 0
        self.density = 480 # it means problems will be generated every 480 frames
        self.speed = 3 # the speed of question boxes

        # some buttons are created here
        self.start_button = MB((512,404), 'startbasic.png', 'starthover.png')
        self.rules_button = MB((512,489), 'rulesbasic.png', 'ruleshover.png')
        self.credit_button = MB((512,574), 'creditbasic.png', 'credithover.png')

        self.China_button = MenuButton('China', (512, 304), 60, (197,31,31))
        self.Egypt_button = MenuButton('Eygpt', (512, 384), 60, (222,211,140))
        self.Italy_button = MenuButton('Italy', (512, 464), 60, (179,214,110))
        self.again_button = MenuButton('Start Again', (512, 410), 60, (112,128,144))
        self.ans_typein = AnswerTypein() # the type in box object
        self.ans = pg.sprite.Group() # the sprite group for the type in box object
        self.ans.add(self.ans_typein)

        # scoreboard and health bar objects
        self.score_board = SB()
        self.health_bar = HI()

        self.STATE = 'start'

        # general sound effects
        base_path = path.dirname(__file__)
        self.sound_effect = {
            'wrong': pg.mixer.Sound(path.join(base_path, 'assets', 'sound', 'sound_effects', 'buzzer.wav')),
            'right': pg.mixer.Sound(path.join(base_path, 'assets', 'sound', 'sound_effects', 'chime.wav')),
            'hit': pg.mixer.Sound(path.join(base_path, 'assets', 'sound', 'sound_effects', 'clunk.wav'))
        }
        for i in self.sound_effect.keys():
            self.sound_effect[i].set_volume(0.15)

        # background image
        self.bg_by_country = {
            'China': (255,255,255),
            'Egypt': (222,211,140),
            'Italy': (179,214,110)
        }

        # background music
        self.volume = 0
        self.bgm_player = pg.mixer.music
        self.bgm_by_country = {
            'China': [path.join(base_path, 'assets', 'China_BGM_1.mp3')],
            'Egypt': [None],
            'Italy': [None]
        }

    def createQuestionBox(self):
        '''
            this method creates a questions box object and put it in a sprite group.
        '''
        x = random.randrange(100, 924) # leave 100pixels on both sides
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
                self.health_bar.update()
                self.lives -= 1
                if self.lives < 0:
                    self.STATE = 'end'
            break # it only needs to run once per frame

    def drawStart(self):
        '''
            show the start button on the screen
        '''
        self.screen.fill((135,206,250)) # sky blue
        for button in [self.start_button, self.rules_button, self.credit_button]:
            if self.isOver(button.rect):
                button.isOver()
            else:
                button.notOver()
        self.screen.blits(((self.start_button.image, self.start_button.rect), (self.rules_button.image, self.rules_button.rect), (self.credit_button.image, self.credit_button.rect)))

    def drawMenu(self):
        '''
            show the menu on the screen
        '''
        self.screen.fill((175,215,237))
        for button in [self.China_button, self.Egypt_button, self.Italy_button]:
            if self.isOver(button.rect): button.isOver()
            else: button.notOver()

        # blits them; the para the blits() takes is a sequence, e.g. here we are using 3 tuples inside 1 tuple and that 1 tuple is parsed into blits()
        self.screen.blits(((self.China_button.image, self.China_button.rect), (self.Egypt_button.image, self.Egypt_button.rect), (self.Italy_button.image, self.Italy_button.rect)))

    def drawEnd(self):
        '''
            show the result page
        '''
        self.screen.fill((190,231,233))

        # display user's final score
        score_record = SB(self.score, (512,330), 60, (244,96,108)) # this is just another scoreboard object with different position, size, and color
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

    def drawGame(self, density, country):
        '''
            start dropping boxes down
        '''
        self.screen.fill(self.bg_by_country[country])
        if density == self.density: # the bigger the density is, the slower the game goes
            self.createQuestionBox()
            density = 0
        density += 1

        for sp in self.questions:
            sp.filename = 'moon_2.png'
            break
        self.questions.update()
        self.questions.draw(self.screen)
        self.deleteOutscreenBox()
        return density

    def checkAns(self, ans_submitted):
        '''
            check answer submitted by users
        '''
        for sp in self.questions:
            if sp.answer == ans_submitted:
                self.sound_effect['right'].play()
                self.score_board.update() # in update(), the score will + 1
                self.score += 1 # I create another instance variable (score) here because it's more convenient
                self.questions.remove(sp)
            else:
                self.sound_effect['wrong'].play()
            break
        #print(self.score_board.score, self.lives)


    def startLoop(self):
        self.mouse_x, self.mouse_y = pg.mouse.get_pos()
        self.drawStart()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() #sys.exit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                pg.quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if self.start_button.rect.collidepoint(self.mouse_x, self.mouse_y):
                    self.STATE = 'menu'
                elif self.rules_button.rect.collidepoint(self.mouse_x, self.mouse_y):
                    self.STATE = 'rules'
                elif self.credit_button.rect.collidepoint(self.mouse_x, self.mouse_y):
                    self.STATE = 'credt'

    def menuLoop(self):
        self.mouse_x, self.mouse_y = pg.mouse.get_pos()
        self.drawMenu()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.STATE = 'start'
            elif event.type == pg.MOUSEBUTTONDOWN:
                if self.China_button.rect.collidepoint(self.mouse_x, self.mouse_y):
                    # start play music here
                    self.STATE = 'game China'
                elif self.Italy_button.rect.collidepoint(self.mouse_x, self.mouse_y):
                    self.STATE = 'game Italy'
                elif self.Egypt_button.rect.collidepoint(self.mouse_x, self.mouse_y):
                    self.STATE = 'game Egypt'

    def ruleLoop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() #sys.exit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.STATE = 'start'

    def creditLoop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() #sys.exit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.STATE = 'start'

    def gameLoop(self, density, country):
        # adjust volume to create a fade in here
        density = self.drawGame(density, country)
        self.screen.blit(self.ans_typein.bg_image, self.ans_typein.bg_rect) # draw the background before drawing the text that users put in
        self.ans.draw(self.screen) # draw the text that users type in

        self.screen.blits(((self.score_board.image, self.score_board.rect), (self.health_bar.byCountry(country), self.health_bar.rect)))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.STATE = 'menu'
            elif event.type == pg.KEYDOWN:
                key_num = event.key # event.key is a number corresponds to the key
                self.ans.update(key_num)

                ans_submitted = self.ans_typein.submit()
                if ans_submitted is None: pass
                else: self.checkAns(ans_submitted) # ans_submiited will not be None if users hit ENTER key with numbers typed in
        return density

    def endLoop(self):
        self.mouse_x, self.mouse_y = pg.mouse.get_pos()
        self.drawEnd()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() #sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if self.again_button.rect.collidepoint(self.mouse_x, self.mouse_y):
                    self.STATE = 'start'

    def mainloop(self):
        # loop it, or say, run it
        while True: # without this loop, the game will exit automatically after clicking 'start again', because there is no codes after while STATE == 'end' loop
            density = 360
            self.volume = 0
            while self.STATE == 'start':
                self.startLoop()
                pg.time.Clock().tick(60) # set the frame rate to be 60 per second at most
                pg.display.update()
            while self.STATE == 'menu':
                self.menuLoop()
                pg.time.Clock().tick(60)
                pg.display.update()
            while self.STATE == 'rules':
                self.ruleLoop()
                pg.time.Clock().tick(60)
                pg.display.update()
            while self.STATE == 'credit':
                self.creditLoop()
                pg.time.Clock().tick(60)
                pg.display.update()
            while self.STATE[:4] == 'game': # note the difference here
                density = self.gameLoop(density, self.STATE[5:])
                pg.time.Clock().tick(60)
                pg.display.update()
            while self.STATE == 'end':
                self.endLoop()
                pg.time.Clock().tick(60)
                pg.display.update()

            # reset everything
            self.questions.empty()
            self.ans_typein.result = ''
            self.ans_typein.update(0) # empty the type in box
            self.score, self.score_board.score = 0, -1
            self.score_board.update() # have to update to change the image
            self.lives, self.health_bar.health = 3, 4
            self.health_bar.update() # same
