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

char_width = 90

# Character init
character = characterCl.Character()



clock = pygame.time.Clock()

def game_loop():

    # starting position
    x = int(display_width * .5)
    y = 500

    # speed and momentum variables
    x_speed = 2
    x_momentum = 0
    x_momentum_cap = 7
    jump_height = 15
    drop_speed = 1
    y_momentum = 0
    y_momentum_cap = 50

    # gravity and friction
    gravity = .5
    friction = .6
    
    


    pressed_left = False
    pressed_right = False
    pressed_up = False
    pressed_down = False

    dead = False

    while not dead:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = True        
            elif event.type == pygame.KEYDOWN:          # check for key presses          
                if event.key == pygame.K_LEFT:        # left arrow turns left
                    pressed_left = True
                elif event.key == pygame.K_RIGHT:     # right arrow turns right
                    pressed_right = True
                elif event.key == pygame.K_UP:        # up arrow goes up
                    y_momentum = -jump_height + (y_momentum / 2.4)
                elif event.key == pygame.K_DOWN:     # down arrow goes down
                    pressed_down = True
            elif event.type == pygame.KEYUP:            # check for key releases
                if event.key == pygame.K_LEFT:        # left arrow turns left
                    pressed_left = False
                elif event.key == pygame.K_RIGHT:     # right arrow turns right
                    pressed_right = False
                elif event.key == pygame.K_UP:        # up arrow goes up
                    pressed_up = False
                elif event.key == pygame.K_DOWN:     # down arrow goes down
                    pressed_down = False

        # In your game loop, check for key states:
        if pressed_left:
            x_momentum -= x_speed
        if pressed_right:
            x_momentum += x_speed
        """if pressed_up:
            y_momentum -= jump_height"""
        if pressed_down:
            y_momentum += drop_speed

        # print(event)

        x += x_momentum
        y += y_momentum

        # friction
        if x_momentum > 0:
            x_momentum -= friction
        elif x_momentum < 0:
            x_momentum += friction
        else:
            x_momentum = 0

        # gravity
        y_momentum += gravity

        # momentum caps
        if x_momentum > x_momentum_cap:
            x_momentum = x_momentum_cap
        elif x_momentum < -x_momentum_cap:
            x_momentum = -x_momentum_cap

        if y_momentum > y_momentum_cap:
            y_momentum = y_momentum_cap
        elif y_momentum < -y_momentum_cap:
            y_momentum = -y_momentum_cap    

        # Main display function
        gameDisplay.fill(white)
        character.drawChar(gameDisplay, x, y)

        # screen boundaries
        if x > display_width - int(char_width / 2):
            x = display_width - int(char_width / 2)
            x_momentum *= -1
        elif x < 0 + int(char_width / 2):   
            x = 0 + int(char_width / 2)
            x_momentum *= -1
        elif y < 0 + int(char_width / 2):
            y = 0 + int(char_width / 2)
            y_momentum *= -.5
        elif y > display_height - int(char_width / 2):
            y = display_height - int(char_width / 2)
            y_momentum = 0
    
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