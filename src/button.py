import pygame


class Button:
    """
    Buttons class.
    """
    
    def __init__(self, screen, message):
        """
        Initialize button attributes.
        :param screen: game screen
        :param message: button message
        :return:
        """

        self.message = message

        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        
        # Set the dimensions and properties of the button.
        self.width, self.height = 75, 50
        self.button_color = (0, 255, 0)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 36)
        
        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # The button message needs to be prepared only once.
        self.__prepare_message()

    def __prepare_message(self):
        """
        Turn message into a rendered image and center text on the button.
        :return:
        """
        
        self.message_image = self.font.render(self.message, True, self.text_color,
                                              self.button_color)

        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center

    def draw_button(self):
        """
        Draw blank button and then draw message.
        :return:
        """
        
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.message_image, self.message_image_rect)
