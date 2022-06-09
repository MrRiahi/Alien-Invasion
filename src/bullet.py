import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """
    class of fired bullets from the ship.
    """

    def __init__(self, settings, screen, ship):
        """
        Create a bullet object at the ship's current position.
        :param screen: game screen
        :param settings: game settings
        :param ship: ship object
        :return:
        """
        
        super(Bullet, self).__init__()
        self.screen = screen
        
        # Create a bullet rect at (0, 0) and then set correct position. 
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        
        self.bullet_color = settings.bullet_color
        self.bullet_speed_factor = settings.bullet_speed_factor

    def update(self):
        """
        Move the bullet up the screen.
        :return:
        """
        
        # Update the decimal position of the bullet.
        self.y -= self.bullet_speed_factor

        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """
        Draw the bullet to the screen.
        :return:
        """

        pygame.draw.rect(self.screen, self.bullet_color, self.rect)
