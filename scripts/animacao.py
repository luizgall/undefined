from tela import tela
import pygame
from assetLoader import assetLoader
class Animacao():
    def __init__(self, model):
        self.frames = []
        self.vel = 5
        self.pos = [0,0]
        self.frameAtual = 0
        self.loop = True
        self.terminou = False
        self.count = 0

        for frames in model["frames"]:
            quadro = assetLoader.procurar(frames, "imagem")
            quadro = pygame.transform.scale(quadro, (400, 600))
            quadro = pygame.transform.rotate(quadro, 90)
            self.frames.append(quadro)
    
    def play(self):
        tela.blit(self.frames[self.frameAtual], self.pos)
        if self.count <= self.vel:
            self.count += 1
        else:
            self.count = 0
            if (self.frameAtual == len(self.frames) - 1) and self.loop:
                self.frameAtual = 0
            elif (self.frameAtual < len(self.frames) - 1):
                self.frameAtual += 1
