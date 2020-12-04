import pygame
import character as char

class Player1(char.Character):
    def __init__(self, gravity):
        super().__init__(gravity)

        self.maxSpeed = 4
        self.accX = .6

        # these are momentum variables, and are always added to the position of the player character
        self.movementx = 0
        self.movementy = 0

        # this is the positive momentum, always added or subtracted to the movement variables
        self.momentumx = 0
        self.momentumy = 0

        self.maxFallSpeed = 5

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
        super().advance()
        self.changeDirection()
        if self.direction == "r":
            self.gunPoint = (self.rect.center[0], self.rect.center[1])
        else:
            self.gunPoint = (self.rect.center[0], self.rect.center[1])

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

    def draw(self, screen):
        if self.direction == "r":
          screen.blit(self.surface, self.rect)
        else:
          screen.blit(pygame.transform.flip(self.surface, True, False), self.rect)
