import pygame
from gameObject import GameObject
from tela import tela
from physics import Physics
from camera import Camera

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
        self.jogador = ""
        self.fisica = Physics()
        self.camera = Camera()
    def start(self):
        print("Start Cena ", self.nome)
        ## criar objetos
        for obj in self.objetosModel:
            novoObjeto = GameObject(obj)
            if obj["tipo"] == "player":
                self.jogador = novoObjeto
                self.jogador.pos = obj["pos"]
                self.camera.definirFoco(self.jogador.pos)
            self.objetos.append(novoObjeto)
        self.iniciarCena(self.objetos, self)
    def update(self):
        self.atualizarCena(self.objetos, self)
        self.fisica.atualizar(self.objetos)
        self.camera.draw(self.objetos, self.modo)
        if self.terminou:
            return {
                "proximaCena": self.proximaCena,
                "terminou": True
            }
        else:
            return {
                "terminou": False
            }

