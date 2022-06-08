
class Settings:
    """
    Settings of Alien Invasion game.
    """

    def __init__(self):
        """ Initialize the game's settings. """
        
        # Screen settings
        self.screenWidth = 1000
        self.screenHeight = 500
        self.backgroundColor = (255, 255, 255)
        
        # ُShip settings
        self.shipLimit = 3
        
        # Alien settings
        self.fleetDropSpeed = 5
        
        # Bullet settings
        self.bulletWidth = 100
        self.bulletHeight = 15
        self.bulletColor = (60, 60, 60)
        self.bulletsAllowed = 3
        
        # How quickly the game speeds up.
        self.speedUpScale = 1.1
        
        # Initialize dynamic settings.
        self.initializeDynamicSettings()
        
        
        
    def initializeDynamicSettings(self):
        """ Initialize settings that change throughout the game. """
        
        self.shipSpeedFactor = 1.5
        self.bulletSpeedFactor = 3
        self.alienSpeedFactor = 0.3
        
        # fleetDirection of 1 represents right; -1 represents left.
        self.fleetDirection = 1
        
        # Scoring
        self.alienPoints = 50
        
       
    
    def inreaseSpeed(self):
        """ Increase speed settings. """
        
        self.shipSpeedFactor *= self.speedUpScale
        print('shipSpeedFactor: ', self.shipSpeedFactor)
        self.alienSpeedFactor *= self.speedUpScale
        print('alienSpeedFactor: ', self.alienSpeedFactor)
        self.bulletSpeedFactor *= self.speedUpScale
        print('bulletSpeedFactor: ', self.bulletSpeedFactor)
