from floor import Floor
# from newEnemy import Enemy
import pygame
from pygame.locals import *

class Stage():
    def __init__(self):
        self.platforms = []
        # self.enemy = Enemy(100, 100, 400)
        self.startDoor = pygame.Rect(10, 10, 40, 50)
        self.endDoor = pygame.Rect(200, 300, 40, 50)
        self.name = ""
        self.nextStageName = ""

    def draw(self, screen):
        # self.enemy.draw(screen)
        for platform in self.platforms:
            platform.draw(screen)
        if self.startDoor != None:
            pygame.draw.rect(screen, (255, 255,0), self.startDoor)
            # self.startDoor.draw(screen)
        if self.endDoor != None:   
            pygame.draw.rect(screen, (255,0 ,0), self.endDoor)
            # self.endDoor.draw(screen)
       
    # def run(self):
    #     self.enemy.append(self.enemy)
    #     for enemyies in enemy[:]:
    #         enemy.move(x, y)
