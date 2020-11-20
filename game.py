from character import Character
from player import Player
from bullet import Bullet
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

        self.bullet_list = pygame.sprite.Group()

        self.plats = None


    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height)) 
        self.clock = pygame.time.Clock()

        self.gravity = 0.66

        self.player = Player(self.gravity)
        self.player.alive = True

        self.plats = [pygame.Rect(0,450,500,50), pygame.Rect(76,350,500,50), pygame.Rect(0,250,500,50), pygame.Rect(76,150,500,50)]


    def on_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.player.jump()
            if event.key == pygame.K_d:
                self.player.moveRight = True
            if event.key == pygame.K_a:
                self.player.moveLeft = True
            if event.key == pygame.K_UP:
                self.player.jump()
            if event.key == pygame.K_RIGHT:
                self.player.moveRight = True
            if event.key == pygame.K_LEFT:
                self.player.moveLeft = True
            if event.key == pygame.K_SPACE:
                self.shootBullet()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.player.moveRight = False
            if event.key == pygame.K_a:
                self.player.moveLeft = False
            if event.key == pygame.K_RIGHT:
                self.player.moveRight = False
            if event.key == pygame.K_LEFT:
                self.player.moveLeft = False
                

    def shootBullet(self):
        # This will add a bullet to the bullet list and pass the bullet the end of the gun
        # and the direction that the character is facing
        bullet = Bullet(self.player.direction, self.player.gunPoint)
        bullet.add(self.bullet_list)

    def on_loop(self):
        self.player.onGround = False
        for platform in self.plats:
            if self.player.scrnbtm(self.screen_height):
                self.player.setBottom(self.screen_height + 1)

            if self.player.platTopCollide(platform):
                self.player.setBottom(platform.top)
            
            if self.player.platBtmCollide(platform):
                self.player.hitHead(platform.bottom )

            if self.player.platLeftCollide(platform):
                self.player.hitRight(platform.left)

            if self.player.platRightCollide(platform):
                self.player.hitLeft(platform.right)
            
        self.player.advance()

        for each in self.bullet_list:
            if each.x < 0 or each.x > self.screen_width:
                each.kill()
            else:
                each.advance()
            

    def on_render(self):
        self.screen.fill((255,255,255))

        self.player.draw(self.screen)

        for each in self.bullet_list:
            each.draw(self.screen)

        for platform in self.plats:
            pygame.draw.rect(self.screen, (0, 0, 0,), platform)

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
