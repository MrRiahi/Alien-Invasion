
class GameStatistics:
    """
    A class to tracks statistics for Alien Invasion.
    """

    def __init__(self, settings):
        """
        Initialize game statistics.
        :param settings: game settings
        :return:
        """

        self.ship_left = None
        self.score = 0
        
        self.settings = settings

        self.game_active = False  # Start Alien Invasion in an inactive state.
        
        self.reset_statistics()

    def reset_statistics(self):
        """
        Reset game statistics and initialize them.
        :return:
        """

        self.ship_left = self.settings.ship_limit
        self.score = 0
