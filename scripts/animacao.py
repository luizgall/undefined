from tela import tela
import pygame
from assetLoader import assetLoader
class Animacao():
    def __init__(self, model):
        self.frames = []
        self.vel = 10
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


class Parallax():
    def __init__(self, model):
        self.frame0 = model["frames"][0] 
        self.frame0 = assetLoader.procurar(self.frame0, "imagem")
        # self.frame0 = pygame.transform.scale(self.frame0, (400, 600))
        # self.frame0 = pygame.transform.rotate(self.frame0, 90)


        self.frame1 = model["frames"][1] 
        self.frame1 = assetLoader.procurar(self.frame1, "imagem")
        # self.frame1 = pygame.transform.scale(self.frame1, (400, 600))
        # self.frame1 = pygame.transform.rotate(self.frame1, 90)

        self.frame2 = model["frames"][2] 
        self.frame2 = assetLoader.procurar(self.frame2, "imagem")
        self.frame2 = pygame.transform.scale(self.frame2, (600, 600))
        # self.frame2 = pygame.transform.rotate(self.frame2, 90)

        self.frame3 = model["frames"][3] 
        self.frame3 = assetLoader.procurar(self.frame3, "imagem")
        self.frame3 = pygame.transform.scale(self.frame3, (600, 600))
        # self.frame3 = pygame.transform.rotate(self.frame3, 90)

        self.frame0Pos = [0,0]
        self.frame1Pos = [0,0]
        self.frame2Pos = [0,-200]
        self.frame3Pos = [100,150]
    
    def draw(self):
        tela.blit(self.frame0, self.frame0Pos)

        tela.blit(self.frame1, self.frame1Pos)
        tela.blit(self.frame1, [self.frame1Pos[0] + 600,self.frame1Pos[1]])
        
        tela.blit(self.frame2, self.frame2Pos)
        tela.blit(self.frame2, [self.frame2Pos[0] + 600,self.frame2Pos[1]])

        tela.blit(self.frame3, self.frame3Pos)
        tela.blit(self.frame3, [self.frame3Pos[0] + 600,self.frame3Pos[1]])

