import pygame
import sys
from Surprise import *


def run_game():

    pygame.init()

    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption('This is a test. This is only a test.')

    surprise = Surprise()

    if surprise:
        surprise.getVideo()
    else:
        pygame.mixer.music.load('assets/China.wav')
        pygame.mixer.music.play(-1)
    

    while True:

        for event in pygame.event.get():
            if event.type == pygame.K_ESCAPE:
                sys.exit()
            elif event.type == pygame.K_s:
                surprise.endVideo()
                sys.exit()

        pygame.display.flip()

run_game()
