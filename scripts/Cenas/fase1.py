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
def fase1Start(objetos, cena):
    cena.camera.definirFoco(cena.jogador.pos)
def fase1Update(objetos, cena):
    def criarObstaculo():
        obstaculo = GameObject(obsModel)
        cena.objetos.append(obstaculo)
    
    # if len(cena.objetos) < 4:
    #     criarObstaculo()

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
            print(cena.jogador.vel)
            cena.jogador.vel[0] = -10
        elif teclas_pressionadas[pygame.K_RIGHT]:
            cena.jogador.vel[0] = 10
        else:
            cena.jogador.vel[0] = 0
        
        if teclas_pressionadas[pygame.K_UP]:
            if(cena.modo == "PAUSE"):
                if objetos[2].selecionado:
                    objetos[2].selecionado = False
                    objetos[4].selecionado = True
                elif objetos[3].selecionado:
                    objetos[3].selecionado = False
                    objetos[2].selecionado = True
                elif objetos[4].selecionado:
                    objetos[4].selecionado = False
                    objetos[3].selecionado = True                    
            elif not (cena.jogador.caindo):
                cena.jogador.vel[1] -= 15
                cena.jogador.caindo = True

        if teclas_pressionadas[pygame.K_DOWN]:
            if(cena.modo == "PAUSE"):
                if objetos[2].selecionado:
                    objetos[2].selecionado = False
                    objetos[3].selecionado = True
                elif objetos[3].selecionado:
                    objetos[3].selecionado = False
                    objetos[4].selecionado = True
                elif objetos[4].selecionado:
                    objetos[4].selecionado = False
                    objetos[2].selecionado = True  

        if teclas_pressionadas[pygame.K_ESCAPE]:
            if(cena.modo == "PAUSE"):
                cena.camera.definirFoco(cena.jogador.pos)                
                cena.modo = "fase1"
            else:    
                objetos[2].selecionado = True            
                cena.modo = "PAUSE"
                cena.camera.definirFoco([0,0])
        
        if teclas_pressionadas[pygame.K_RETURN]:
            if(cena.modo == "PAUSE" and objetos[2].selecionado):
                cena.camera.definirFoco(cena.jogador.pos)                
                cena.modo = "fase1"
            elif(cena.modo == "PAUSE" and objetos[3].selecionado):
                cena.modo = "fase1"                
                cena.terminou = True
                cena.jogador.pos = [0,0]
                cena.proximaCena = "fase1"
            elif(cena.modo == "PAUSE" and objetos[4].selecionado):
                cena.modo = "fase1"                
                cena.terminou = True
                cena.proximaCena = "menuPrincipal"

        
            
            
fase1 = {
    "nome": "Fase 1",
    "modos": ["fase1", "PAUSE", "SAIR"],
    "modoInicial": 0,
    "start": fase1Start,
    "update": fase1Update,
    "objetos": [
            {
             "tipo": "plataforma", 
             "camada": "fase1",
             "nome": "plataforma",      
             "pos": [0, 380], 
             "altura": 50,
             "largura": 1000
        },

        {
             "tipo": "player", 
             "camada": "fase1",
             "nome": "Jogador",      
             "pos": [50, 70],
             "altura": 60,
             "largura": 30
        },
        {
                "tipo": "botão",
                "nome": "Continuar",
                "pos": [250, 180],
                "id": "1",
                "texto": "Continuar",
                "camada": "PAUSE"
        },
        {
                "tipo": "botão",
                "nome": "Continuar",
                "pos": [250, 230],
                "id": "1",
                "texto": "Recomeçar",
                "camada": "PAUSE"
        },
        {
                "tipo": "botão",
                "nome": "Continuar",
                "pos": [250, 280],
                "id": "1",
                "texto": "Sair",
                "camada": "PAUSE"
        },

        {
             "tipo": "plataforma", 
             "camada": "fase1",
             "nome": "plataforma",      
             "pos": [200, 280], 
             "altura": 100,
             "largura": 100
        }
    ]
}
