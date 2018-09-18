import pygame
from tela import tela

class Camera:
    def __init__(self):
        self.pos = [0,0]
        self.foco = {}
    
    def draw(self, objetos, modo):
        tela.fill((255,255,255))
        for obj in objetos:
            if obj.camada == modo:
                obj.draw(self.pos)

        pygame.display.flip() 
    
    def definirFoco(self, objetoPos):
        self.foco = objetoPos
        self.pos = objetoPos
