import pygame
import sys
sys.path.append("Cenas/")
from gameObject import GameObject
from tela import tela
from eventos import GerenciadorEventos
from scenes import Cena
from Cenas import *


def scenesFactory():

    return {
        "menuPrincipal": Cena(menuPrincipal),
        "fase1": Cena(fase1)
    }
