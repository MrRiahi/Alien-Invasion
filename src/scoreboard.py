import pygame


class Scoreboard:
    """
    Report scoring information.
    """

    def __init__(self, settings, screen, game_statistics):
        """
        Initialize score keeping attributes.
        :param settings: game settings
        :param screen: game screen
        :param game_statistics: game statistics
        :return:
        """
        
        self.settings = settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.game_statistics = game_statistics

        # Font settings for scoring information.
        self.textColor = (0, 255, 0)
        self.font = pygame.font.SysFont(None, size=32)
        
        # Prepare the initial score image.
        self.prepare_score()

    def prepare_score(self):
        """
        Turn the score into rendered image
        :return:
        """
        
        scoreStr = str(self.game_statistics.score)
        self.score_image = self.font.render(scoreStr, True, self.textColor,
                                            self.settings.background_color)
        
        # Display the score at the top of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def show_score(self):
        """
        Draw score to the screen.
        :return:
        """
        
        self.screen.blit(self.score_image, self.score_rect)
