"""
Author: Bryson Rogers
Class: Platform
    A onscreen object that provides surface for 
    player and baddies to move on.
"""
import pygame
from game import grey

class Platform:
  def __init__(self, x, y, width, height):
      self.platform = pygame.Rect.Rect(x, y, width, height)

  def draw(self, surface):
      pygame.draw.rect(surface, grey, self.platform)