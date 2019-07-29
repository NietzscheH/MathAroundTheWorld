from AnswerTypein import AnswerTypein
from QuestionBox import QuestionBox
from MenuButton import MenuButton
from Controller import Controller
from QuestionGenerator import QuestionGenerator
import pygame as pg

def main():
    pg.init()
    print('##### Testing question box generator #####')
    testQB = QuestionBox(100, 1)
    testQB.update()
    assert testQB.rect.y == -35
    print('##### Test completed #####')

    print('##### Testing answer typein #####')
    testAT = AnswerTypein()
    testAT.update(53)
    assert testAT.result == '5'
    print('##### Test completed #####')

    print('##### Testing question generator #####')
    testQG = QuestionGenerator()
    exp, ans = testQG.level_1()
    assert str(eval(exp)) == ans
    print('##### Test completeted #####')

main()
