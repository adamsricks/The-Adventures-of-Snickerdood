import pygame
'''import bulletCl
import bigBulletCl'''

"""
All you gotta do to interface is this:
Set the starting position setStartPos(x,y).
In the game loop call character.drawChar(gameDisplay) and character.advanceChar(pygame).
And detect collisions but we'll see how that'll work.
And that's it! Lol

Up: Reduce fall speed
Down: Increase fall speed
Right & left: Move right and left
Space: Jump
Z: Aim diagonally down
X: Aim diagonally up
C: Ability (???)
V: Small blast
"""

class Character(pygame.sprite.Sprite):
    def __init__(self, x = 0, y = 0):
        super().__init__()

        # position
        self.x = x
        self.y = y

        # size
        self.CHAR_RADIUS = 40 # depricated
        self.HEIGHT = 43
        self.WIDTH = 25

        # hit box size
        self.HITBOXHEIGHT = 34
        self.HITBOXWIDTH = 23

        # and assigning it before it is advanced in advanceChar()
        self.hitbox_x = self.x
        self.hitbox_y = self.y
        
        '''
        self.x_gun_location = 0
        self.y_gun_location = 0
        self.GUN_SIZE = 7

        self.bullet_list = pygame.sprite.Group()
        self.big_bullet_list = pygame.sprite.Group()
        '''

        # jump and in-air stuff
        self.JUMP_HEIGHT = 15
        self.JUMP_MAX = 1
        self.jumps = self.JUMP_MAX
        self.JUMP_MOMENTUM_CANCEL = 2.4 # divides the momentum while you're in the air (slows air x momentum)
        self.DROP_SPEED = .3
        self.FLOAT_AMOUNT = .2

        # speed stuff
        self.X_SPEED = 3 # static x-axis speed add
        self.x_momentum = 0
        self.X_MOMENTUM_CAP = 5

        self.y_momentum = 0
        self.Y_MOMENTUM_CAP = 50

        # air momentum lock changes how much you can actually change direction midair (smaller value means you have less control)
        self.AIR_MOMENTUM_LOCK = .12

        '''
        self.BIG_BULLET_KICKBACK = 25'''

        # key press states
        # movement
        self.pressed_left = False
        self.pressed_right = False
        self.pressed_up = False
        self.pressed_down = False
        self.on_ground = False
        self.on_platform = False

        # direction_facing (r or l)
        self.direction_facing = "r"

        # gun stuff
        self.looking_diag_up = False
        self.looking_diag_down = False

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
        self.gun_direction = "r"

        # other states and stuff
        self.health = 200
        self.alive = True
        self.lives = 1

        # gravity and friction
        self.GRAVITY = .5
        self.FRICTION = .5

        self.walkRight = [pygame.image.load('pics/megaman-right-1.bmp'), pygame.image.load('pics/megaman-right-2.bmp'), pygame.image.load('pics/megaman-right-3.bmp'), pygame.image.load('pics/megaman-right-4.bmp'), pygame.image.load('pics/megaman-right-5.bmp'), pygame.image.load('pics/megaman-right-6.bmp')]
        self.walkLeft = [pygame.image.load('pics/megaman-left-1.bmp'), pygame.image.load('pics/megaman-left-2.bmp'), pygame.image.load('pics/megaman-left-3.bmp'), pygame.image.load('pics/megaman-left-4.bmp'), pygame.image.load('pics/megaman-left-5.bmp'), pygame.image.load('pics/megaman-left-6.bmp')]
        self.standingRight = pygame.image.load('pics/megaman-right-static-1.bmp')
        self.standingLeft = pygame.image.load('pics/megaman-left-static-1.bmp')

        # walk count for animation
        self.walkCount = 0

    # check all the key states
    def checkKeys(self, pygame):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.alive = False      

            # check for key presses 
            elif event.type == pygame.KEYDOWN:                    
                if event.key == pygame.K_LEFT:
                    self.pressed_left = True
                elif event.key == pygame.K_RIGHT:
                    self.pressed_right = True
                if event.key == pygame.K_DOWN:  
                    self.pressed_down = True
                elif event.key == pygame.K_UP:
                    self.pressed_up = True

                # space for jump
                if event.key == pygame.K_SPACE:
                    if self.jumps > 0:
                        self.y_momentum = -self.JUMP_HEIGHT + (self.y_momentum / self.JUMP_MOMENTUM_CANCEL)
                if event.key == pygame.K_a:
                    self.looking_diag_down = True
                    #pass
                if event.key == pygame.K_s:
                    self.looking_diag_up = True
                    #pass
                if event.key == pygame.K_d:
                    '''self.doAbility()'''
                if event.key == pygame.K_f:
                    '''self.shootBullet()'''

            # check for key releases
            elif event.type == pygame.KEYUP:            
                if event.key == pygame.K_LEFT:
                    self.pressed_left = False
                if event.key == pygame.K_RIGHT:
                    self.pressed_right = False
                if event.key == pygame.K_UP:
                    self.pressed_up = False
                if event.key == pygame.K_DOWN:
                    self.pressed_down = False
                if event.key == pygame.K_SPACE:
                    self.jumps -= 1
                if event.key == pygame.K_a:
                    self.looking_diag_down = False
                if event.key == pygame.K_s:
                    self.looking_diag_up = False

    # quick set start position
    def setStartPos(self, x, y):
        self.x = x
        self.y = y

    # check where we are
    def checkScreenBoundaries(self, pygame):
        # screen boundaries
        display_width, display_height = pygame.display.get_surface().get_size()
        # right boundary
        if self.x > display_width - self.WIDTH:
            self.x = display_width - self.WIDTH
            self.x_momentum *= -1
        # left boundary
        elif self.x < 0:   
            self.x = 0
            self.x_momentum *= -1
        # top boundary
        if self.y < 0:
            self.y = 0
            self.y_momentum *= -.5
        # floor boundary
        elif self.y > display_height - self.HEIGHT:
            self.y = display_height - self.HEIGHT
            self.y_momentum = 0
            self.on_ground = True
        elif self.y > display_height - 1:
            #self.on_ground = True
            pass
        if self.y_momentum > 0 or self.y_momentum < 0:
            self.on_ground = False
            
    # gun stuff
    def changeGunDirection(self):
        if self.looking_diag_down == True and self.looking_diag_up == True:
            self.gun_direction = "u"
        elif self.pressed_down == True and self.on_ground == False:
            self.gun_direction = "d"
        elif self.pressed_up == True:
            if self.looking_diag_up == True:
                if self.direction_facing == "r":
                    self.gun_direction = "ur"
                elif self.direction_facing == "l":
                    self.gun_direction = "ul"
            elif self.looking_diag_down == True:
                if self.direction_facing == "r":
                    self.gun_direction = "dr"
                elif self.direction_facing == "l":
                    self.gun_direction = "dl"
            else:
                self.gun_direction = "u"
        elif self.direction_facing == "r":
            if self.looking_diag_up == True:
                self.gun_direction = "ur"
            elif self.looking_diag_down == True:
                self.gun_direction = "dr"
            else:
                self.gun_direction = "r"
        elif self.direction_facing == "l":
            if self.looking_diag_up == True:
                self.gun_direction = "ul"
            elif self.looking_diag_down == True:
                self.gun_direction = "dl"
            else:
                self.gun_direction = "l"

    # draw duh gun  
    def drawGun(self, surface):
        if self.gun_direction == "dl":
            self.x_gun_location = self.x - self.CHAR_RADIUS
            self.y_gun_location = self.y + self.CHAR_RADIUS
        elif self.gun_direction == "l":
            self.x_gun_location = self.x - self.CHAR_RADIUS
            self.y_gun_location = self.y
        elif self.gun_direction == "ul":
            self.x_gun_location = self.x - self.CHAR_RADIUS
            self.y_gun_location = self.y - self.CHAR_RADIUS
        elif self.gun_direction == "u":
            self.x_gun_location = self.x
            self.y_gun_location = self.y - self.CHAR_RADIUS
        elif self.gun_direction == "ur":
            self.x_gun_location = self.x + self.CHAR_RADIUS
            self.y_gun_location = self.y - self.CHAR_RADIUS
        elif self.gun_direction == "r":
            self.x_gun_location = self.x + self.CHAR_RADIUS
            self.y_gun_location = self.y  
        elif self.gun_direction == "dr":
            self.x_gun_location = self.x + self.CHAR_RADIUS
            self.y_gun_location = self.y + self.CHAR_RADIUS
        elif self.gun_direction == "d":
            self.x_gun_location = self.x
            self.y_gun_location = self.y + self.CHAR_RADIUS

        # figure out how to draw the gun...
        pygame.draw.circle(surface, (0,0,0), (int(self.x_gun_location),int(self.y_gun_location)), self.GUN_SIZE, 1)
    
    # shoot duh bullet
    def shootBullet(self):
        pass
        #bullet = bulletCl.Bullet(self.x_gun_location, self.y_gun_location, self.gun_direction)
        #self.bullet_list.add(bullet)

    # do duh abilidi
    def doAbility(self):
        pass
        '''bigBullet = bigBulletCl.BigBullet(self.x_gun_location, self.y_gun_location, self.gun_direction)
        self.big_bullet_list.add(bigBullet)
        if self.gun_direction == "dl":
            self.x_momentum += self.BIG_BULLET_KICKBACK
            self.y_momentum -= self.BIG_BULLET_KICKBACK
        elif self.gun_direction == "l":
            self.x_momentum += self.BIG_BULLET_KICKBACK
        elif self.gun_direction == "ul":
            self.x_momentum += self.BIG_BULLET_KICKBACK
            self.y_momentum += self.BIG_BULLET_KICKBACK
        elif self.gun_direction == "u":
            self.y_momentum += self.BIG_BULLET_KICKBACK
        elif self.gun_direction == "ur":
            self.x_momentum -= self.BIG_BULLET_KICKBACK
            self.y_momentum += self.BIG_BULLET_KICKBACK
        elif self.gun_direction == "r":
            self.x_momentum -= self.BIG_BULLET_KICKBACK
        elif self.gun_direction == "dr":
            self.x_momentum -= self.BIG_BULLET_KICKBACK
            self.y_momentum -= self.BIG_BULLET_KICKBACK
        elif self.gun_direction == "d":
            self.y_momentum -= self.BIG_BULLET_KICKBACK'''

    # our platform detection that doesnt work
    def detectPlatformCollision(self, thisObject):
        
        # topright
        '''if self.hitbox.topright[0] >= thisObject.bottomleft[0] and (self.hitbox.topright[1] < thisObject.bottomleft[1] and self.hitbox.bottomright[1] > thisObject.topleft[1]):
            self.x_momentum *= -1
            print("collide right")'''
        
        '''if self.hitbox.bottomright[1] >= thisObject.topleft[1] and (self.hitbox.bottomright[0] > thisObject.topleft[0] and self.hitbox.bottomleft[0] < thisObject.topright[0]):
            self.y_momentum = 0
            #self.on_ground = True
            print("hitting top")'''

        if self.hitbox.colliderect(thisObject) and (self.hitbox.bottomright[0] > thisObject.topleft[0] and self.hitbox.bottomleft[0] < thisObject.topright[0]):
            self.y_momentum = 0
            self.y = thisObject.top - self.HEIGHT + 1
            self.on_platform = True
        elif not self.hitbox.colliderect(thisObject) and (self.hitbox.bottomright[0] > thisObject.topleft[0] and self.hitbox.bottomleft[0] < thisObject.topright[0]):
            self.on_platform = False
        '''
        # bottomright
        if thisObject.collidepoint(self.hitbox.bottomright): #and self.hitbox.bottomright[0] < thisObject.topleft[0]:
            self.x_momentum = 0
            print("collide bottomright")
        elif thisObject.collidepoint(self.hitbox.bottomright): #and self.hitbox.bottomright[1] < thisObject.topleft[1]:
            self.y_momentum = 0
            self.on_ground = True
            print(thisObject.collidepoint(self.hitbox.bottomright))
            print(self.hitbox.bottomright[1] < thisObject.topleft[1])
            print("collide bottomright")
        # topleft
        if thisObject.collidepoint(self.hitbox.topleft): #and self.hitbox.topleft[0] > thisObject.bottomright[0]:
            self.x_momentum = 0
            print("collide topleft")
        elif thisObject.collidepoint(self.hitbox.topleft): #and self.hitbox.topleft[1] > thisObject.bottomright[1]:
            self.y_momentum = 0
            print("collide topleft")
        # bottomleft
        if thisObject.collidepoint(self.hitbox.bottomleft): #and self.hitbox.bottomleft[0] > thisObject.topright[0]:
            self.x_momentum = 0
            print("collide bottomleft")
        elif thisObject.collidepoint(self.hitbox.bottomleft): #and self.hitbox.bottomleft[1] < thisObject.topright[1]:
            self.y_momentum = 0
            self.on_ground = True
            print("collide bottomleft")
        print("detecting collisions")'''

        

        # use clipline(x1, y1, x2, y2) to test for platform collisions (returns empty tuple if it doesn't collide)
        

    # move 'dat boi
    def advanceChar(self, pygame):
        # momentum
        self.x += self.x_momentum
        self.y += self.y_momentum

        # friction
        if self.on_ground:
            if self.x_momentum > 0.2:
                self.x_momentum -= self.FRICTION
            elif self.x_momentum < -0.2:
                self.x_momentum += self.FRICTION
            else:
                self.x_momentum = 0
        
        # checking if hes on the platform but doesnt work
        if self.on_platform:
            if self.x_momentum > 0.2:
                self.x_momentum -= self.FRICTION
            elif self.x_momentum < -0.2:
                self.x_momentum += self.FRICTION
            else:
                self.x_momentum = 0

        # gravity
        if self.on_ground == False and self.on_platform == False:
            self.y_momentum += self.GRAVITY

        # momentum caps
        if self.x_momentum > self.X_MOMENTUM_CAP:
            self.x_momentum = self.X_MOMENTUM_CAP
        elif self.x_momentum < -self.X_MOMENTUM_CAP:
            self.x_momentum = -self.X_MOMENTUM_CAP

        if self.y_momentum > self.Y_MOMENTUM_CAP:
            self.y_momentum = self.Y_MOMENTUM_CAP
        elif self.y_momentum < -self.Y_MOMENTUM_CAP:
            self.y_momentum = -self.Y_MOMENTUM_CAP

        # checking for key states
        # regular movement on ground
        if self.on_ground or self.on_platform:
            if self.pressed_left:
                self.x_momentum -= self.X_SPEED
                self.direction_facing = "l"
            if self.pressed_right:
                self.x_momentum += self.X_SPEED
                self.direction_facing = "r"
        # less movement in air
        elif not self.on_ground or self.on_platform:
            if self.pressed_left:
                self.x_momentum -= self.X_SPEED * self.AIR_MOMENTUM_LOCK
                self.direction_facing = "l"
            if self.pressed_right:
                self.x_momentum += self.X_SPEED * self.AIR_MOMENTUM_LOCK
                self.direction_facing = "r"
        # float if pressing up in air
        if self.pressed_up:
            self.y_momentum -= self.FLOAT_AMOUNT
        # drop hard if pressing down
        if self.pressed_down:
            self.y_momentum += self.DROP_SPEED
        # get jumps back if on ground
        if self.on_ground:
            self.jumps = self.JUMP_MAX
            self.on_platform = False
        if self.on_platform:
            self.jumps = self.JUMP_MAX
            print(self.jumps)

        
        self.checkScreenBoundaries(pygame)
        self.changeGunDirection()
        self.checkKeys(pygame)
        '''for bullet in self.bullet_list:
            bullet.advanceBullet(pygame)
            if bullet.alive == False:
                self.bullet_list.remove(bullet)

        for bigBullet in self.big_bullet_list:
            bigBullet.advanceBigBullet(pygame)
            if bigBullet.alive == False:
                self.big_bullet_list.remove(bigBullet)'''

        # assigning hitbox and making it follow him
        self.hitbox_x = self.x + 15
        self.hitbox_y = self.y + 9
        self.hitbox = pygame.Rect(self.hitbox_x, self.hitbox_y, self.HITBOXWIDTH, self.HITBOXHEIGHT)

        # walk count for animation
        if self.walkCount + 1 >= 24:
            self.walkCount = 0
 
    # draw 'dat boi
    def drawChar(self, surface):
        #pygame.draw.circle(surface, (0,0,0), (int(self.x),int(self.y)), self.CHAR_RADIUS, 1)
        '''self.drawGun(surface)
        for bullet in self.bullet_list:
            bullet.drawBullet(surface)
        for bigBullet in self.big_bullet_list:
            bigBullet.drawBigBullet(surface)'''
        #pygame.draw.rect(surface, (0,0,0), self.hitbox)

        # hitbox draw
        pygame.draw.rect(surface,black,(self.hitbox_x,self.hitbox_y,self.HITBOXWIDTH,self.HITBOXHEIGHT))
    
        # running animation while running (duh)
        if self.x_momentum == 0:
            if self.direction_facing == "r":
                surface.blit(self.standingRight, (self.x, self.y))
            elif self.direction_facing == "l":
                surface.blit(self.standingLeft, (self.x, self.y))
        elif self.direction_facing == "r":
            surface.blit(self.walkRight[self.walkCount//4], (self.x, self.y))
            self.walkCount += 1
        elif self.direction_facing == "l":
            surface.blit(self.walkLeft[self.walkCount//4], (self.x, self.y))
            self.walkCount += 1

        

# test main
def main():
    pygame.init()

    global display_width
    display_width = 1200
    global display_height
    display_height = 600

    global gameDisplay
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("Character Test")

    # Colors
    global black
    global white
    black = (0,0,0)
    white = (255,255,255)

    # Character init
    global char
    char = Character()

    global clock
    clock = pygame.time.Clock()
    game_loop()
    pygame.quit()
    quit()

# test game loop
def game_loop():

    # starting position
    char.setStartPos(int(display_width * .5), 200)

    rectangle = pygame.Rect(800, 400, 400, 20)
    

    while char.alive:

        # Main display function
        gameDisplay.fill(white)
        char.advanceChar(pygame)
        char.drawChar(gameDisplay)
        

        pygame.draw.rect(gameDisplay, black, rectangle)

        char.detectPlatformCollision(rectangle)
    
        # update display and clock move forward 
        pygame.display.update()
        clock.tick(60)
        #print(f"topleft = {char.hitbox.topleft}")
        #print(f"bottomleft = {char.hitbox.bottomleft}")
        #print(f"bottomright = {char.hitbox.bottomright}")
        #print(f"topright = {char.hitbox.topright}")




        # use clipline(x1, y1, x2, y2) to test for platform collisions (returns empty tuple if it doesn't collide)

if __name__ == "__main__":
    main()