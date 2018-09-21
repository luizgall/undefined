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
        self.audios = []
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
        path = "../assets/img/"
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
                font["font"] = pygame.font.Font(join(path, file), 20)
                font["nome"] = file
                self.fontes.append(font)
                
    def carregarAudios(self):
        # path = "../assets/audio/"
        # for file in listdir(path):
        #     if isfile(join(path, file)):
        #         self.mensagem = "carregando fonte " + file
        #         font = {}
        #         font["audio"] = pygame.font.Font(join(path, file), 20)
        #         font["nome"] = file
        #         self.audios.append(font)
        pass
    def procurar(self, nome, tipo):
        if tipo == "imagem":    
            for img in self.imagens:
                if img["nome"] == nome:
                    return img["img"]

        if tipo == "fonte":    
            for font in self.fontes:
                if font["nome"] == nome:
                    return font["font"]
            
        # self.status = "next"

assetLoader = AssetLoader()