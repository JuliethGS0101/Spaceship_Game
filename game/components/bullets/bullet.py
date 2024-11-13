import pygame

from pygame.sprite import Sprite
from game.utils.constants import BULLET, BULLET_ENEMY, SCREEN_HEIGHT

class Bullet(Sprite):
    
    BULLET_SIZE = pygame.transform.scale(BULLET, (10, 20))
    BULLET_SIZE_ENEMY = pygame.transform.scale(BULLET_ENEMY,(9, 32))
    BULLETS = {'player': BULLET_SIZE, 'enemy': BULLET_SIZE_ENEMY}
    SPEED = 20

    def __init__(self, spaceship):
       self.image = self.BULLETS[spaceship.type]
       self.rect = self.image.get_rect()
       self.rect.center = spaceship.rect.center
       self.owner = spaceship.type

    def update(self, bullets):
        if self.owner == 'enemy':
            self.rect.y += self.SPEED
        else:
            self.rect.y -= self.SPEED

        if self.rect.y < 0 or self.rect.y >= SCREEN_HEIGHT:
            bullets.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)