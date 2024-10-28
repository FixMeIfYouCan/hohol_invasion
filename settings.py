import pygame

class Settings():
    def __init__(self):
        self.screen_width = 0
        self.screen_height = 0
        self.image = pygame.image.load('images/pole2.png')
        DEFAULT_IMAGE_SIZE = (1920, 1080)
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)     
        
        self.bg = self.image
        self.ship_speed = 10
