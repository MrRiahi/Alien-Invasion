import sys
import pygame
from time import sleep

from src.bullet import Bullet
from src.alien import Alien


def check_events(settings, screen, game_statistics, play_button, ship, aliens, bullets):
    """
    Respond to keypress and mouse events.
    :param settings: game settings
    :param screen: game screen
    :param game_statistics: game statistics
    :param play_button: play button
    :param ship: ship
    :param aliens: aliens
    :param bullets: ship's bullets
    """

    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        # ٍQuit event
        if event.type == pygame.QUIT:
            sys.exit()
    
        # Press the key
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, settings, screen, ship, bullets)
                
        # Release the key
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)
            
        # Click play button
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, game_statistics, play_button,
                            mouse_x, mouse_y, ship, aliens, bullets)
            

def check_key_down_events(event, settings, screen, ship, bullets):
    """
    Respond to down key presses.
    :param event:
    :param settings:
    :param screen:
    :param ship:
    :param bullets:
    :return:
    """

    # Right
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    # Left
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings=settings, screen=screen, ship=ship, bullets=bullets)


def fire_bullet(settings, screen, ship, bullets):
    """
    Fire a bullet if limit not reached yet..
    :param settings:
    :param screen:
    :param ship:
    :param bullets:
    :return:
    """

    # Create a new bullet and add it to the bullets group.
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings=settings, screen=screen, ship=ship)
        bullets.add(new_bullet)


def check_key_up_events(event, ship):
    """
    Respond to releases.
    :param event:
    :param ship:
    :return:
    """

    # Right
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    # Left
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
        

def update_screen(settings, screen, game_statistics, scoreboard, ship, aliens, bullets, play_button):
    """
    Update images on the screen and flip to the new screen.
    :param settings:
    :param screen:
    :param game_statistics:
    :param scoreboard:
    :param ship:
    :param aliens:
    :param bullets:
    :param play_button:
    :return:
    """
    
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.background_color)
    
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()
    aliens.draw(screen)
    
    # Draw score information.
    scoreboard.show_score()
    
    # Draw the play button if the game is inactive.
    if not game_statistics.game_active:
        play_button.draw_button()
    
    # Make the most recently drawn screen visible.
    pygame.display.flip()

    
def update_bullets(settings, screen, scoreboard, game_statistics, ship, aliens, bullets):
    """
    Update position of bullets and get rid of old bullets.
    :param settings:
    :param screen:
    :param scoreboard:
    :param game_statistics:
    :param ship:
    :param aliens:
    :param bullets:
    :return:
    """
    
    # Update bullet positions.
    bullets.update() 
    
    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
    # Check any bullets that have hit aliens. If so, get rid of the bullet 
    # and the alien.
    check_bullet_alien_collision(settings=settings, screen=screen,
                                 scoreboard=scoreboard, game_statistics=game_statistics,
                                 ship=ship, aliens=aliens, bullets=bullets)


def create_fleet(settings, screen, ship, aliens):
    """
    Create full fleet of aliens.
    :param settings:
    :param screen:
    :param ship:
    :param aliens:
    :return:
    """

    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    alien = Alien(settings=settings, screen=screen)
    alien_width = alien.rect.width
    n_aliens_x = get_alien_number_x(settings=settings, alien_width=alien_width)
    n_rows = get_number_of_rows(settings=settings, ship_height=ship.rect.height,
                                alien_height=alien.rect.height)
    
    # Create the fleet of aliens.
    for i_row in range(0, n_rows):
        for i_alien_x in range(0, n_aliens_x):
            create_alien(settings=settings, screen=screen, aliens=aliens, 
                         alien_width=alien_width, alien_number=i_alien_x,
                         row_number=i_row)


def get_alien_number_x(settings, alien_width):
    """
    Determine the number of aliens that fit in a row.
    :param settings:
    :param alien_width:
    :return:
    """

    available_space_x = settings.screen_width - 2 * alien_width
    n_aliens_x = int(available_space_x / (2 * alien_width))
    
    return n_aliens_x


def get_number_of_rows(settings, ship_height, alien_height):
    """
    Determine the number of rows of aliens that fit on the screen.
    :param settings:
    :param ship_height:
    :param alien_height:
    :return:
    """

    available_space_x = settings.screen_height - 2 * alien_height - ship_height
    n_rows = int(available_space_x / (2 * alien_height))
    
    return n_rows


def create_alien(settings, screen, aliens, alien_width, alien_number, row_number):
    """
    Create an alien and place it in the row.
    :param settings: game settings object.
    :param screen: pygame screen object.
    :param aliens: group of alien object.
    :param alien_width: width of an alien.
    :param alien_number: number of alien in a row.
    :param row_number: row number for aliens.
    :return:
    """

    # Create an alien
    alien = Alien(settings=settings, screen=screen)
    
    # Set X position of an alien
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    
    # Set Y position of an alien
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    
    # Add the alien
    aliens.add(alien)
    

