import pygame
from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu:
  HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
  HALF_SCREEN__WIDTH = SCREEN_WIDTH // 2

  def __init__(self, screen):
    screen.fill((255, 255, 255))
    self.font = pygame.font.Font(FONT_STYLE, 30)

  def update(self, game):
    pygame.display.update()
    self.handle_events_on_menu(game)

  def draw(self, screen, message, x = HALF_SCREEN__WIDTH, y = HALF_SCREEN_HEIGHT, color = (0, 0, 0)):
    text = self.font.render(message, True, color)
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    screen.blit(text, text_rect)

  def handle_events_on_menu(self, game):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        game.running = False
        game.playing = False
      elif event.type == pygame.KEYDOWN:
        game.run()

  def reset_screen_color(self, screen):
    screen.fill((255, 255, 255))

  def update_message(self, message):
    self.text = self.font.render(message, True, (0, 0, 0))
    self.text_rect = self.text.get_rect()
    self.text_rect.center = (self.half_screen_width, self.half_screen_height)
        