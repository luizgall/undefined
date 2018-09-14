#IMPORTS
import pygame
import sys
from scenes import GerenciadorCenas


#INICIAR PYGAME
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

gerenciadorCenas = GerenciadorCenas()
gerenciadorCenas.iniciar()


#GAME LOOP
while True:
    #renderizar 
    gerenciadorCenas.atualizar()
    clock.tick(60)
