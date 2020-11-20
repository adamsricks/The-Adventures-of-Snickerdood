import pygame
import character as char

class Player(char.Character):
    def __init__(self, gravity):
        super().__init__(gravity)

        self.health = 200
    def startPos(self, rect):
        self.rect.bottom = rect.bottom
        self.rect.left = rect.left
