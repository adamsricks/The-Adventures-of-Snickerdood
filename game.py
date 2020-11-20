from character import Character
from player import Player
from stage import Stage
from menu import Menu

import pickle
import sys

import pygame
from pygame.locals import *

# Set up movement variables.


black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
grey = pygame.Color(128, 128, 128)
red = pygame.Color(255, 0, 0)
blue = pygame.Color(0, 255, 0)
green = pygame.Color(0, 0, 255)

class Game:
    def __init__(self):
        self.screen = None
        self.clock = None

        self.screen_width = 576
        self.screen_height = 576

        self.gravity = 0

        self.player = None

        self.stage = None

        self.menu = None


    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height)) 
        self.clock = pygame.time.Clock()

        self.gravity = 0.66

        self.menu = Menu()

        # self.stage =  pickle.load( open( "Level1/Stage1", "rb" ) )
        
        

        # self.player = Player(self.gravity)
        # self.player.startPos(self.stage.startDoor.rect)



    def on_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            levelName = self.menu.getLevel(event.pos)
            if levelName != None:
                self.stage = self.stage =  pickle.load( open( levelName + "/Stage1", "rb" ) )
                self.player = Player(self.gravity)
                self.player.startPos(self.stage.startDoor.rect)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.player.jump()
            if event.key == pygame.K_d:
                self.player.moveRight = True
            if event.key == pygame.K_a:
                self.player.moveLeft = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.player.moveRight = False
            if event.key == pygame.K_a:
                self.player.moveLeft = False
                

       

    def on_loop(self):
        if self.player != None:
            self.player.onGround = False

            if self.player.scrnbtm(self.screen_height):
                self.player.setBottom(self.screen_height + 1)
            
            for platform in self.stage.platforms:
                if self.player.platTopCollide(platform.rect):
                    self.player.setBottom(platform.rect.top)
                
                if self.player.platBtmCollide(platform.rect):
                    self.player.hitHead(platform.rect.bottom )

                if self.player.platLeftCollide(platform.rect):
                    self.player.hitRight(platform.rect.left)

                if self.player.platRightCollide(platform.rect):
                    self.player.hitLeft(platform.rect.right)

            if self.player.inDoorWay(self.stage.endDoor.rect):
                self.stage =  pickle.load( open( self.stage.nextStageName, "rb" ) )
                self.player.startPos(self.stage.startDoor.rect)
                
            self.player.advance()

    def on_render(self):
        self.screen.fill((255,255,255))

        if self.stage != None:
            self.stage.draw(self.screen)
            self.player.draw(self.screen)
        else:
            self.menu.draw(self.screen)


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
