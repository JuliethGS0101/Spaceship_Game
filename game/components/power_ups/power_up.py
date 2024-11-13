import pygame
from random import randint
from pygame.sprite import Sprite

from game.utils.constants import SCREEN_HEIGHT


class PowerUp(Sprite):

    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = randint(100, SCREEN_HEIGHT - 100)
        self.rect.y = 0
        self.start_time = 0

    def update(self, game_speed, power_ups):
        self.rect.y += game_speed
        if self.rect.y >= SCREEN_HEIGHT:
            power_ups.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)