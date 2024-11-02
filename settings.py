import pygame

class Settings():
    def __init__(self):
        self.screen_width = 1920
        self.screen_height = 1080

        self.image = pygame.image.load('images/pole2.png')
        DEFAULT_IMAGE_SIZE = (1920, 1080)
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)     
        
        self.bg = self.image
        self.ship_speed = 10
        self.bullet_speed = 10
        self.bullet_allowed = 3

        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1