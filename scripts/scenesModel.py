import pygame
import sys
sys.path.append("Cenas/")
from gameObject import GameObject
from tela import tela
from eventos import GerenciadorEventos
from scenes import Cena
from Cenas import *


def scenesFactory():

    # fase1 = {
    #     "nome": "Primeira Fase",
    #     "modos": ["PRINCIPAL", "JOGO", "SAIR"],
    #     "modoInicial": 0,
    #     "start": menuPrincipalStart,
    #     "update": menuPrincipalUpdate,
    #     "objetos": [

    #         {
    #             "tipo": "texto",
    #             "nome": "botao",
    #             "pos": [400, 300],
    #             "id": "1",
    #             "texto": "Iniciando jogo",
    #             "camada": "JOGO"
    #         }

    #     ]
    # }

    return {
        "menuPrincipal": Cena(menuPrincipal),
        "fase1": Cena(menuPrincipal)
    }
