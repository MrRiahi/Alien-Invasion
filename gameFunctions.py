import sys
import pygame
from time import sleep

from bullet import Bullet
from alien import Alien


def checkEvents(settings, screen, gameStats, playButton, ship, aliens, bullets):
    """
    Respond to keypress and mouse events.
    
    Parameters
    ----------
        
    Returns
    ----------
    
    Author: MrR
    Date: Tuesday - 2020 19 May
    """
    
    
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        # ٍQuit event
        if event.type == pygame.QUIT:
            sys.exit()
    
        # Press the key
        elif event.type == pygame.KEYDOWN:
            checkKeyDownEvents(event, settings, screen, ship, bullets)
                
        # Release the key
        elif event.type == pygame.KEYUP:
            checkKeyUpEvents(event, ship)
            
        # Click play button
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            checkPlayButton(settings, screen, gameStats, playButton, 
                            mouseX, mouseY, ship, aliens, bullets)
            
            
    
    
def checkKeyDownEvents(event, settings, screen, ship, bullets):
    """
    Respond to keypresses.
    
    Parameters
    ----------
    event: Object
        Object of pygame event.
    ship: Object
        Object of ship.
        
    Returns
    ----------
    
    Author: MrR
    Date: Friday - 2020 22 May
    """
    
    
    # Right
    if event.key == pygame.K_RIGHT:
        ship.movingRight = True
    # Left
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = True
    elif event.key == pygame.K_SPACE:
        fireBullet(settings=settings, screen=screen, ship=ship, bullets=bullets)
    
    
    
def fireBullet(settings, screen, ship, bullets):
    """
    Fire a bullet if limit not reached yet..
    
    Parameters
    ----------
    settings: Object
        Object of game settings.
    screen: Object
        Pygame screen object.
    ship: Object
        Object of ship.
    bullets: Object
        Object of bullets.
        
    Returns
    ----------
    
    Author: MrR
    Date: Saturday - 2020 23 May
    """
    
    
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < settings.bulletsAllowed:
        newBullet = Bullet(settings=settings, screen=screen, ship=ship)
        bullets.add(newBullet)


    
def checkKeyUpEvents(event, ship):
    """
    Respond to releases.
    
    Parameters
    ----------
    event: Object
        Object of pygame event.
    ship: Object
        Object of ship.
        
    Returns
    ----------
    
    Author: MrR
    Date: Friday - 2020 22 May
    """
    
    
    # Right
    if event.key == pygame.K_RIGHT:
        ship.movingRight = False
    # Left
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = False
        
    
    
def updateScreen(settings, screen, gameStats, scoreboard, ship, aliens, 
                 bullets, playButton):
    """
    Update images on the screen and flip to the new screen.
    
    Parameters
    ----------
    settings: Object
        Game settings object.
    screen: Object
        Pygame screen object.
    scoreboard: Object
        Score object.
    ship: Object
        Ship object.
    alien: Object
        Alien object.
    bullets: Object
        Bullets object.
        
    Returns
    ----------
    
    Author: MrR
    Date: Tuesday - 2020 19 May
    Update: Thursday - 2020 11 June
    """
    
    
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.backgroundColor)
    
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.drawBullet()
    
    ship.blitme()
    aliens.draw(screen)
    
    # Draw score information.
    scoreboard.showScore()
    
    # Draw the play button if the game is inactive.
    if (not gameStats.gameActive):
        playButton.drawButton()
    
    # Make the most recently drawn screen visible.
    pygame.display.flip()
  
    
    
def updateBullets(settings, screen, scoreboard, gameStats, ship, aliens, 
                  bullets):
    """
    Update position of bullets and get rid of old bullets.
    
    Parameters
    ----------
    settings: Object
        Game settings object.
    screen: Object
        Pygame screen object.
    ship: Object
        Ship object.
    aliens: Object
        Group of alien object.
    bullets: Object
        Object of bullets.
        
    Returns
    ----------
    
    Author: MrR
    Date: Saturday - 2020 23 May
    Update: Friday - 2020 29 May
    """
    
    
    # Update bullet positions.
    bullets.update() 
    
    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
    # Check any bullets that have hit aliens. If so, get rid of the bullet 
    # and the alien.
    checkBulletAlienCollision(settings=settings, screen=screen, 
                              scoreboard=scoreboard, gameStats=gameStats, 
                              ship=ship, aliens=aliens, bullets=bullets)



