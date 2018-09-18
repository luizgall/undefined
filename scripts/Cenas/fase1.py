import pygame
import sys
from gameObject import GameObject

obsModel = {
             "tipo": "plataforma", 
             "camada": "fase1",
             "nome": "plataforma",      
             "pos": [200, 200],
             "altura": 20,
             "largura": 20
        }
def fase1Start(objetos):
    pass
def fase1Update(objetos, cena):
    def criarObstaculo():
        obstaculo = GameObject(obsModel)
        cena.objetos.append(obstaculo)
    
    if len(cena.objetos) < 4:
        criarObstaculo()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # if event.type == pygame.KEYDOWN:
        #     # if event.key == pygame.K_UP:
        #     if event.key == pygame.K_DOWN:
        #       pass
        #     if event.key == pygame.K_UP:
        #        cena.jogador.pos[0] += 10
        #     if event.key == pygame.K_RIGHT:
        #        cena.jogador.vel[0] += 10
        #     elif event.key == pygame.K_LEFT:
        #        cena.jogador.vel[0] -= 10
        #     if event.key == pygame.K_RETURN:
        #        pass
        #     if event.key == pygame.K_ESCAPE:
        #        pass
        # if event.type == pygame.KEYUP:
        #     cena.jogador.vel = [0,0]
        
        teclas_pressionadas = pygame.key.get_pressed()
        if teclas_pressionadas[pygame.K_LEFT]:
            cena.jogador.vel[0] = -10
        elif teclas_pressionadas[pygame.K_RIGHT]:
            cena.jogador.vel[0] = 10
        else:
            cena.jogador.vel[0] = 0
        
        if teclas_pressionadas[pygame.K_UP]:
            cena.jogador.ace = [0,-10]
            print("JUMP", cena.jogador.ace)

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
        },

        {
             "tipo": "player", 
             "camada": "fase1",
             "nome": "Jogador",      
             "pos": [50, 120],
             "altura": 60,
             "largura": 30
        }
    ]
}
