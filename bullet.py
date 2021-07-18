import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """
    A class to manage bullets fired from the ship.
    
    Author: MrR
    Date: Friday - 2020 22 May
    """
    
    
    
    def __init__(self, settings, screen, ship):
        """ Create a bullet object at the ship's current position. """
        
        super(Bullet, self).__init__()
        self.screen = screen
        
        # Create a bullet rect at (0, 0) and then set correct position. 
        self.rect = pygame.Rect(0, 0, settings.bulletWidth, settings.bulletHeight)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        
        self.bulletColor = settings.bulletColor
        self.bulletSpeedFactor = settings.bulletSpeedFactor
    
    
    
    def update(self):
        """ Move the bullet up the screen. """
        
        # Update the decimal position of the bullet.
        self.y -= self.bulletSpeedFactor
        # Update the rect position.
        self.rect.y = self.y
        
    
    
    def drawBullet(self):
        """ Draw the bullet to the screen. """
        pygame.draw.rect(self.screen, self.bulletColor, self.rect)