def createFleet(settings, screen, ship, aliens):
    """
    Create full fleet of aliens.
    
    Parameters
    ----------
    settings: Object
        Game settings object.
    screen: Object
        Pygame screen object.
    ship: Object
        Ship object.
    aliens: Object
        Group of alien object.
        
    Returns
    ----------
    
    Author: MrR
    Date: Thursday - 2020 28 May
    """
    
    
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    alien = Alien(settings=settings, screen=screen)
    alienWidth = alien.rect.width
    nAliensX = getAlienNumberX(settings=settings, alienWidth=alienWidth)
    nRows = getNumberOfRows(settings=settings, shipHeight=ship.rect.height,
                            alienHeight=alien.rect.height)
    
    # Create the fleet of aliens.
    for iRow in range(0, nRows):
        for alienNumber in range(0, nAliensX):
            createAlien(settings=settings, screen=screen, aliens=aliens, 
                        alienWidth=alienWidth, alienNumber=alienNumber,
                        rowNumber=iRow)
        
        
        
def getAlienNumberX(settings, alienWidth):
    """
    Determine the number of aliens that fit in a row.
    
    Parameters
    ----------
    settings: Object
        Game settings object.
    alienWidth: int
        Width of an alien.
        
    Returns
    ----------
    nAliensX: int
        Number of aliens that fit in a row.
    
    Author: MrR
    Date: Thursday - 2020 28 May
    """
    
    
    availableSpaceX = settings.screenWidth - 2 * alienWidth
    nAliensX = int(availableSpaceX / (2 * alienWidth))
    
    return nAliensX



def getNumberOfRows(settings, shipHeight, alienHeight):
    """
    Determine the number of rows of aliens that fit on the screen.
    
    Parameters
    ----------
    settings: Object
        Game settings object.
    shipHeight: int
        Height of a ship.
    alienHeight: int
        Height of an alien.
        
    Returns
    ----------
    nRows: int
        Number of rows for aliens.
    
    Author: MrR
    Date: Thursday - 2020 28 May
    """
    
    
    availableSpaceX = settings.screenHeight - 2 * alienHeight - shipHeight
    nRows = int(availableSpaceX / (2 * alienHeight))
    
    return nRows



def createAlien(settings, screen, aliens, alienWidth, alienNumber, rowNumber):
    """
    Create an alien and place it in the row.
    
    Parameters
    ----------
    settings: Object
        Game settings object.
    screen: Object
        Pygame screen object.
    aliens: Object
        Group of alien object.
    alienWidth: int
        Width of an alien.
    alienNumber: int
        The number of alien in a row.
    rowNumber: int
        The row number for aliens.
        
    Returns
    ----------
    
    Author: MrR
    Date: Thursday - 2020 28 May
    """
    
    
    # Create an alien
    alien = Alien(settings=settings, screen=screen)
    
    # Set X position of an alien
    alien.x = alienWidth + 2 * alienWidth * alienNumber
    alien.rect.x = alien.x
    
    # Set Y position of an alien
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * rowNumber
    
    # Add the alien
    aliens.add(alien)



def updateAliens(settings, screen, gameStats, ship, aliens, bullets):
    """
    Check if the fleet is at an edge,
    and then update the postions of all aliens in the fleet.
    
    Parameters
    ----------
    settings: Object
        Game settings object.
    screen: Object
        Pygame screen object.
    gameStats: Object
        Game stats object.
    ship: Object
        Ship object.
    aliens: Object
        Group of alien object.
    bullets: Object
        Object of bullets.
        
    Returns
    ----------
    
    Author: MrR
    Date: Friday - 2020 29 May
    """
    
    
    checkFleetEdges(settings, aliens)
    aliens.update()
    
    ## Look for ship-alien collision.
    if pygame.sprite.spritecollideany(ship, aliens):
        restartGame(settings=settings, screen=screen, gameStats=gameStats, ship=ship,
                aliens=aliens, bullets=bullets)
    
    # Look for aliens hitting the bottom of the screen.
    checkAliensBottom(settings=settings, screen=screen, gameStats=gameStats,
                      ship=ship, aliens=aliens, bullets=bullets)
    
    
    
def checkFleetEdges(settings, aliens):
    """
    Respond appropriately of any aliens have reached an edge.
    
    Parameters
    ----------
    settings: Object
        Game settings object.
    aliens: Object
        Group of alien object.
        
    Returns
    ----------
    
    Author: MrR
    Date: Friday - 2020 29 May
    """
    
    
    for alien in aliens.sprites():
        if alien.checkEdges():
            changeFleetDirection(settings, aliens)
            break



