import pygame
import characterCl

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("heyo")

# Colors
black = (0,0,0)
white = (255,255,255)

# Character init
character = characterCl.Character()

x = int(display_width * .5)
y = 500

clock = pygame.time.Clock()

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        # Control circle with keys


        # Main display function
        gameDisplay.fill(white)
        character.drawChar(gameDisplay, x, y)
        
        # print(event)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()