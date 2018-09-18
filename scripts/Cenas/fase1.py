import pygame
import sys
from gameObject import GameObject

def fase1Start(objetos):
    pass
def fase1Update(objetos, cena):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_UP:
            if event.key == pygame.K_DOWN:
              pass
            if event.key == pygame.K_UP:
               pass
            if event.key == pygame.K_RETURN:
               pass
            if event.key == pygame.K_ESCAPE:
               pass

fase1 = {
    "nome": "Fase 1",
    "modos": ["fase1", "JOGO", "SAIR"],
    "modoInicial": 0,
    "start": fase1Start,
    "update": fase1Update,
    "objetos": [
            {
             "tipo": "plataforma", 
             "camada": "fase1",
             "nome": "plataforma",      
             "pos": [0, 380],
             "altura": 20,
             "largura": 1000
        }
    ]
}
