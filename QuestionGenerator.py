from random import *

class QuestionGenerator:
    def __init__(self):
        self.dict = {
            1: '+',
            2: '-',
            3: '*',
            4: '/'
        }

    def level_1(self):
        '''
            Uses random processes to produce questions for Level 1
            args: none
            return: (exp, ans) ('tuple') two strings: the first contains
                    the question, the second contains the answer
        '''
        # Randomly selects two numbers and an operator
        exp = '{num1}{operation}{num2}'.format(num1=randint(0, 9), operation=self.dict[randint(1, 4)], num2=randint(0, 9))
        
        # Avoids dividing by zero
        if exp[1] == '/' and exp[-1] == '0':
            exp = exp.replace(exp[-1], str(randint(1, 9)))

        ans = round(eval(exp), 2)
        if ans == int(ans): ans = int(ans)

        # Replaces Pythonic operators with more reader-friendly symbols
        try:
            exp = exp.replace('*', 'x')
        except:
            pass
        try:
            exp = exp.replace('/', '÷')
        except:
            pass
        return exp, str(ans)
