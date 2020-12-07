from floor import Floor
import pygame
from pygame.locals import *

class Stage():
    def __init__(self):
        self.platforms = []
        self.startDoor = None
        self.endDoor = None
        
        self.name = ""
        self.nextStageName = ""


    def draw(self, screen):
        for platform in self.platforms:
            platform.draw(screen)
        if self.startDoor != None:
            pygame.draw.rect(screen, (255, 255,0), self.startDoor)
            # self.startDoor.draw(screen)
        if self.endDoor != None:   
            pygame.draw.rect(screen, (255,0 ,0), self.endDoor)
            # self.endDoor.draw(screen)
