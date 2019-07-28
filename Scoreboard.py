import pygame

class Scoreboard:
    '''
    This class displays the user's current score
    '''
    def __init__(self, x_coor, y_coor, score):
        '''
        Initializes a scoreboard object
        args:
              score ('int') positive integer that represents the user's
                current score
              x_coor ('int') the x-coordinate of the upper left corner
              y_coor ('int') the y-coordinate of the upper left corner              
        return: ('Scoreboard') object of class Scoreboard
        '''
        # Initializes Sprite functionality
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        # Gets the rectangle for positioning
        self.rect = self.image.get_rect()        
        self.rect.x = x_coor
        self.rect.y = y_coor
        self.score = score

    def __str__(self):
        '''
        Stringification of scoreboard object
        args: none
        return: none
        '''
        return 'Current Score: ' + str(self.score)

    def updateScoreboard(new_score):
        '''
        Updates the scoreboard to display a new score
        args: new_score ('int') the updated score
        return: none
        '''
        # Updates image
        pass   


