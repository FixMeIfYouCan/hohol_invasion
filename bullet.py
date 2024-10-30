import pygame
from pygame.sprite import Sprite
from settings import Settings

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.settings = Settings()
        self.screen_rect = ai_game.screen.get_rect()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/ship2.png')
        DEFAULT_IMAGE_SIZE = (20,25)
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.y = float(self.rect.y)
    
    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
       self.screen.blit(self.image, self.rect)