import pygame
import os
import time
import random
from character import Character
from pygame.locals import *
from pygame import mixer

pygame.font.init()
pygame.init()

# fps = 27
# WIDTH, HEIGHT = 800, 800
# window = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Enemy Tutorial")

# Load images
# playerleft = [pygame.image.load('pics/megaman-left-1.bmp'), pygame.image.load('pics/megaman-left-2.bmp'), pygame.image.load('pics/megaman-left-3.bmp'), 
# pygame.image.load('pics/megaman-left-4.bmp'), pygame.image.load('pics/megaman-left-5.bmp'), pygame.image.load('pics/megaman-left-6.bmp')]

# playerrights = [pygame.image.load('pics/megaman-right-1.bmp'), pygame.image.load('pics/megaman-right-2.bmp'), pygame.image.load('pics/megaman-right-3.bmp'), 
# pygame.image.load('pics/megaman-right-4.bmp'), pygame.image.load('pics/megaman-right-5.bmp'), pygame.image.load('pics/megaman-right-6.bmp')]

bullet_img = pygame.image.load(os.path.join('pics','bullet-1.bmp'))

# stand = pygame.image.load('TestGames/R6.png')
# Enemy image
#flameLeft = [pygame.image.load('pics/heatman-flaming-left-1.bmp'), pygame.image.load('pics/heatman-flaming-left-2.bmp'), pygame.image.load('pics/heatman-flaming-left-3.bmp'), pygame.image.load('pics/heatman-flaming-left-4.bmp'), pygame.image.load('pics/heatman-flaming-left-5.bmp'), pygame.image.load('pics/heatman-flaming-left-6.bmp'), pygame.image.load('pics/heatman-flaming-left-7.bmp'), pygame.image.load('pics/heatman-flaming-left-8.bmp')]
#flameRight = [pygame.image.load('pics/heatman-flaming-right-1.bmp'), pygame.image.load('pics/heatman-flaming-right-2.bmp'), pygame.image.load('pics/heatman-flaming-right-3.bmp'), pygame.image.load('pics/heatman-flaming-right-4.bmp'), pygame.image.load('pics/heatman-flaming-right-5.bmp'), pygame.image.load('pics/heatman-flaming-right-6.bmp'), pygame.image.load('pics/heatman-flaming-right-7.bmp'), pygame.image.load('pics/heatman-flaming-right-8.bmp')]
# walkRight = [pygame.image.load('TestGames/R1E.png'), pygame.image.load('TestGames/R2E.png'), pygame.image.load('TestGames/R3E.png'), pygame.image.load('TestGames/R4E.png'), pygame.image.load('TestGames/R5E.png'), pygame.image.load('TestGames/R6E.png'), pygame.image.load('TestGames/R7E.png'), pygame.image.load('TestGames/R8E.png'), pygame.image.load('TestGames/R9E.png'), pygame.image.load('TestGames/R10E.png'), pygame.image.load('TestGames/R11E.png')]
# walkLeft = [pygame.image.load('TestGames/L1E.png'), pygame.image.load('TestGames/L2E.png'), pygame.image.load('TestGames/L3E.png'), pygame.image.load('TestGames/L4E.png'), pygame.image.load('TestGames/L5E.png'), pygame.image.load('TestGames/L6E.png'), pygame.image.load('TestGames/L7E.png'), pygame.image.load('TestGames/L8E.png'), pygame.image.load('TestGames/L9E.png'), pygame.image.load('TestGames/L10E.png'), pygame.image.load('TestGames/L11E.png')]

walkRight = [pygame.image.load('TestGames/R1E.png'), pygame.image.load('TestGames/R2E.png'), pygame.image.load('TestGames/R3E.png'), pygame.image.load('TestGames/R4E.png'), pygame.image.load('TestGames/R5E.png'), pygame.image.load('TestGames/R6E.png'), pygame.image.load('TestGames/R7E.png'), pygame.image.load('TestGames/R8E.png'), pygame.image.load('TestGames/R9E.png'), pygame.image.load('TestGames/R10E.png'), pygame.image.load('TestGames/R11E.png')]
walkLeft = [pygame.image.load('TestGames/L1E.png'), pygame.image.load('TestGames/L2E.png'), pygame.image.load('TestGames/L3E.png'), pygame.image.load('TestGames/L4E.png'), pygame.image.load('TestGames/L5E.png'), pygame.image.load('TestGames/L6E.png'), pygame.image.load('TestGames/L7E.png'), pygame.image.load('TestGames/L8E.png'), pygame.image.load('TestGames/L9E.png'), pygame.image.load('TestGames/L10E.png'), pygame.image.load('TestGames/L11E.png')]


# Lasers
bullet_img = pygame.image.load(os.path.join('pics','bullet-1.bmp'))

