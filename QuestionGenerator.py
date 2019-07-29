from random import *

class QuestionGenerator:
    def __init__(self):
        self.dict = {
            1: '+',
            2: '-',
            3: '*',
            4: '/'
        }
        pass

    def level_1(self):
        exp = '{num1}{operation}{num2}'.format(num1=randint(0, 9), operation=self.dict[randint(1, 4)], num2=randint(0, 9))
        if exp[1] == '/' and exp[-1] == '0':
            exp = exp.replace(exp[-1], str(randint(1, 9)))

        ans = round(eval(exp), 2)
        if ans == int(ans): ans = int(ans)

        try:
            exp = exp.replace('*', 'x')
        except:
            pass
        try:
            exp = exp.replace('/', '÷')
        except:
            pass
        return exp, str(ans)
