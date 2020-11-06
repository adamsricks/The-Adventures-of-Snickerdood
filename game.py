from character import Character
from player import Player
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

        self.char = None

        self.plat = None


    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height)) 
        self.clock = pygame.time.Clock()

        self.gravity = 0.33

        self.char = Player(self.gravity)

        self.plat = pygame.Rect(200,300,100,100)


    def on_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.char.jump()
            if event.key == pygame.K_d:
                self.char.moveRight = True
            if event.key == pygame.K_a:
                self.char.moveLeft = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.char.moveRight = False
            if event.key == pygame.K_a:
                self.char.moveLeft = False
                

       

    def on_loop(self):
        self.char.onGround = False
        
        if self.char.scrnbtm(self.screen_height):
            self.char.setBottom(self.screen_height + 1)

        if self.char.platTopCollide(self.plat):
            self.char.setBottom(self.plat.top)
        
        if self.char.platBtmCollide(self.plat):
            self.char.hitHead(self.plat.bottom )

        if self.char.platLeftCollide(self.plat):
            self.char.hitRight(self.plat.left)

        if self.char.platRightCollide(self.plat):
            self.char.hitLeft(self.plat.right)
            
        self.char.advance()

    def on_render(self):
        self.screen.fill((255,255,255))

        self.char.draw(self.screen)

        pygame.draw.rect(self.screen, (0, 0, 0,), self.plat)

        pygame.display.update()
        self.clock.tick(90)
        
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
