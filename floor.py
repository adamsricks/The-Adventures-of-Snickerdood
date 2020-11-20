import pygame
from pygame.locals import *

class Floor():
    def __init__(self, point1 = (0, 0), point2 = (0, 0)):
        
        self.color = (0, 0, 0,)
        self.rect = pygame.Rect(point1, point2)
        self.rect.normalize()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    