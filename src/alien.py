import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """
    An alien in the fleet.
    """
    
    def __init__(self, screen, settings):
        """
        Initialize the alien and set its starting position.
        :param screen: game screen
        :param settings: game settings
        :return:
        """
        
        super(Alien, self).__init__()  # Are you sure?????????????
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

    def blitme(self):  # check the correct names.
        """
        Draw the alien at its current location.
        :return:
        """
        
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """
        Check edges of the screen. If the alien is at the edge of the screen, return True.
        :return:
        """

        screen_rect = self.screen.get_rect()
        
        if self.rect.right >= screen_rect.right or self.rect.left <= screen_rect.left:
            return True

    def update(self):
        """
        Move the alien right or left.
        :return:
        """

        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x
        