import pygame
import character as char

class Player(char.Character):
    def __init__(self, gravity):
        super().__init__(gravity)

        self.maxSpeed = 3.5
        self.accX = .5

        self.direction = "r"

        self.alive = True

        # This will update to give the end of the gun so bullet can grab it when necessary
        self.gunPoint = self.rect.center

        self.jump_height = 13

        self.health = 200

    def jump(self):
      if self.onGround:
        self.onGround = False
        self.rect.bottom = self.rect.bottom - 1
        self.movementy = 0
        self.movementy -= self.jump_height

    def changeDirection(self):
        if self.movementx > 0:
            self.direction = 'r'
        elif self.movementx < 0:
            self.direction = 'l'

    def advance(self):
        super().advance()
        self.changeDirection()
        self.gunPoint = self.rect.center





# test game loop
def game_loop():
    pass

def main():
    pass
    

if __name__ == "__main__":
    main()