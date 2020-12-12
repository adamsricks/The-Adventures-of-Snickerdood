import pygame
from pygame.locals import *

class Menu():
    def __init__(self):
        font = pygame.font.Font(None, 32)
        self.level1Rect = pygame.Rect(10, 10, 140, 32)
        self.level1Name = "name"
        self.Level1txt = font.render(self.level1Name, True, pygame.Color('black'))
        self.level2Rect = pygame.Rect(10, 42, 140, 32)
        self.level2Name = "wk 13 demo"
        self.Level2txt = font.render(self.level2Name, True, pygame.Color('black'))
        self.level3Rect = pygame.Rect(10, 74, 140, 32)
        self.level3Name = "spuddy"
        self.Level3txt = font.render(self.level3Name, True, pygame.Color('black'))
        self.level4Rect = pygame.Rect(10, 106, 140, 32)
        self.level4Name = "CS246"
        self.Level4txt = font.render(self.level4Name, True, pygame.Color('black'))
        self.level5Rect = pygame.Rect(10, 138, 140, 32)
        self.level5Name = "Test World 3"
        self.Level5txt = font.render(self.level5Name, True, pygame.Color('black'))
        self.level6Rect = pygame.Rect(10, 170, 140, 32)
        self.level6Name = "Demo World"
        self.Level6txt = font.render(self.level6Name, True, pygame.Color('black'))
        self.level7Rect = pygame.Rect(10, 202, 140, 32)
        self.level7Name = "Level 7"
        self.Level7txt = font.render(self.level7Name, True, pygame.Color('black'))
        self.level8Rect = pygame.Rect(10, 234, 140, 32)
        self.level8Name = "World 2"
        self.Level8txt = font.render(self.level8Name, True, pygame.Color('black'))

    def draw(self, screen):
        screen.blit(self.Level1txt, (self.level1Rect.x+5, self.level1Rect.y+5))
        pygame.draw.rect(screen, pygame.Color('white'), self.level1Rect, 2)
        screen.blit(self.Level2txt, (self.level2Rect.x+5, self.level2Rect.y+5))
        pygame.draw.rect(screen, pygame.Color('white'), self.level2Rect, 2)
        screen.blit(self.Level3txt, (self.level3Rect.x+5, self.level3Rect.y+5))
        pygame.draw.rect(screen, pygame.Color('white'), self.level3Rect, 2)
        screen.blit(self.Level4txt, (self.level4Rect.x+5, self.level4Rect.y+5))
        pygame.draw.rect(screen, pygame.Color('white'), self.level4Rect, 2)
        screen.blit(self.Level5txt, (self.level5Rect.x+5, self.level5Rect.y+5))
        pygame.draw.rect(screen, pygame.Color('white'), self.level5Rect, 2)
        screen.blit(self.Level6txt, (self.level6Rect.x+5, self.level6Rect.y+5))
        pygame.draw.rect(screen, pygame.Color('white'), self.level6Rect, 2)
        screen.blit(self.Level7txt, (self.level7Rect.x+5, self.level7Rect.y+5))
        pygame.draw.rect(screen, pygame.Color('white'), self.level7Rect, 2)
        screen.blit(self.Level8txt, (self.level8Rect.x+5, self.level8Rect.y+5))
        pygame.draw.rect(screen, pygame.Color('white'), self.level8Rect, 2)

    def getLevel(self, pos):
        if self.level1Rect.collidepoint(pos):
            return self.level1Name
        if self.level2Rect.collidepoint(pos):
            return self.level2Name
        if self.level3Rect.collidepoint(pos):
            return self.level3Name
        if self.level4Rect.collidepoint(pos):
            return self.level4Name
        if self.level5Rect.collidepoint(pos):
            return self.level5Name
        if self.level6Rect.collidepoint(pos):
            return self.level6Name
        if self.level7Rect.collidepoint(pos):
            return self.level7Name
        if self.level8Rect.collidepoint(pos):
            return self.level8Name
        
        return None
