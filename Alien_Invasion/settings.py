import pygame


class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = (0, 0, 0)
        self.bg_image = pygame.image.load('images/background.bmp')
        self.bg_image = pygame.transform.scale(self.bg_image, (1360, 768))
        self.ship_image = pygame.image.load('images/spaceship.bmp')
        self.ship_speed = 6
        self.ship_limit = 3
        self.bullet_speed = 6
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = (212, 175, 55)
        self.bl_image = pygame.image.load('images/bullet.bmp')
        self.bullets_allowed = 3
        self.alien_image = pygame.image.load('images/alien.bmp')
        self.alien_speed = 1.0
        self.fleet_drop_speed = 100
        self.fleet_direction = 1
        self.text_bg_color = (31, 33, 90)
        self.speedup_scale = 1.25
        self.initialize_dynamic_settings()
        self.alien_points = 10

    def initialize_dynamic_settings(self):
        self.ship_speed = 6
        self.bullet_speed = 3.5
        self.alien_speed = 1.0
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.speedup_scale)
