import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """
    A class to represent a single alien in the fleet.
    
    Author: MrR
    Date: Thursday - 2020 28 May
    """


    
    def __init__(self, screen, settings):
        """ Initialize the alien and set its starting position. """
        
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings
        
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('Images/alien.png')
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left of the screen.
        self.x = self.rect.width
        self.y = self.rect.height
        
        # Store the alien's exact position.
        self.x = float(self.rect.x)



    def blitme(self):
        """ Draw the alien at its current location. """
        
        self.screen.blit(self.image, self.rect)



    def checkEdges(self):
        """ Return True if alien is at edge of screen. """
        
        screenRect = self.screen.get_rect()
        
        if self.rect.right >= screenRect.right:
            return True
        elif self.rect.left <= screenRect.left:
            return True
        
        
    def update(self):
        """ Move the alien right or left. """
        
        self.x += (self.settings.alienSpeedFactor * self.settings.fleetDirection)
        self.rect.x = self.x
        