def changeFleetDirection(settings, aliens):
    """
    Drop the entire fleet and change the fleet's direction.
    
    Parameters
    ----------
    settings: Object
        Game settings object.
    aliens: Object
        Group of alien object.
        
    Returns
    ----------
    
    Author: MrR
    Date: Friday - 2020 29 May
    """
    
    
    for alien in aliens.sprites():
        alien.rect.y += settings.fleetDropSpeed
    
    settings.fleetDirection *= -1



def checkBulletAlienCollision(settings, screen, scoreboard, gameStats,
                              ship, aliens, bullets):
    """
    Respond to bullet-alien collisions.
    
    Parameters
    ----------
    settings: Object
        Game settings object.
    screen: Object
        Pygame screen object.
    ship: Object
        Ship object.
    aliens: Object
        Group of alien object.
    bullets: Object
        Object of bullets.
        
    Returns
    ----------
    
    Author: MrR
    Date: Friday - 2020 29 May
    """
    
      
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if collisions:
        for aliens in collisions.values():
            gameStats.score += settings.alienPoints * len(aliens)
            scoreboard.prepareScore()
    
    # Check the fleet is empty or not
    if len(aliens) == 0:
        # Destroy existing bullets, speed up the game and create new fleet.
        bullets.empty()
        createFleet(settings=settings, screen=screen, ship=ship, aliens=aliens)
        
        settings.inreaseSpeed()



def restartGame(settings, screen, gameStats, ship, aliens, bullets):
    """
    Respond to ship being hit by alien.
    
    Parameters
    ----------
    settings: Object
        Game settings object.
    screen: Object
        Pygame screen object.
    gameStats: Object
        Game stats object.
    ship: Object
        Ship object.
    aliens: Object
        Group of alien object.
    bullets: Object
        Object of bullets.
        
    Returns
    ----------
    
    Author: MrR
    Date: Friday - 2020 29 May
    """
    
    
    if gameStats.shipLeft > 0:
        # Decrement shipLeft
        gameStats.shipLeft -= 1
        
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        
        # Create a new fleet and center the ship.
        createFleet(settings=settings, screen=screen, ship=ship, aliens=aliens)
        ship.centerShip()
    
        # Pause.
        sleep(0.5)
    else:
        gameStats.gameActive = False
        pygame.mouse.set_visible(True)



def checkAliensBottom(settings, screen, gameStats, ship, aliens, bullets):
    """
    Check if any aliens have reached the bottom of the screen..
    
    Parameters
    ----------
    settings: Object
        Game settings object.
    screen: Object
        Pygame screen object.
    gameStats: Object
        Game stats object.
    ship: Object
        Ship object.
    aliens: Object
        Group of alien object.
    bullets: Object
        Object of bullets.
        
    Returns
    ----------
    
    Author: MrR
    Date: Friday - 2020 29 May
    """
    
    
    screenRect = screen.get_rect()
    
    for alien in aliens.sprites():
        if alien.rect.bottom >= screenRect.bottom:
            # Treat this the same as if the ship got hit.
            restartGame(settings=settings, screen=screen, gameStats=gameStats,
                        ship=ship, aliens=aliens, bullets=bullets)
            break



def checkPlayButton(settings, screen, gameStats, playButton, mouseX, mouseY,
                    ship, aliens, bullets):
    """
    Start a new game when the player clicks Play.
    
    Parameters
    ----------
    settings: Object
        Game settings object.
    screen: Object
        Pygame screen object.
    gameStats: Object
        Game stats object.
    playButton: Object
        Start button object.
    mouseX:
    mouseY:
    ship: Object
        Ship object.
    aliens: Object
        Group of alien object.
    bullets: Object
        Object of bullets.
        
    Returns
    ----------
    
    Author: MrR
    Date: Monday - 2020 01 June
    Update: Wensday - 2020 10 June
    """
    
    
    buttonClicked = playButton.rect.collidepoint(mouseX, mouseY)
    
    if ((buttonClicked) and (not gameStats.gameActive)):       
        # Reset the game statistics.
        gameStats.resetStats()
        gameStats.gameActive = True
        
        # Empty the aliens and bullets lists.
        aliens.empty()
        bullets.empty()
        
        # Initialize dynamic settings
        settings.initializeDynamicSettings()
        
        # Create a new fleet and center the ship.
        createFleet(settings=settings, screen=screen, ship=ship, aliens=aliens)
        ship.centerShip()
        
        # Hide the mouse cursor
        pygame.mouse.set_visible(False)
        
    
        