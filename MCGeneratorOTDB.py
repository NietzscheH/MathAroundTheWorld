import requests
import random

class MCGeneratorOTDB:
    '''
        This Proxy class supplies multiple choice questions from opentdb.com
    '''

    def __init__(self, level):

        self.level = level
        if self.level == 'level1':
            question_data = requests.get('https://opentdb.com/api.php?amount=1&category=19&difficulty=easy&type=multiple')
        
        elif self.level == 'level2':
            question_data = requests.get('https://opentdb.com/api.php?amount=1&category=19&difficulty=medium&type=multiple')

        else:
            question_data = requests.get('https://opentdb.com/api.php?amount=1&category=19&difficulty=hard&type=multiple')

        # Converts json to Python dictionary
        question_data = question_data.json()
        self.data_list = question_data['results']
        self.data_dict = self.data_list[0]

        # Creates a list of answers
        self.aquestion = self.data_dict['question']
        answer_list = [self.data_dict['correct_answer']]
        for i in self.data_dict['incorrect_answers']:
            answer_list.append(i)

        # Assigns answers randomly
        random_list = random.sample(answer_list, 4)
        self.choice_a = "a) " + random_list[0]
        self.choice_b = "b) " + random_list[1]
        self.choice_c = "c) " + random_list[2]
        self.choice_d = "d) " + random_list[3]

        self.mc_list = [self.choice_a, self.choice_b, self.choice_c, self.choice_d]

        # Identify correct answer
        for choice in self.mc_list:
            if self.data_dict['correct_answer'] in choice:
                correct_choice = choice
        self.ans = correct_choice


    def showMCQuestion(self):
        '''
            Prints the question and four optional responses
            args: none
            return: ('str') the correct answer to the question
        '''

        print(self.aquestion)
        print(self.choice_a)
        print(self.choice_b)
        print(self.choice_c)
        print(self.choice_d)

        return self.ans
                   
        
def test():
    print('########### Testing MCGeneratorOTDB Level 1 ##############')
    try:
        math_question = MCGeneratorOTDB('level1')
    except:
        print("Get questions from the local bank.")
    else:
        math_question.showMCQuestion()
        print('Answer: ', math_question.ans)
        #print(math_question.data_list)

    print('########### Testing MCGeneratorOTDB Level 2 ##############')    
    try:
        math_question = MCGeneratorOTDB('level2')
    except:
        print("Get questions from the local bank.")
    else:
        math_question.showMCQuestion()
        print('Answer: ', math_question.ans)
        #print(math_question.data_list)

    print('########### Testing MCGeneratorOTDB Level 3 ##############') 
    try:
        math_question = MCGeneratorOTDB('level3')
    except:
        print("Get questions from the local bank.")
    else:
        math_question.showMCQuestion()
        print('Answer: ', math_question.ans)
        #print(math_question.data_list)

    print('############ MCGeneratorOTDB Tests Complete ##############')

if __name__ == '__main__':

    test()
