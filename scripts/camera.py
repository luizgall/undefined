import pygame
from tela import tela

class Camera:
    def __init__(self):
        self.pos = [0,0]
        self.foco = {}
    
    def draw(self, objetos, modo):
        for obj in objetos:
            if obj.camada == modo:
                obj.draw(self.pos)

        pygame.display.flip() 

    def drawBG(self, objeto):
        objeto.play()

    def drawParallax(self, objeto):
        objeto.draw()

    def definirFoco(self, objetoPos):
        self.foco = objetoPos
        self.pos = objetoPos
