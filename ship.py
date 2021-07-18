import pygame


class Ship():
    """
    A class stores settings for ship.
    
    Author: MrR
    Date: Monday - 2020 18 May
    """
    
    
    
    def __init__(self, settings, screen):
        """ Initialize the ship and set its starting position. """
    
        self.screen = screen
        self.settings = settings
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('Images/ship.png')
        self.rect = self.image.get_rect()
        self.screenRect = self.screen.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screenRect.centerx
        self.rect.bottom = self.screenRect.bottom
        
        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        
        # Set right and left movement flag
        self.movingRight = False
        self.movingLeft = False
        
        
        
    def updatePosition(self):
        """ Update the ship's position based on movement flags. """
        
        # Moving right
        if (self.movingRight and self.rect.right < self.screenRect.right):
            self.center += self.settings.shipSpeedFactor
        
        # Moving left
        if (self.movingLeft and self.rect.left > self.screenRect.left):
            self.center -= self.settings.shipSpeedFactor
            
        # Update rect object from self.center.
        self.rect.centerx = self.center
        
        
        
    def blitme(self):
        """ Draw the ship at its current location. """
        
        self.screen.blit(self.image, self.rect)
    
    
    
    def centerShip(self):
        """ Center the ship on the screen. """
        
        self.center = self.screenRect.centerx