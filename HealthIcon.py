import pygame

class HealthIcon:
    '''
    The instances of this class respresent the number of chances the user has
        to get a correct answer before the game ends
    '''
    def __init__(self, x_coor, y_coor):
        '''
        Initializes a healthicon object
        args:
              x_coor ('int') the x-coordinate of the upper left corner
              y_coor ('int') the y-coordinate of the upper left corner
        return: ('HealthIcon') object of class Scoreboard
        '''
        # Initializes Sprite functionality
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        # Gets the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x_coor
        self.rect.y = y_coor

    def __str__(self):
        '''
        Stringification of healthicon object
        args: none
        return: coordinates for the upper left corner
        '''
        return 'Health Icon: (', + str(x_coor) + ', ' + str(y_coor) + ')'

