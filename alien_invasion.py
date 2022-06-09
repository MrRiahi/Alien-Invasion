import pygame
from pygame.sprite import Group

from src.ship import Ship
from src.button import Button
import src.game_functions as gf
from src.settings import Settings
from src.scoreboard import Scoreboard
from src.game_statistics import GameStatistics


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    
    # Screen settings
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Create an instance to store game statistics.
    game_statistics = GameStatistics(settings=settings)
    
    scoreboard = Scoreboard(settings=settings, screen=screen, game_statistics=game_statistics)
    
    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(settings=settings, screen=screen)
    aliens = Group()
    bullets = Group()
    
    # Make a play button
    play_button = Button(screen=screen, message='Play')
    
    # Create the fleet of aliens
    gf.create_fleet(settings=settings, screen=screen, ship=ship, aliens=aliens)
    
    # Start the main loop for the game.
    while True:
        gf.check_events(settings=settings, screen=screen, game_statistics=game_statistics,
                        play_button=play_button, ship=ship, aliens=aliens,
                        bullets=bullets)
        
        if game_statistics.game_active:
            ship.update_position()
            gf.update_bullets(settings=settings, screen=screen,
                              scoreboard=scoreboard, game_statistics=game_statistics,
                              ship=ship, bullets=bullets, aliens=aliens)
            
            gf.update_aliens(settings=settings, screen=screen, game_statistics=game_statistics,
                             ship=ship, aliens=aliens, bullets=bullets)
            
        gf.update_screen(settings=settings, screen=screen, scoreboard=scoreboard,
                         ship=ship, aliens=aliens, bullets=bullets,
                         game_statistics=game_statistics, play_button=play_button)


if __name__ == '__main__':
    run_game()
    