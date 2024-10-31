import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load('images/hohol.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        DEFAULT_IMAGE_SIZE = (120, 150)
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = pygame.Rect(0, 0, DEFAULT_IMAGE_SIZE[0], DEFAULT_IMAGE_SIZE[1])