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
        self.image = pygame.image.load('images/geranka.png')
        self.image = pygame.transform.rotate(self.image, 125)
        DEFAULT_IMAGE_SIZE = (50, 75)
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = pygame.Rect(0, 0, DEFAULT_IMAGE_SIZE[0], DEFAULT_IMAGE_SIZE[1])
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
    
    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
       self.screen.blit(self.image, self.rect)