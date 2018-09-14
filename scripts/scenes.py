import pygame
from gameObject import GameObject
from tela import tela


class Scene:
    def __init__(self, model):
        self.nome = model["nome"]
        self.objetosModel = model["objetos"]
        self.objetos = []
        self.atualizarCena = model["update"]
    def start(self):
        print("Start scene ", self.nome)
        ## criar objetos
        for obj in self.objetosModel:
            novoObjeto = GameObject(obj)
            self.objetos.append(novoObjeto)
    def update(self):
        for obj in self.objetos:
            print(obj.tipo)
            obj.draw()
        self.atualizarCena(self.objetos)
    