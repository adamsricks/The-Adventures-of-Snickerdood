import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, direction, center):
        super().__init__()
        self.direction = direction
        
        self.axe_right = pygame.transform.flip(pygame.image.load("axe03.png").convert_alpha(), True, False)
        self.axe_left = pygame.image.load("axe03.png").convert_alpha()

        self.surface_right = [self.axe_right, pygame.transform.rotate(self.axe_right, -45), pygame.transform.rotate(self.axe_right, -90), pygame.transform.rotate(self.axe_right, -135), pygame.transform.rotate(self.axe_right, -180), pygame.transform.rotate(self.axe_right, -225), pygame.transform.rotate(self.axe_right, -270), pygame.transform.rotate(self.axe_right, -315)]
        self.surface_left = [self.axe_left, pygame.transform.rotate(self.axe_left, 45), pygame.transform.rotate(self.axe_left, 90), pygame.transform.rotate(self.axe_left, 135), pygame.transform.rotate(self.axe_left, 180), pygame.transform.rotate(self.axe_left, 225), pygame.transform.rotate(self.axe_left, 270), pygame.transform.rotate(self.axe_left, 315)]
        
        if self.direction == "r":
            self.surface = self.surface_right
        else:
            self.surface = self.surface_left

        self.rect = self.surface_right[0].get_rect(center = (100, 576))
        self.rect.center = center
        

        self.spin_count = 0
        self.image_num = 0
        self.animation_speed = 5

        self.x = center[0]
        self.y = center[1]

        self.speed = 7

        if direction == "l":
            self.x_movement = -self.speed
        elif direction == "r":
            self.x_movement = self.speed

    def draw(self, screen):
        # pygame.draw.rect(screen, (0,0,0), self.rect)
        screen.blit(self.surface[self.image_num], self.rect)

    def advance(self):
        self.spin_count += 1
        if self.spin_count // self.animation_speed >= len(self.surface):
            self.spin_count = 0
        self.image_num = self.spin_count // self.animation_speed
        self.rect = self.surface[self.image_num].get_rect(center = (100, 576))
        self.x += self.x_movement
        self.rect.center = (self.x, self.y)

    def checkCollision(self, character):
        if character.rect.colliderect(self.rect):
            return True

        



def main():
    pygame.init()

    global gameDisplay
    gameDisplay = pygame.display.set_mode((1200,600))
    pygame.display.set_caption("Bullet Test")

    global black
    global white
    black = (0,0,0)
    white = (255,255,255)

    global bullet
    bullet = Bullet("l", (500,500))

    global clock
    clock = pygame.time.Clock()
    game_loop()
    pygame.quit()
    quit()



def game_loop():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)

        bullet.advance()
        bullet.draw(gameDisplay)

        pygame.display.update()
        clock.tick(60)





if __name__ == "__main__":
    main()