import pygame
import character as char

class Player1(char.Character):
    def __init__(self, gravity):
        super().__init__(gravity)

        # speed cap for x
        self.maxSpeed = 3
        # constant that's added to the momentum
        self.accX = .3
        
        self.movementx = 0
        self.movementy = 0

        # like gravity but for the x axis
        self.drag = .17

        # speed cap for y
        self.maxFallSpeed = 7

        self.direction = "r"

        self.alive = True

        # This will update to give the end of the gun so bullet can grab it when necessary
        self.gunPoint = self.rect.center

        self.jump_height = 6

        self.health = 200

    def startPos(self, rect):
        self.rect.bottom = rect.bottom
        self.rect.left = rect.left

    def jump(self):
      if self.onGround:
        self.onGround = False
        self.rect.bottom = self.rect.bottom - 1
        self.movementy = 0
        self.movementy -= self.jump_height

    def changeDirection(self):
        if self.movementx > 0:
            self.direction = 'r'
        elif self.movementx < 0:
            self.direction = 'l'

    def advance(self):
        self.changeDirection()
        if self.direction == "r":
            self.gunPoint = (self.rect.center[0], self.rect.center[1])
        else:
            self.gunPoint = (self.rect.center[0], self.rect.center[1])

        if not self.onGround:
            if self.movementy >= self.maxFallSpeed:
                self.movementy = self.maxFallSpeed
                self.rect.centery += self.movementy
            else:
                self.movementy += self.gravity
                self.rect.centery += self.movementy
        else:
            self.movementy = 0

        if self.moveRight:
            # only adds momentum if not past screen boundary
            if self.rect.right < 576:
                if self.movementx <= self.maxSpeed:
                    self.movementx += self.accX
                #self.rect.centerx += self.movementx
            else:
                self.movementx = 0
                self.rect.right = 576
        elif not self.moveLeft:
            if self.movementx >= self.drag:
                self.movementx -= self.drag

        if self.moveLeft:
            # only adds momentum if not past screen boundary
            if self.rect.left > 0:
                if self.movementx >= -self.maxSpeed:
                    self.movementx -= self.accX
                #self.rect.centerx += self.movementx
            else:
                self.movementx = 0
                self.rect.left = 0
        elif not self.moveRight:
            if self.movementx <= -self.drag:
                self.movementx += self.drag

        #print(f"movementx before = {self.movementx}")
        if abs(self.movementx) < self.drag:
            self.movementx = 0
    
        # actually moves the character
        self.rect.centerx += self.movementx
        #print(f"movementx after = {self.movementx}")

    def draw(self, screen):
        if self.direction == "r":
          screen.blit(self.surface, self.rect)
        else:
          screen.blit(pygame.transform.flip(self.surface, True, False), self.rect)
