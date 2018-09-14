import pygame
from gameObject import GameObject
from tela import tela


class Cena:
    def __init__(self, model):
        self.nome = model["nome"]
        self.objetosModel = model["objetos"]
        self.modos = model["modos"]
        self.modo = self.modos[model["modoInicial"]]
        self.modoAtual = self.modos[model["modoInicial"]]
        self.objetos = []
        self.terminou = False
        self.proximaCena = ""
        self.iniciarCena = model["start"]
        self.atualizarCena = model["update"]
    def start(self):
        print("Start Cena ", self.nome)
        ## criar objetos
        for obj in self.objetosModel:
            novoObjeto = GameObject(obj)
            self.objetos.append(novoObjeto)
        self.iniciarCena(self.objetos)
    def update(self):
        tela.fill((255,255,255))
        for obj in self.objetos:
            if obj.camada == self.modo:
                obj.draw()

        pygame.display.flip()    
        self.atualizarCena(self.objetos, self)
        if self.terminou:
            return {
                "proximaCena": self.proximaCena,
                "terminou": True
            }
        else:
            return {
                "terminou": False
            }

