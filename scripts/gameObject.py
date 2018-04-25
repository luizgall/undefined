import pygame

class GameObject:
    def __init__(self, name, pos):
        self.pos = pos
        self.vel = [0,0]
        self.name = name
    def draw(self, color, tela):
        pygame.draw.rect(tela, color, (self.pos[0],self.pos[1],20,20))
