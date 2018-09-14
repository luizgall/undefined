import pygame
import random
from tela import tela

class GameObject:
    def __init__(self, model):
        
        self.pos = model["pos"]
        self.vel = [0,0]
        self.corPadrao = [0,0,0]
        self.corSelecionado = [255,0,0]
        self.selecionado = False
        self.nome = model["nome"]
        self.tipo = model["tipo"]
        if self.tipo == "botão":
            self.id = model["id"]
            self.texto = model["texto"]
        self.interact = False
    def draw(self):
        if self.tipo == "botão":
            myfont = pygame.font.SysFont('Arial', 30)
            if self.selecionado:
                font = myfont.render(self.texto, False, self.corSelecionado)
            else:
                font = myfont.render(self.texto, False, self.corPadrao)    
            tela.blit(font,(self.pos[0],self.pos[1]))
        else:        
            pygame.draw.rect(tela, self.corAtual, (self.pos[0],self.pos[1],20,20))
    def touch(self, target):
        if self.interact:
            self.interact = False
            self.color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
