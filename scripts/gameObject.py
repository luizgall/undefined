import pygame
import random
from tela import tela

class GameObject:
    def __init__(self, model):
        
        self.pos = model["pos"]
        self.vel = [0,0]
        self.ace = [0,0]
        self.altura = 0
        self.caindo = False
        self.camada = model["camada"]
        self.corPadrao = [0,0,0]
        self.corSelecionado = [255,0,0]
        self.selecionado = False
        self.nome = model["nome"]
        self.tipo = model["tipo"]
        self.peso = 0
        if self.tipo == "botão" or self.tipo == "texto":
            self.id = model["id"]
            self.texto = model["texto"]
        self.interact = False
        if self.tipo == "plataforma" or self.tipo == "player":
            self.largura = model["largura"]
            self.altura = model["altura"]
        if self.tipo == "player":
            self.peso = 1
            self.corPadrao = [255, 0, 0]
    def draw(self, cameraPos):
        if self.tipo == "botão" or self.tipo == "texto":
            myfont = pygame.font.SysFont('Arial', 30)
            if self.selecionado:
                font = myfont.render(self.texto, False, self.corSelecionado)
            else:
                font = myfont.render(self.texto, False, self.corPadrao)    
            tela.blit(font,(self.pos[0] - cameraPos[0],self.pos[1] - cameraPos[1]))
        else:        
            pygame.draw.rect(tela, self.corPadrao, (self.pos[0] - cameraPos[0]+300,self.pos[1] - cameraPos[1]+250, self.largura, self.altura))
    def touch(self, target):
        if self.interact:
            self.interact = False
            self.color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
