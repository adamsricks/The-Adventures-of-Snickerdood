import pygame
from pygame.locals import *
from animation import Animation

class Floor():
    def __init__(self, point1 = (0, 0)):      
        self.center = point1
        self.rect = Animation.log.get_rect(center = self.center)

    def draw(self, screen):
        screen.blit(Animation.log, self.rect)


    