# Background
# bg = pygame.transform.scale(pygame.image.load('TestGames//bg.png'), (WIDTH, HEIGHT))
char = pygame.image.load('TestGames/standing.png')
# Background music
clock = pygame.time.Clock()


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
         if self.walkCount + 1 >= 18:
                self.walkCount = 0
         if self.vel > 0:
             window.blit(self.creature_img_right[self.walkCount//3], (self.x,self.y))
             self.walkCount += 1
         else:
             window.blit(self.creature_img_left[self.walkCount//3], (self.x,self.y))
             self.walkCount += 1

         for bullet in self.bullets:
            bullet.draw(window)
    
    def move(self, path, x, y, eyeX, eyeY):
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

#Player class
# class Player(Creature):
#     def __init__(self, x, y, walkCount = 0, health=100):
#         super().__init__(x, y, walkCount, health)
#         self.creature_img_left = playerleft
#         self.creature_img_right = playerrights
#         self.creature_img_standing = stand
#         self.bullet_img = bullet_img
#         self.mask = pygame.mask.from_surface(self.creature_img_standing)
#         self.max_health = health
#         self.jumpCount = 10
#         self.vel = 7
#         self.standing = True
#         self.isJump = False
#         self.left = False
#         self.right = False
#         self.facing = None
        
#     #Checks to see if bullet hits object
#     def move_bullets(self, vel, objs):
#         self.cooldown()
#         for bullet in self.bullets:
#             bullet.move(vel)
#             if bullet.off_screen(WIDTH):
#                 self.bullets.remove(bullet)
#             else:
#                 for obj in objs:
#                     if bullet.collision(obj):
#                         objs.remove(obj) #Removes the bullets and obj it hits
#                         if bullet in self.bullets:
#                             self.bullets.remove(bullet)
#     #Draws player
#     def draw(self, window):
#         super().draw(window) #Calls the ship initall variables
#         self.healthbar(window)
#     #Creates a health bar for player
#     def healthbar(self, window):
#         pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.creature_img_standing.get_height() + 10, self.creature_img_standing.get_width(), 10))
#         pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.creature_img_standing.get_height() + 10, self.creature_img_standing.get_width() * (self.health/self.max_health), 10))

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
#Checks for collotion of two objects and returns the result
# def collide(obj1, obj2):
#     print('hit')
#     offset_x = int(obj2.x - obj1.x)
#     offset_y = int(obj2.y - obj1.y)
#     return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

#Main class
# def main():
#     run = True
#   #Frame rate
#     enemy_width = random.randint(100, 1700)
#     #player = Player(WIDTH / 2, HEIGHT - 100)
#     gravity = .66
#     player = Character.rect
#     level = 0
#     lives = 5
#     main_font = pygame.font.SysFont("comicsans", 50)
#     lost_font = pygame.font.SysFont("comicsans", 60)
#     #Enemy details
#     enemies = []
#     wave_length = 5
#     player_vel = 7
#     #Player details
#     bullet_vel = 10
#     #Game run speed
#     clock = pygame.time.Clock()

#     lost = False
#     lost_count = 0
#     #Updates the screen 
#     def redraw_window():
#         window.blit(bg, (0,0))
#         #Draws the text
#         lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
#         level_label = main_font.render(f"Level: {level}", 1, (255,255,255))
#         #Displays text
#         window.blit(lives_label, (10, 10))
#         window.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
#         #Draws enemy in enemies list
#         for enemy in enemies:
#             enemy.draw(window)

#         #player.draw(window)
#         #Displays gameover
#         if lost:
#             lost_label = lost_font.render("Game Over", 1, (255,255,255))
#             window.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))
#         #Updates screen
#         pygame.display.update()
#     #Game running loop
#     while run:
#         clock.tick(fps)
#         redraw_window()
#         #or player.health <= 0:
#         if lives <= 0: #or player.health <= 0:
#             lost = True
#             lost_count += 1

#         if lost:
#             if lost_count > fps * 3:
#                 run = False
#             else:
#                 continue

#         if len(enemies) == 0:
#             level += 1
#             wave_length += 1
#             for i in range(wave_length):
#                 enemy = Enemy(random.randrange(50, WIDTH-100), HEIGHT - 100, WIDTH - 100)
#                 enemies.append(enemy)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 quit()

#         # keys = pygame.key.get_pressed()
#         # if keys[pygame.K_LEFT] and player.x - player_vel > 0: # left
#         #     player.x -= player_vel
#         #     player.facing = 1
#         # if keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < WIDTH: # right
#         #     player.x += player_vel
#         #     player.facing = -1
#         # if keys[pygame.K_UP] and player.y - player_vel > 0: # up
#         #     player.y -= player_vel
#         # if keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() + 15 < HEIGHT: # down
#         #     player.y += player_vel
#         # if keys[pygame.K_SPACE]:
#         #     player.shoot(player.facing)

#         for enemy in enemies[:]:
#             enemy.move(player)
#             enemy.move_bullets(bullet_vel, player)

#             if collide(enemy, player):
#                 player.health -= 10
#                 enemies.remove(enemy)
#             elif enemy.x + enemy.get_height() > HEIGHT:
#                 lives -= 1
#                 enemies.remove(enemy)

#         player.move_bullets(-bullet_vel, enemies)

# def main_menu():
#     title_font = pygame.font.SysFont("comicsans", 70)
#     run = True
#     while run:
#         window.blit(bg, (0,0))
#         title_label = title_font.render("Press the mouse to begin...", 1, (255,255,255))
#         window.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
#         pygame.display.update()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 main()
#     pygame.quit()

# main_menu()

