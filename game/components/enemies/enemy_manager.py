import pygame

from random import randint
from game.components.enemies.enemy import Enemy

class EnemyManager:
    def __init__(self):
        self.enemies = []
        
    def update(self, game):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies, game)

            if enemy.rect.colliderect(game.player.rect):
                self.enemies.remove(enemy)
                if not game.player.has_power_up:
                    game.playing = False
                    game.death_count.update()
                    pygame.time.delay(1000)
                    break

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
            
    def add_enemy(self):
        enemy_type = randint(1, 4)
        if enemy_type == 1:
            enemy = Enemy()
        else:
            speed_x = 7
            speed_y = 2
            move_x_for = [50, 120]
            enemy = Enemy(enemy_type, speed_x, speed_y, move_x_for)
            
        if len(self.enemies) < 1:
            self.enemies.append(enemy)
            
    def reset(self):
        self.enemies = []