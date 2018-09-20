import pygame
from os import listdir
from os.path import isfile, join
import time

class AssetLoader:
    def __init__(self):
        self.status = "carregando"
        self.mensagem = ""
        self.imagens = []
        self.sons = []
        self.fontes = []
    
    def carregarAssets(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.carregarImagens()
        self.carregarFontes()
        self.carregarAudios()
        self.status = "terminou"
        self.mensagem = ""

    def carregarImagens(self):
        path = "../assets/Img/"
        for file in listdir(path):
            if isfile(join(path, file)):
                self.mensagem = "carregando imagem " + file
                img = {}
                img["img"] = pygame.image.load(join(path, file))
                img["nome"] = file
                self.imagens.append(img)

    def carregarFontes(self):
        path = "../assets/fonts/"
        for file in listdir(path):
            if isfile(join(path, file)):
                self.mensagem = "carregando fonte " + file
                font = {}
                font["img"] = pygame.font.Font(join(path, file), 20)
                font["nome"] = file
                self.fontes.append(font)
                
    def carregarAudios(self):
        pass
    def procurarImagem(self, nome):
        for img in self.imagens:
            if img["nome"] == nome:
                return img["img"]
        
        # self.status = "next"