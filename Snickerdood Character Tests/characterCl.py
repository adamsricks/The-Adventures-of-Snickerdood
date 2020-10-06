import pygame

class Character():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def drawChar(self, surface, x, y):
        self.x = x
        self.y = y
        pygame.draw.circle(surface, (0,0,0), (x,y), 45, 1)