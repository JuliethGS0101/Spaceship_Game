import pygame


from random import randint
from pygame.sprite import Sprite

from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_3, ENEMY_4,  SHIP_WIDTH, SHIP_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT
from game.components.bullets.bullet import Bullet

class Enemy(Sprite):
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 1
    MOV_X = {0: 'left', 1: 'right'}
    IMAGE = {1: ENEMY_1, 2: ENEMY_2, 3: ENEMY_3, 4: ENEMY_4}
    def __init__(self, image_index = 1, speed_x = SPEED_X, speed_y = SPEED_Y, move_x_for = [30, 100]):
        self.image = self.IMAGE[image_index]
        self.image = pygame.transform.scale(self.image, (SHIP_WIDTH, SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, SCREEN_WIDTH)
        self.rect.y = self.Y_POS
        
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.movement_x = self.MOV_X[randint(0, 1)]
        self.move_x_for = randint(move_x_for[0], move_x_for[1])      
        self.step = 0
        self.type = 'enemy'
        self.shooting_time = randint(30, 50)

    def update(self, enemies, game):
        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager)


        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x
        self.change_movement_x()
        
        if self.rect.y >= SCREEN_HEIGHT:
            enemies.remove(self)

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += randint(20, 50)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def change_movement_x(self):
        self.step += 1
        if (self.step >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - SHIP_WIDTH):
            self.movement_x = 'left'
            self.step = 0 
            
        elif (self.step >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10):
            self.movement_x = 'right'
            self.step = 0 