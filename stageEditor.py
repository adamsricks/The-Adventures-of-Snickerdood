from floor import Floor
from newEnemy import Enemy

import pygame
from pygame.locals import *

class StageEditor():
    def __init__(self):
        self.keyPress = ""

        self.start = (0, 0)
        self.size = (0, 0)
        self.end = (0, 0)
        self.drawing = False

        self.levelName = ""
        self.stageCounter = 1



    def draw(self, screen):
        # self.size = self.end[0]-self.start[0], self.end[1]-self.start[1]
        # pygame.draw.rect(screen, (0, 0, 0), (self.start, self.size), 1)

        self.drawTextbox(screen)

       


    def onMouseDown(self, pos):
        if self.keyPress == "floor":
            self.start = pos

            self.drawing = True
        

    def onMouseUp(self, pos):
        if self.keyPress == "floor":

            self.drawing = False
        if self.keyPress == "door1" or self.keyPress == "door2" or self.keyPress == "enemy":
            self.start = pos


    def onMouseMotion(self, pos):
        if self.keyPress == "floor":
            self.end = pos

    def addPlatform(self):
        return Floor(self.start)
    
    def addDoor(self):
        
        door = pygame.Rect(self.start[0], self.start[1], 40, 50)
        # if self.keyPress == "door1":
        #     door.color = (255, 255,0)
        # else:
        #     door.color = (255,0 ,0)
        return door

    def addBaddie(self):
        pass

    def drawTextbox(self, screen):
        font = pygame.font.Font(None, 32)
        input_box = pygame.Rect(10, 10, 140, 32)
        txt_surface = font.render(self.levelName, True, pygame.Color('lightskyblue3'))
        
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, pygame.Color('lightskyblue3'), input_box, 2)
    
    def addEnemy(self):
        return Enemy(self.start[0], self.start[1])
