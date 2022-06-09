import pygame


class Ship:
    """
    A ship class.
    """
    
    def __init__(self, settings, screen):
        """
        Initialize the ship and set its starting position.
        :param settings: game setting
        :param screen: game screen
        :return:
        """
    
        self.screen = screen
        self.settings = settings
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('./Images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        
        # Set right and left movement flag
        self.moving_right = False
        self.moving_left = False

    def update_position(self):
        """
        Update the ship's position based on movement flags.
        :return:
        """
        
        # Moving right
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        
        # Moving left
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.settings.ship_speed_factor
            
        # Update rect object from self.center.
        self.rect.centerx = self.center
        
    def blitme(self):
        """
        Draw the ship at its current location.
        :return:
        """
        
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """
        Center the ship on the screen.
        :return:
        """
        
        self.center = self.screen_rect.centerx
