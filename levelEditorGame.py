from stage import Stage
from stageEditor import StageEditor


import pickle
import sys
import os

import pygame
from pygame.locals import *

# pickle.dump( tree, open( "save.p", "wb" ) )
# Set up movement variables.


black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
grey = pygame.Color(128, 128, 128)
red = pygame.Color(255, 0, 0)
blue = pygame.Color(0, 255, 0)
green = pygame.Color(0, 0, 255)

class LevelEditorGame:
    def __init__(self):
        self.screen = None
        self.clock = None

        self.screen_width = 576
        self.screen_height = 576

        self.SE = None

        self.stage = None


    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height)) 
        self.clock = pygame.time.Clock()

        self.SE = StageEditor()

        self.stage = Stage()


    def on_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == MOUSEBUTTONDOWN:
            self.SE.onMouseDown(event.pos)

            
        if event.type == MOUSEBUTTONUP:
            self.SE.onMouseUp(event.pos)
            if self.SE.keyPress == "floor":
                self.stage.platforms.append(self.SE.addPlatform())
            
            if self.SE.keyPress == "door1":
                self.stage.startDoor = self.SE.addDoor()

            if self.SE.keyPress == "door2":
                self.stage.endDoor = self.SE.addDoor()
            if self.SE.keyPress == "enemy":
                self.stage.enemies.append(self.SE.addEnemy())

        # if event.type == MOUSEMOTION and self.SE.drawing:
        #     self.SE.onMouseMotion(event.pos)
            
        
        if event.type == KEYDOWN:
            if event.key == pygame.K_RETURN:
                    self.SE.keyPress = ""
            if self.SE.keyPress != "name":
                if event.key == pygame.K_s:
                    self.stage.nextStageName = self.SE.levelName + "/Stage" + str(self.SE.stageCounter + 1)

                    if not os.path.exists(self.SE.levelName ):
                        os.makedirs(self.SE.levelName )

                    pickle.dump( self.stage, open(self.SE.levelName + "/Stage" + str(self.SE.stageCounter), "wb"))
                    
                    self.SE.stageCounter += 1
                    self.stage = Stage()
                    self.stage.nextStageName = self.SE.levelName + "/Stage" + str(self.SE.stageCounter)
                    self.SE.keyPress = ""
                    self.SE.start = (0, 0)
                    self.SE.end = (0, 0)

                    # self.stage.
                if event.key == pygame.K_f:
                    self.SE.keyPress = "floor"
                if event.key == pygame.K_d:
                    if self.SE.keyPress != "door1":
                        self.SE.keyPress = "door1"
                    else:
                        self.SE.keyPress = "door2"

                if event.key == pygame.K_n:
                    self.SE.keyPress = "name"
                if event.key == pygame.K_e:
                    self.SE.keyPress = "enemy"

                if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    if self.SE.keyPress == "floor":
                        self.stage.platforms.pop()
                    if self.SE.keyPress == "enemy":
                        self.stage.enemies.pop()
                
            else:
                if event.key == pygame.K_BACKSPACE:
                        self.SE.levelName = self.SE.levelName[:-1]
                else:
                    self.SE.levelName +=event.unicode

            
                
                

       

    def on_loop(self):
        self.stage.run()

    def on_render(self):
        self.screen.fill((255,255,255))

        self.stage.draw(self.screen)

        self.SE.draw(self.screen)

        pygame.display.update()
        self.clock.tick(120)
        
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            sys.exit()
 
        while True:
            for event in pygame.event.get():
                self.on_event(event)
            
            self.on_loop()
            self.on_render()
        self.on_cleanup()
