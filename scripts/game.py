#IMPORTS
import pygame
import sys
import _thread
from gerenciadorCenas import GerenciadorCenas
from assetLoader import assetLoader
from tela import tela
import scenesModel

#INICIAR PYGAME
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

cenas = scenesModel.scenesFactory()
_thread.start_new_thread(assetLoader.carregarAssets, ())
myfont = pygame.font.Font('../assets/fonts/Kalam-Bold.ttf', 20)
while assetLoader.status == "carregando":
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    tela.fill((0,0,0))
    font = myfont.render(assetLoader.mensagem, True, (255, 255, 255))
    tela.blit(font,(200 , 300))
    pygame.display.flip() 

tela.fill((0,0,0))
gerenciadorCenas = GerenciadorCenas(cenas)
gerenciadorCenas.iniciar()

#GAME LOOP
while True:
        gerenciadorCenas.atualizar()
        clock.tick(60)
