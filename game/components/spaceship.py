import pygame

from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, SHIP_WIDTH, SHIP_HEIGHT, DEFAULT_TYPE
from game.components.bullets.bullet import Bullet


class Spaceship(Sprite):
    X_POS = (SCREEN_WIDTH // 2) - SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 10
    
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (SHIP_WIDTH, SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.power_time_up = 0

    def update(self, user_input, game):
        if user_input[pygame.K_LEFT]:
            self.move_left()               
        if user_input[pygame.K_RIGHT]:
            self.move_right()
        if user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_DOWN]:
            self.move_down()
        if user_input[pygame.K_SPACE]:
            self.shoot(game)

            
    def shoot(self, game)   :
        bullet = Bullet(self)
        game.bullet_manager.add_bullet(bullet)
        
                
    def move_left(self):
        self.rect.x -= self.SHIP_SPEED
        if self.rect.x < 0:
            self.rect.x = SCREEN_WIDTH - SHIP_WIDTH
            
    def move_right(self):
        self.rect.x += self.SHIP_SPEED
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = 0
            
    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= self.SHIP_SPEED
            
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT -70:
            self.rect.y += self.SHIP_SPEED        
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def set_image(self, size = (40, 60), image = SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)