import pygame
from pygame.locals import *

class Floor():
    def __init__(self, point1 = (0, 0)):      
        self.center = point1
        self.rect = None
    def draw(self, screen):
        surface = pygame.image.load("character pic/log_platform.png").convert_alpha()

        if self.rect == None:
            self.rect = surface.get_rect(center = self.center)

        screen.blit(surface, self.rect)


    