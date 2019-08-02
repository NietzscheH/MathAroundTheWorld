import pygame as pg
import os

class HealthIcon:
    def __init__(self):
        self.health = 3

        # get and rescale the image
        base_path = os.path.dirname(__file__)
        self.dict = {
            'China': pg.transform.scale(pg.image.load(os.path.join(base_path, 'assets', 'heart_1.png')), (32, 32)),
            'Egypt': pg.transform.scale(pg.image.load(os.path.join(base_path, 'assets', 'moon_1.png')), (32, 32)),
            'Italy': pg.transform.scale(pg.image.load(os.path.join(base_path, 'assets', 'moon_2.png')), (32, 32))
        }

        # blit the image onto a surface
        self.image = pg.Surface((96, 32), pg.SRCALPHA, 32).convert_alpha()
        
        self.icon = None

        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 10)
        # so, after initialization (i.e., after the object is created), the image is actually a blank image with nothing
        
    def update(self):
        '''
            Updates the health status
            args: none
            return: none
        '''
        self.health -= 1
        self.image = pg.Surface((96, 32), pg.SRCALPHA, 32).convert_alpha() # this step resets the image, or it will only draw upon the original image
    
    def byCountry(self, country):
        self.icon = self.dict[country]
        for i in range(self.health):
            self.image.blit(self.icon, (i*32,0))
        return self.image
