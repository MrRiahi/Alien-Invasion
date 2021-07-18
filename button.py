import pygame


class Button():
    """
    A class to manage buttons.
    
    Author: MrR
    Date: Sunday - 2020 31 May
    """
    
    
    
    def __init__(self, settings, screen, message):
        """ Initialize button attributes. """
        
        self.screen = screen
        self.screenRect = self.screen.get_rect()
        
        # Set the dimensions and properties of the button.
        self.width, self.height = 75, 50
        self.buttonColor = (0, 255, 0)
        self.textColor = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 36)
        
        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screenRect.center
        
        # The button message needs to be prepared only once.
        self.prepareMessage(message)
        
        
        
    def prepareMessage(self, message):
        """ Turn message into a rendered image and center text on the button. """
        
        self.messageImage = self.font.render(message, True,
                                             self.textColor, self.buttonColor)
        self.messageImageRect = self.messageImage.get_rect()
        self.messageImageRect.center = self.rect.center
        
        
        
    def drawButton(self):
        """  Draw blank button and then draw message. """
        
        self.screen.fill(self.buttonColor, self.rect)
        self.screen.blit(self.messageImage, self.messageImageRect)