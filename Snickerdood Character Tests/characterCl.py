import pygame
import bulletCl
import bigBulletCl

"""
All you gotta do to interface is this:
Set the starting position with character.x = something and character.y = something.
In the game loop call character.drawChar(gameDisplay) and character.advanceChar(pygame)
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

        self.x = x
        self.y = y

        self.CHAR_RADIUS = 35

        self.hitbox_x = self.x - self.CHAR_RADIUS
        self.hitbox_y = self.y - self.CHAR_RADIUS

        self.hitbox = pygame.Rect(self.x, self.y, 70, 70)
        
        self.x_gun_location = 0
        self.y_gun_location = 0
        self.GUN_SIZE = 7

        self.bullet_list = pygame.sprite.Group()
        self.big_bullet_list = pygame.sprite.Group()

        # jump and in-air stuff
        self.JUMP_HEIGHT = 15
        self.JUMP_MAX = 3
        self.jumps = self.JUMP_MAX
        self.JUMP_MOMENTUM_CANCEL = 2.4 # divides the momentum while you're in the air (slows air x momentum)
        self.DROP_SPEED = .3
        self.FLOAT_AMOUNT = .2

        # speed stuff
        self.X_SPEED = 4
        self.x_momentum = 0
        self.X_MOMENTUM_CAP = 7

        self.y_momentum = 0
        self.Y_MOMENTUM_CAP = 50

        # air momentum lock changes how much you can actually change direction midair (smaller value means you have less control)
        self.AIR_MOMENTUM_LOCK = .07

        self.BIG_BULLET_KICKBACK = 25

        # key press states
        # movement
        self.pressed_left = False
        self.pressed_right = False
        self.pressed_up = False
        self.pressed_down = False
        self.on_ground = False

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
        self.FRICTION = .7

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
                    self.doAbility()
                if event.key == pygame.K_f:
                    self.shootBullet()
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

        # checking for key states
        if self.on_ground:
            if self.pressed_left:
                self.x_momentum -= self.X_SPEED
                self.direction_facing = "l"
            if self.pressed_right:
                self.x_momentum += self.X_SPEED
                self.direction_facing = "r"
        elif not self.on_ground:
            if self.pressed_left:
                self.x_momentum -= self.X_SPEED * self.AIR_MOMENTUM_LOCK
                self.direction_facing = "l"
            if self.pressed_right:
                self.x_momentum += self.X_SPEED * self.AIR_MOMENTUM_LOCK
                self.direction_facing = "r"
        if self.pressed_up:
            self.y_momentum -= self.FLOAT_AMOUNT
        if self.pressed_down:
            self.y_momentum += self.DROP_SPEED
        if self.on_ground:
            self.jumps = self.JUMP_MAX

    def setStartPos(self, x, y):
        self.x = x
        self.y = y

    # check where we are
    def checkScreenBoundaries(self, pygame):
        # screen boundaries
        display_width, display_height = pygame.display.get_surface().get_size()
        # right boundary
        if self.x > display_width - self.CHAR_RADIUS:
            self.x = display_width - self.CHAR_RADIUS
            self.x_momentum *= -1
        # left boundary
        elif self.x < 0 + self.CHAR_RADIUS:   
            self.x = 0 + self.CHAR_RADIUS
            self.x_momentum *= -1
        # top boundary
        if self.y < 0 + self.CHAR_RADIUS:
            self.y = 0 + self.CHAR_RADIUS
            self.y_momentum *= -.5
        # floor boundary
        elif self.y > display_height - self.CHAR_RADIUS:
            self.y = display_height - self.CHAR_RADIUS
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
        bullet = bulletCl.Bullet(self.x_gun_location, self.y_gun_location, self.gun_direction)
        self.bullet_list.add(bullet)

    # do duh abilidi
    def doAbility(self):
        bigBullet = bigBulletCl.BigBullet(self.x_gun_location, self.y_gun_location, self.gun_direction)
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
            self.y_momentum -= self.BIG_BULLET_KICKBACK


    def detectCollision(self, object):
        if self.hitbox.colliderect(object):
            self.y_momentum = 0
        

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

        # gravity
        if self.on_ground == False:
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

        
        self.checkScreenBoundaries(pygame)
        self.changeGunDirection()
        self.checkKeys(pygame)
        for bullet in self.bullet_list:
            bullet.advanceBullet(pygame)
            if bullet.alive == False:
                self.bullet_list.remove(bullet)

        for bigBullet in self.big_bullet_list:
            bigBullet.advanceBigBullet(pygame)
            if bigBullet.alive == False:
                self.big_bullet_list.remove(bigBullet)

        self.hitbox_x = self.x - self.CHAR_RADIUS
        self.hitbox_y = self.y - self.CHAR_RADIUS
        self.hitbox = pygame.Rect(self.hitbox_x, self.hitbox_y, 70, 70)
 
    # draw 'dat boi
    def drawChar(self, surface):
        pygame.draw.circle(surface, (0,0,0), (int(self.x),int(self.y)), self.CHAR_RADIUS, 1)
        self.drawGun(surface)
        for bullet in self.bullet_list:
            bullet.drawBullet(surface)
        for bigBullet in self.big_bullet_list:
            bigBullet.drawBigBullet(surface)
        #pygame.draw.rect(surface, (0,0,0), self.hitbox)