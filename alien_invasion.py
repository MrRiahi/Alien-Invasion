import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    
    # Screen settings
    settings = Settings()
    screen = pygame.display.set_mode((settings.screenWidth, settings.screenHeight))
    pygame.display.set_caption("Alien Invasion")
    
    # Create an instance to store game statistics.
    gameStats = GameStats(settings=settings)
    
    scoreboard = Scoreboard(settings=settings, screen=screen, gameStats=gameStats)
    
    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(settings=settings, screen=screen)
    aliens = Group()
    bullets = Group()
    
    # Make a play button
    playButton = Button(settings=settings, screen=screen, message='Play')
    
    # Create the fleet of aliens
    gf.createFleet(settings=settings, screen=screen, ship=ship, aliens=aliens)
    
    # Start the main loop for the game.
    while True:
        gf.checkEvents(settings=settings, screen=screen, gameStats=gameStats,
                       playButton=playButton, ship=ship, aliens=aliens,
                       bullets=bullets)
        
        if gameStats.gameActive:
            ship.updatePosition()
            gf.updateBullets(settings=settings, screen=screen,
                             scoreboard=scoreboard, gameStats=gameStats,
                             ship=ship, bullets=bullets, aliens=aliens)
            
            gf.updateAliens(settings=settings, screen=screen, gameStats=gameStats,
                            ship=ship, aliens=aliens, bullets=bullets)  
            
        gf.updateScreen(settings=settings, screen=screen, scoreboard=scoreboard,
                        ship=ship, aliens=aliens, bullets=bullets, 
                        gameStats=gameStats, playButton=playButton)


if __name__ == '__main__':
    run_game()
    