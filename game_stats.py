class GameStats():
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.invincible = False
        self.invincible_start_time = 0
    
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.invincible = False
