import pygame
import os
import time
import random
from character import Character
from pygame.locals import *
from pygame import mixer
from animation import Animation



bullet_img = pygame.image.load(os.path.join('pics','bullet-1.bmp'))


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

        if self.walkCount + 1 >= 18:
            self.walkCount = 0
        if self.vel > 0:
            window.blit(Animation.walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            window.blit(Animation.walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        
    
    def move(self, path, x, y, eyeX, eyeY):
    
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
    

#Enemy class
class Enemy(Creature):
 
    #Enemy inital varibles            
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        # self.creature_img_left = walkLeft
        # self.creature_img_right = walkRight


        self.path = [x - 30, x + 30]
        self.eyeX = 300
        self.eyeY = 200
        self.walkCount
        self.vel = random.randrange(1, 2)
        self.rect = Animation.walkRight[0].get_rect(bottom = self.x, right = self.y)
                
    def move(self, x, y):
        super().move(self.path, x, y, self.eyeX, self.eyeY)                  
    
    def collision(self, objPoint):

        # if self.rect.collidepoint(objPoint):
            
        return self.rect.collidepoint(objPoint)
    def draw(self, window):
        super().draw(window)
        self.rect.topleft = (self.x, self.y)
        # pygame.draw.rect(window, (255, 0, 0), self.rect) 