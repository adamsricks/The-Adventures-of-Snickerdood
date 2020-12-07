import pygame
import character as char

class Player1(char.Character):
    def __init__(self, gravity):
        super().__init__(gravity)

        

        self.idleList = [pygame.image.load("character pic/Woodcutter_idle/Woodcutter_idle1.png").convert_alpha(), pygame.image.load("character pic/Woodcutter_idle/Woodcutter_idle2.png").convert_alpha(), pygame.image.load("character pic/Woodcutter_idle/Woodcutter_idle3.png").convert_alpha(), pygame.image.load("character pic/Woodcutter_idle/Woodcutter_idle4.png").convert_alpha()]
        self.runList = [pygame.image.load("character pic/Woodcutter_run/Woodcutter_run1.png").convert_alpha(), pygame.image.load("character pic/Woodcutter_run/Woodcutter_run2.png").convert_alpha(), pygame.image.load("character pic/Woodcutter_run/Woodcutter_run3.png").convert_alpha(), pygame.image.load("character pic/Woodcutter_run/Woodcutter_run4.png").convert_alpha(), pygame.image.load("character pic/Woodcutter_run/Woodcutter_run5.png").convert_alpha(), pygame.image.load("character pic/Woodcutter_run/Woodcutter_run6.png").convert_alpha()]
        self.jumpList = [pygame.image.load("character pic/Woodcutter_jump/Woodcutter_jump.png").convert_alpha(), pygame.image.load("character pic/Woodcutter_jump/Woodcutter_jump1.png").convert_alpha(), pygame.image.load("character pic/Woodcutter_jump/Woodcutter_jump2.png").convert_alpha(), pygame.image.load("character pic/Woodcutter_jump/Woodcutter_jump3.png").convert_alpha(), pygame.image.load("character pic/Woodcutter_jump/Woodcutter_jump4.png").convert_alpha(), pygame.image.load("character pic/Woodcutter_jump/Woodcutter_jump5.png").convert_alpha()]


        self.drawList = self.idleList

        self.animatedIndex = 0
        self.surface = self.drawList[self.animatedIndex]
        self.rect = self.surface.get_rect(center = (self.rect.x, self.rect.y))

        self.maxSpeed = 3
        self.accX = .5

        self.animation = "i"
        self.direction = "r"

        self.alive = True

        # This will update to give the end of the gun so bullet can grab it when necessary
        self.gunPoint = self.rect.center

        self.jump_height = 3

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

        if not self.moveRight and not self.moveLeft:
            if self.animation != "i":
                self.animation = "i"
                self.drawList = self.idleList
                self.animatedIndex = 0
        
        if self.moveRight or self.moveLeft:
            if self.animation != "r":
                self.animation = "r"
                self.drawList = self.runList
                self.animatedIndex = 0
        if self.movementy > 0:
            self.animation = "falling"
            self.animatedIndex = 0
            self.drawList = self.jumpList[4:]
        
        if self.movementy < 0:
            self.animation = "up"
            self.animatedIndex = 0
            self.drawList = self.jumpList[:5]

            

        # print(self.movementy)

    def draw(self, screen):
        if self.direction == "r":
          screen.blit(self.surface, self.rect)
        else:
          screen.blit(pygame.transform.flip(self.surface, True, False), self.rect)
    
    def nextAnimation(self):
        if self.animation != "falling":
            listLen = len(self.drawList)-1
            
            if self.animatedIndex != listLen:
                self.animatedIndex += 1
            else:
                self.animatedIndex = 0

        self.surface = self.drawList[self.animatedIndex]
        # self.rect = self.surface.get_rect(bottom = self.rect.bottom)
    
