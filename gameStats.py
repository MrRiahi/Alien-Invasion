class GameStats():
    """
    A class to tracks statistics for Alien Invasion.
    
    Author: MrR
    Date: Friday - 2020 29 May
    """
    
    
    
    def __init__(self, settings):
        """ Initialize statistics. """
        
        self.settings = settings
        
        # Start Alien Invasion in an inactive state.
        self.gameActive = False
        
        self.resetStats()
        
        
        
    def resetStats(self):
        """ Initialize statistics that can change during the game. """
        
        self.shipLeft = self.settings.shipLimit
        self.score = 0