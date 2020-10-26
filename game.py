from character import Character
import pygame

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
grey = pygame.Color(128, 128, 128)
red = pygame.Color(255, 0, 0)
blue = pygame.Color(0, 255, 0)
green = pygame.Color(0, 0, 255)

class Game:
  def __init__(self):
    self.character = Character()
    