import requests
import random

class MCGenerator:
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
        data_dict = self.data_list[0]

        # Creates a list of answers
        self.aquestion = data_dict['question']
        answer_list = [data_dict['correct_answer']]
        for i in data_dict['incorrect_answers']:
            answer_list.append(i)

        # Assigns answers randomly
        self.mc_list = random.sample(answer_list, 4)


    def showMCQuestion(self):
        '''
            Prints the question and four optional responses
            args: none
            return: none
        '''

        print(self.aquestion)
        print('a)', self.mc_list[0])
        print('b)', self.mc_list[1])
        print('c)', self.mc_list[2])
        print('d)', self.mc_list[3])            
        
def test():
    
    question_data = requests.get('https://opentdb.com/api.php?amount=1&category=19&difficulty=easy&type=multiple')

    print(type(question_data))
    question_data = question_data.json()

    print(question_data)
    print(type(question_data))

    data_list = question_data['results']

    print(data_list)
    print(type(data_list))

    data_dict = data_list[0]
    print(data_dict)
    print(type(data_dict))

    # Isolates question
    aquestion = data_dict['question']
    print(aquestion)
    
    # Creates a list of answers
    answer_list = [data_dict['correct_answer']]
    
    for i in data_dict['incorrect_answers']:
        answer_list.append(i)
    print(answer_list)

    # Sorts for multiple choice
    mc_list = [random.choice(answer_list) for i in answer_list]

    print(aquestion)
    print('1)', mc_list[0])
    print('2)', mc_list[1])    
    print('3)', mc_list[2])
    print('4)', mc_list[3])

    


def test2():
    print('########### Testing MCGenerator Level 1 ##############')
    try:
        math_question = MCGenerator('level1')
    except:
        print("Get questions from the local bank.")
    else:
        math_question.showMCQuestion()
        #print(math_question.data_list)

    print('########### Testing MCGenerator Level 2 ##############')    
    try:
        math_question = MCGenerator('level2')
    except:
        print("Get questions from the local bank.")
    else:
        math_question.showMCQuestion()
        #print(math_question.data_list)

    print('########### Testing MCGenerator Level 3 ##############') 
    try:
        math_question = MCGenerator('level3')
    except:
        print("Get questions from the local bank.")
    else:
        math_question.showMCQuestion()
        #print(math_question.data_list)

    print('############ MCGenerator Tests Complete ##############')

if __name__ == '__main__':

    test2()
