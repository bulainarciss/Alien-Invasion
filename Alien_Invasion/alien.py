import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = self.settings.alien_image
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width/2
        self.rect.y = self.rect.height/2
        self.x = float(self.rect.x)
        self.direction = 1

    def update(self):
        self.x += self.settings.alien_speed * self.direction
        self.rect.x = self.x

    def check_edge(self):
        self.screen_rect = self.screen.get_rect()
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True