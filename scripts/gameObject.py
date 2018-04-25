import pygame
from random import randint

class GameObject:
    def __init__(self, name, pos):
        self.pos = pos
        self.vel = [0,0]
        self.color = [0,0,0]
        self.name = name
        self.interact = False
    def draw(self, tela):
        pygame.draw.rect(tela, self.color, (self.pos[0],self.pos[1],20,20))
    def touch(self, target):
        if self.interact:
            self.interact = False
            self.color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
