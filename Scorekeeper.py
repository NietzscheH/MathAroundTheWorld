import pygame

class Scorekeeper:
    '''
    This class keeps track of the user's score and the status of the
        Scoreboard and HealthIcons
    '''
    def __init__(self, current_score, health_tally, health_icon_count):
        '''
        Initializes a scorekeeper object
        args:
              current_score ('int') the user's current score
              health_tally ('int') an intermediate tally use to calculate
                  when Health Icons will be earned or deducted
              health_icon_count ('int') the current number of Health Icons
        return: ('Scorekeeper') object of class Scorekeeper
        '''
        self.current_score = 90
        self.health_tally = 0
        self.health_icon_count = 3

    def __str__(self):
        '''
        Stringification of scorekeeper object
        args: none
        return: current score and number of HealthIcons
        '''
        return 'Score: ' + str(self.current_score) + ' Health Icons: ' + str(self.health_icon_count)

    def updateScore(self, direction):
        '''
        Updates scorekeeper based on user's performance
        args: direction ('int') 1 for correct answer; -1 for wrong answer 
                or box hitting ground
        return: new_score ('tuple') (current_score, health_icon_count_change);
                the Controller can index into the tuple to update the
                scoreboard and the number of Health Icon sprites displayed
        '''
        # Updates score for correct answer
        if direction == 1:
            self.current_score += 10
            self.health_tally += 1
        # Updates score for wrong answer or box hitting ground
        elif direction == -1:
            self.current_score -= 10
            self.health_tally -= 1
        else:
            self.current_score = self.current_score
            self.health_tally = self.health_tally

        # Updates number of Health Icons if necessary
        if self.health_tally == 3 and self.health_icon_count < 3:
            self.health_icon_count += 1
            health_icon_count_change = 1
            self.health_tally = 0
        elif self.health_tally == -3 and self.health_icon_count > 0:
            self.health_icon_count -= 1
            health_icon_count_change = -1
            self.health_tally = 0
        else:
            health_icon_count_change = 0

        return (self.current_score, health_icon_count_change)

def test():
    
    print('#### Testing Scorekeeper Class ####')
    
    test_scorekeeper = Scorekeeper((1024, 768), 90, 3)

    print('==== Testing initialization ====')
    assert test_scorekeeper.current_score == 90
    assert test_scorekeeper.health_tally == 0
    assert test_scorekeeper.health_icon_count == 3

    print('==== Testing updateScore ====')
    test_scorekeeper.updateScore(-1)
    assert test_scorekeeper.current_score == 80
    assert test_scorekeeper.health_tally == -1
    test_scorekeeper.updateScore(-1)
    assert test_scorekeeper.current_score == 70
    assert test_scorekeeper.health_tally == -2
    test_scorekeeper.updateScore(-1)
    assert test_scorekeeper.current_score == 60
    assert test_scorekeeper.health_icon_count == 2
    assert test_scorekeeper.health_tally == 0
    test_scorekeeper.updateScore(0)
    assert test_scorekeeper.current_score == 60
    assert test_scorekeeper.health_tally == 0
    test_scorekeeper.updateScore(1)
    assert test_scorekeeper.current_score == 70
    assert test_scorekeeper.health_tally == 1

    print('**** Scorekeeper Class Passes All Tests ****')

if __name__ == '__main__':

    test()

     
