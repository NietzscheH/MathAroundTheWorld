from AnswerTypein import AnswerTypein
from QuestionBox import QuestionBox
from MenuButton import MenuButton
from Controller import Controller
import pygame as pg

pg.init()
print('##### Testing question box generator #####')
testQB = QuestionBox(100, 1)
testQB.update()
assert testQB.rect.y == -29
print('##### Test completed #####')

print('##### Testing answer typein #####')
testAT = AnswerTypein()
testAT.update(53)
assert testAT.result == '5'
print('##### Test completed #####')
