import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height), pygame.RESIZABLE)
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.clock = pygame.time.Clock()
        self.FPS = 60
    
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

        
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
            
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
            
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
        
        self.clock.tick(self.FPS)

    
    def _update_screen(self):
        self.screen.blit(self.settings.bg, (0, 0))
        self.ship.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()