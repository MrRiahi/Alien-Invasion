
class Settings:
    """
    Settings of Alien Invasion game.
    """

    def __init__(self):
        """
        Initialize the game's settings.
        :return:
        """
        
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 500
        self.background_color = (255, 255, 255)
        
        # ُShip settings
        self.ship_limit = 3
        
        # Alien settings
        self.fleet_drop_speed = 5
        
        # Bullet settings
        self.bullet_width = 100
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # How quickly the game speeds up.
        self.speed_up_scale = 1.1
        
        # ---- Initialize dynamic settings ----
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.3

        # fleetDirection of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """ Increase speed settings. """
        
        self.ship_speed_factor *= self.speed_up_scale
        print('ship_speed_factor: ', self.ship_speed_factor)
        self.alien_speed_factor *= self.speed_up_scale
        print('alien_speed_factor: ', self.alien_speed_factor)
        self.bullet_speed_factor *= self.speed_up_scale
        print('bullet_speed_factor: ', self.bullet_speed_factor)
