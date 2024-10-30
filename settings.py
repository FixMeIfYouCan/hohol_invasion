import pygame

class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bullet_width = 10
        self.bullet_height = 30
        self.bullet_image = pygame.image.load('images/pole2.png')
        DEFAULT_BULLET_SIZE = (self.bullet_height, self.bullet_width)
        self.image = pygame.transform.scale(self.bullet_image, DEFAULT_BULLET_SIZE)   

        self.image = pygame.image.load('images/pole2.png')
        DEFAULT_IMAGE_SIZE = (1200, 800)
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)     
        
        self.bg = self.image
        self.ship_speed = 10
        self.bullet_speed = 20