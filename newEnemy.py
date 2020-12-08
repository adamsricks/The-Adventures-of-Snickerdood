import pygame
import os
import time
import random
from character import Character
from pygame.locals import *
from pygame import mixer

pygame.font.init()
pygame.init()

bullet_img = pygame.image.load(os.path.join('pics','bullet-1.bmp'))

walkRight = [pygame.image.load('TestGames/R1E.png'), pygame.image.load('TestGames/R2E.png'), pygame.image.load('TestGames/R3E.png'), pygame.image.load('TestGames/R4E.png'), pygame.image.load('TestGames/R5E.png'), pygame.image.load('TestGames/R6E.png'), pygame.image.load('TestGames/R7E.png'), pygame.image.load('TestGames/R8E.png'), pygame.image.load('TestGames/R9E.png'), pygame.image.load('TestGames/R10E.png'), pygame.image.load('TestGames/R11E.png')]
walkLeft = [pygame.image.load('TestGames/L1E.png'), pygame.image.load('TestGames/L2E.png'), pygame.image.load('TestGames/L3E.png'), pygame.image.load('TestGames/L4E.png'), pygame.image.load('TestGames/L5E.png'), pygame.image.load('TestGames/L6E.png'), pygame.image.load('TestGames/L7E.png'), pygame.image.load('TestGames/L8E.png'), pygame.image.load('TestGames/L9E.png'), pygame.image.load('TestGames/L10E.png'), pygame.image.load('TestGames/L11E.png')]

#Creature class
class Creature:
    COOLDOWN = 10 #Cool down for ROF
    #Creature inishall variables
    def __init__(self, x, y, walkCount = 0, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.creature_img_left = None
        self.creature_img_right = None
        self.creature_img_standing = None
        self.bullet_img = None
        self.bullets = []
        self.cool_down_counter = 0
        self.walkCount = walkCount
        self.vel = None
    
    def draw(self, window):
        print("draw")
        if self.walkCount + 1 >= 18:
            self.walkCount = 0
        if self.vel > 0:
            window.blit(self.creature_img_right[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            window.blit(self.creature_img_left[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
    
    def move(self, path, x, y, eyeX, eyeY):
        print("hello move")
        if self.vel > 0:
            if self.x < path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            
            if self.x > path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1
    #Fires the bullet
    def shoot(self, facing):
        if self.cool_down_counter == 0:
    def get_width(self):
        return self.creature_img_standing.get_width()
    #Gets height of ship image 
    def get_height(self):
        return self.creature_img_standing.get_height()
#Enemy class
class Enemy(Creature):
 
    #Enemy inital varibles            
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.creature_img_left = walkLeft
        self.creature_img_right = walkRight
        self.creature_img_standing = char
        self.bullet_img = bullet_img
        self.mask = pygame.mask.from_surface(self.creature_img_standing)
        self.path = [x - 30, x + 30]
        self.eyeX = 300
        self.eyeY = 200
        self.walkCount
        self.vel = random.randrange(1, 2)
                
    def move(self, x, y):
        super().move(self.path, x, y, self.eyeX, self.eyeY)                  
   