import pygame


class Scoreboard():
    """
    A class to report scoring information.
    
    Author: MrR
    Date: Thursday - 2020 11 June
    """
    
    
    
    def __init__(self, settings, screen, gameStats):
        """ Initialize scorekeeping attributes. """
        
        self.settings = settings
        self.screen = screen
        self.screenRect = self.screen.get_rect()
        self.gameStats = gameStats
        
        # Font settings for scoring information.
        self.textColor = (0, 255, 0)
        self.font = pygame.font.SysFont(None, size=32)
        
        # Prepare the initial score image.
        self.prepareScore()
        
        
        
    def prepareScore(self):
        """ Turn the score into a rendered image. """
        
        scoreStr = str(self.gameStats.score)
        self.scoreImage = self.font.render(scoreStr, True, self.textColor,
                                           self.settings.backgroundColor)
        
        # Display the score at the top of the screen.
        self.scoreRect = self.scoreImage.get_rect()
        self.scoreRect.right = self.screenRect.right - 20
        self.scoreRect.top = 20
        
        
        
    def showScore(self):
        """ Draw score to the screen. """
        
        self.screen.blit(self.scoreImage, self.scoreRect)