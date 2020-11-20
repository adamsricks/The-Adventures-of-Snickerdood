import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, direction, center):
        super().__init__()
        self.surface = None
        self.center = center
        self.direction = direction

        self.x = center[0]
        self.y = center[1]

        self.speed = 7

        # self.rect = self.surface.get_rect(center = (100, 576))

        self.rect = pygame.Rect(self.x,self.y,5,3)

        if direction == "l":
            self.x_movement = -self.speed
        elif direction == "r":
            self.x_movement = self.speed

    def draw(self, screen):
        # screen.blit(self.surface, self.rect)
        pygame.draw.rect(screen, (0,0,0), self.rect)

    def advance(self):
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