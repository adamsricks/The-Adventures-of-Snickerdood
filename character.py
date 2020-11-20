import pygame
from pygame.locals import *

class Character:
    def __init__(self, gravity):
        self.surface = pygame.image.load("Woodcutter.png").convert_alpha()
        
        self.rect = self.surface.get_rect(center = (100, 576))
        
        self.movementy = 0
        self.movementx = 0

        self.moveLeft = False
        self.moveRight = False

        self.onGround = False

        self.gravity = gravity

        self.maxSpeed = 4
        self.accX = .15


    def advance(self):
      
      if not self.onGround:
        self.movementy += self.gravity
        self.rect.centery += self.movementy
      else:
        self.movementy = 0
        

      if self.moveRight:
        if self.movementx < 0:
          self.movementx = 0
        if self.rect.right < 576:
          
          if self.movementx <= self.maxSpeed:
            self.movementx += self.accX
          self.rect.centerx += self.movementx
        else:
          self.movementx = 0
          self.rect.right = 576

      if self.moveLeft:
        if self.movementx > 0:
          self.movementx = 0
        if self.rect.left > 0:
          
          if self.movementx >= -self.maxSpeed:
            self.movementx -= self.accX
          self.rect.centerx += self.movementx
        else:
          self.movementx = 0
          self.rect.left = 0

    def jump(self):
      if self.onGround:
        self.onGround = False
        self.rect.bottom = self.rect.bottom - 1
        self.movementy = 0
        self.movementy -= 12
    
    def platTopCollide(self, platform):
      return platform.collidepoint(self.rect.midbottom)
    
    def platBtmCollide(self, platform):
      return platform.collidepoint(self.rect.midtop)

    def platLeftCollide(self, platform):
      return platform.collidepoint(self.rect.midright)
    
    def platRightCollide(self, platform):
      return platform.collidepoint(self.rect.midleft)

    def scrnbtm(self, sceenbtm):
      return self.rect.bottom > sceenbtm

    def setBottom(self, top):
      self.rect.bottom = top
      self.onGround = True

    def hitHead(self, btm):
      self.rect.top = btm
      self.movementy = 0

    def hitRight(self, left):
      self.rect.right = left
      self.movementx = 0
    
    def hitLeft(self, right):
      self.rect.left = right
      self.movementx = 0
