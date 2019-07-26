from AnswerTypein import AnswerTypein
from QuestionBox import QuestionBox
from MenuButton import MenuButton
from Controller import Controller


print('##### Testing question box generator #####')
assert str(QuestionBox(100,0.05)) == 'Hello'
print('##### Test completed #####')

print('##### Testing menu button #####')
assert str(MenuButton(Controller.screen)) == str(Controller.screen.get_rect().center)
print('##### Test completed')
