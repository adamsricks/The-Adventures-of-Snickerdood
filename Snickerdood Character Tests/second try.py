import pygame
import characterCl

pygame.init()

display_width = 1200
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("heyo")

# Colors
black = (0,0,0)
white = (255,255,255)

# Character init
char = characterCl.Character()


clock = pygame.time.Clock()

def game_loop():

    # starting position
    char.setStartPos(int(display_width * .5), 500)

    rectangle = pygame.Rect(200, 400, 100, 100)
    

    while char.alive:

        # Main display function
        gameDisplay.fill(white)
        char.drawChar(gameDisplay)
        char.advanceChar(pygame)

        pygame.draw.rect(gameDisplay, black, rectangle)

        char.detectCollision(rectangle)
    
        # update display and clock move forward 
        pygame.display.update() 
        clock.tick(60)

# actually do everything 
def main():
    game_loop()
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()