def update_aliens(settings, screen, game_statistics, ship, aliens, bullets):
    """
    Check if the fleet is at an edge,
    and then update the positions of all aliens in the fleet.
    :param settings: game settings object.
    :param screen: pygame screen object.
    :param game_statistics: game stats object.
    :param ship: ship object.
    :param aliens: group of alien object.
    :param bullets: object of bullets.
    :return:
    """
    
    check_fleet_edges(settings, aliens)
    aliens.update()
    
    # Look for ship-alien collision.
    if pygame.sprite.spritecollideany(ship, aliens):
        restart_game(settings=settings, screen=screen, game_statistics=game_statistics, ship=ship,
                     aliens=aliens, bullets=bullets)
    
    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(settings=settings, screen=screen, game_statistics=game_statistics,
                        ship=ship, aliens=aliens, bullets=bullets)
    
    
def check_fleet_edges(settings, aliens):
    """
    Respond appropriately of any aliens have reached an edge.
    :param settings: game settings object.
    :param aliens: group of alien object.
        
    :returns:
    """
    
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break


def change_fleet_direction(settings, aliens):
    """
    Drop the entire fleet and change the fleet's direction.
    :param settings: game settings object.
    :param aliens: group of alien object.
    :return:
    """
    
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    
    settings.fleet_direction *= -1


def check_bullet_alien_collision(settings, screen, scoreboard, game_statistics, ship, aliens, bullets):
    """
    Respond to bullet-alien collisions.
    :param settings: game settings object.
    :param screen: pygame screen object.
    :param scoreboard:
    :param game_statistics:
    :param ship: ship object.
    :param aliens: group of alien object.
    :param bullets: object of bullets.
    :return:
    """
    
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if collisions:
        for aliens in collisions.values():
            game_statistics.score += settings.alien_points * len(aliens)
            scoreboard.prepare_score()
    
    # Check the fleet is empty or not
    if len(aliens) == 0:
        # Destroy existing bullets, speed up the game and create new fleet.
        bullets.empty()
        create_fleet(settings=settings, screen=screen, ship=ship, aliens=aliens)
        
        settings.increase_speed()


def restart_game(settings, screen, game_statistics, ship, aliens, bullets):
    """
    Respond to ship being hit by alien.
    :param settings: game settings object.
    :param screen: pygame screen object.
    :param game_statistics: game stats object.
    :param ship: ship object.
    :param aliens: group of alien object.
    :param bullets: object of bullets.
    :returns:
    """
    
    if game_statistics.ship_left > 0:
        # Decrement shipLeft
        game_statistics.ship_left -= 1
        
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        
        # Create a new fleet and center the ship.
        create_fleet(settings=settings, screen=screen, ship=ship, aliens=aliens)
        ship.center_ship()
    
        # Pause.
        sleep(0.5)
    else:
        game_statistics.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(settings, screen, game_statistics, ship, aliens, bullets):
    """
    Check if any aliens have reached the bottom of the screen.
    :param settings: game settings object.
    :param screen: pygame screen object.
    :param game_statistics: game stats object.
    :param ship: ship object.
    :param aliens: group of alien object.
    :param bullets: object of bullets.
    :return:
    """
    
    screen_rect = screen.get_rect()
    
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            restart_game(settings=settings, screen=screen, game_statistics=game_statistics,
                         ship=ship, aliens=aliens, bullets=bullets)
            break


def check_play_button(settings, screen, game_statistics, play_button, mouse_x, mouse_y,
                      ship, aliens, bullets):
    """
    Start a new game when the player clicks Play.
    :param settings: game settings object.
    :param screen: pygame screen object.
    :param game_statistics: game stats object.
    :param play_button: start button object.
    :param mouse_x:
    :param mouse_y:
    :param ship: ship object.
    :param aliens: group of alien object.
    :param bullets: object of bullets.
    :return:
    """
    
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    
    if button_clicked and (not game_statistics.game_active):       
        # Reset the game statistics.
        game_statistics.reset_statistics()
        game_statistics.game_active = True
        
        # Empty the aliens and bullets lists.
        aliens.empty()
        bullets.empty()
        
        # Initialize dynamic settings
        initialize_dynamic_settings(settings=settings)
        
        # Create a new fleet and center the ship.
        create_fleet(settings=settings, screen=screen, ship=ship, aliens=aliens)
        ship.center_ship()
        
        # Hide the mouse cursor
        pygame.mouse.set_visible(False)


def initialize_dynamic_settings(settings):
    """
    Initialize settings that change throughout the game.
    :param settings: game settings
    :return:
    """

    # ---- Initialize dynamic settings ----
    settings.ship_speed_factor = 1.5
    settings.bullet_speed_factor = 3
    settings.alien_speed_factor = 0.3

    # fleetDirection of 1 represents right; -1 represents left
    settings.fleet_direction = 1

    # Scoring
    settings.alien_points = 50
