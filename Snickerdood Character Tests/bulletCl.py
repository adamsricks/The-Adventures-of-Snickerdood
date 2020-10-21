import pygame
import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x_gun_location, y_gun_location, gun_direction):
        super().__init__()
        
        self.x = x_gun_location
        self.y = y_gun_location
        self.direction = gun_direction
        self.alive = True

        self.speed = 25

        self.radius = 5

    def advanceBullet(self, pygame):
        display_width, display_height = pygame.display.get_surface().get_size()
        """
        gun direction
        dl: down-left
        l: left
        ul: up-left
        u: up
        ur: up-right
        r: right
        dr: down-right
        d: down
        """
        if self.direction == "dl":
            self.x -= self.speed
            self.y += self.speed
        elif self.direction == "l":
            self.x -= self.speed
        elif self.direction == "ul":
            self.x -= self.speed
            self.y -= self.speed
        elif self.direction == "u":
            self.y -= self.speed
        elif self.direction == "ur":
            self.x += self.speed
            self.y -= self.speed
        elif self.direction == "r":
            self.x += self.speed
        elif self.direction == "dr":
            self.x += self.speed
            self.y += self.speed
        elif self.direction == "d":
            self.y += self.speed

        # right boundary
        if self.x > display_width - self.radius:
            self.alive = False
        # left boundary
        elif self.x < 0 + self.radius:   
            self.alive = False
        # top boundary
        if self.y < 0 + self.radius:
            self.alive = False
        # floor boundary
        elif self.y > display_height - self.radius:
            self.alive = False

        

    def drawBullet(self, surface):
        pygame.draw.circle(surface, (0,0,0), (int(self.x),int(self.y)), self.radius, 1)