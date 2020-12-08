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






# #Bullet class
# class Bullet:
#     #Inisalizes the variables for the class
#     def __init__(self, x, y, img, facing):
#         self.x = x
#         self.y = y
#         self.img = img
#         self.facing = facing
#         self.mask = pygame.mask.from_surface(self.img)
#     #Draws the lazer
#     #Movement of the lazer
#     def move(self, vel):
#         self.x += self.facing * vel
#     #Checks to see if the lazer goes off screen
#     def off_screen(self, WIDTH):
#         return not(self.x <= WIDTH and self.x >= 0)
#     #Send data to collide function
#     def collision(self, obj):
#         return collide(self, obj)

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
    #Draws the ship
    
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

        #  for bullet in self.bullets:
        #     bullet.draw(window)
    
    def move(self, path, x, y, eyeX, eyeY):
        print("hello move")
        # if abs(y - self.y) < eyeY:
        #     if x > self.x:
        #         self.vel = 3
        #         facing = 1
        #         if self.cool_down_counter == 0:
        #             # bullet = Bullet(self.x, self.y, self.bullet_img, facing)
        #             # self.bullets.append(bullet)
        #             self.cool_down_counter = 1  
            
        #     elif y < self.y:
        #         self.vel = -3
        #         facing = -1
        #         if self.cool_down_counter == 0:
        #             # bullet = Bullet(self.x, self.y, self.bullet_img, facing)
        #             # self.bullets.append(bullet)
        #             self.cool_down_counter = 1
                    
        #     if abs(x - self.x) < eyeX:
        #         if x > self.x:
        #             self.vel = 3
        #             facing = 1
        #             if self.cool_down_counter == 0:
        #                 # bullet = Bullet(self.x, self.y, self.bullet_img, facing)
        #                 # self.bullets.append(bullet)
        #                 self.cool_down_counter = 1  
                    
        #         elif x < self.x:
        #             self.vel = -3
        #             facing = -1
        #             if self.cool_down_counter == 0:
        #                 # bullet = Bullet(self.x, self.y, self.bullet_img, facing)
        #                 # self.bullets.append(bullet)
        #                 self.cool_down_counter = 1
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
    # #Moves bullets and checks for collision
    # def move_bullets(self, vel, obj):
    #     self.cooldown()
    #     for bullet in self.bullets:
    #         bullet.move(vel)
    #         if bullet.off_screen(WIDTH):
    #             self.bullets.remove(bullet)
    #         elif bullet.collision(obj):
    #             obj.health -= 10
    #             self.bullets.remove(bullet)
    # #Cooldown for ROF
    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1
    #Fires the bullet
    def shoot(self, facing):
        if self.cool_down_counter == 0:
            # bullet = Bullet(self.x, self.y, self.bullet_img, facing)
            # self.bullets.append(bullet)
            self.cool_down_counter = 1
            #bulletS = mixer.Sound('bullet.wav')
            #bulletS.play()
    #Gets width of ship image
    def get_width(self):
        return self.creature_img_standing.get_width()
    #Gets height of ship image 
    def get_height(self):
        return self.creature_img_standing.get_height()
#Enemy class
class Enemy(Creature):
 
    #Enemy inital varibles            
    def __init__(self, x, y, end, health=100):
        super().__init__(x, y, health)
        self.creature_img_left = walkLeft
        self.creature_img_right = walkRight
        self.creature_img_standing = char
        self.bullet_img = bullet_img
        self.mask = pygame.mask.from_surface(self.creature_img_standing)
        self.path = [0, end]
        self.eyeX = 300
        self.eyeY = 200
        self.walkCount
        self.vel = random.randrange(2, 5)
                
    def move(self, x, y):
        super().move(self.path, x, y, self.eyeX, self.eyeY)                  
    #Allows enemy to shoot
    def shoot(self):
        if self.cool_down_counter == 0:
            # bullet = Bullet(self.x-20, self.y, self.bullet_img)
            # self.bullets.append(bullet)
            self.cool_down_counter = 1