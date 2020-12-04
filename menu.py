import pygame
from pygame.locals import *

class Menu():
    def __init__(self):
        font = pygame.font.Font(None, 32)
        self.level1Rect = pygame.Rect(10, 10, 140, 32)
        self.Level1txt = font.render("Level 1", True, pygame.Color('black'))
        
        


    def draw(self, screen):
        screen.blit(self.Level1txt, (self.level1Rect.x+5, self.level1Rect.y+5))
        pygame.draw.rect(screen, pygame.Color('white'), self.level1Rect, 2)

    def getLevel(self, pos):
        if self.level1Rect.collidepoint(pos):
            return "World 1"
        
        return None
