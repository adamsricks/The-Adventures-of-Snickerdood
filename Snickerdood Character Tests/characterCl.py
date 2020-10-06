import pygame

class Character():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def drawChar(self, surface, x, y):
        self.x = int(x)
        self.y = int(y)
        pygame.draw.circle(surface, (0,0,0), (self.x,self.y), 45, 1)