import pygame
import sys
from gameObject import GameObject
from tela import tela
from eventos import GerenciadorEventos

def menuPrincipalStart(objetos):
    objetos[1].selecionado = True

def menuPrincipalUpdate(objetos, cena):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_UP:
            if event.key == pygame.K_DOWN:
                if cena.modo == "PRINCIPAL":
                    if objetos[1].selecionado:
                        objetos[1].selecionado = False
                        objetos[2].selecionado = True
                    elif objetos[2].selecionado:
                        objetos[2].selecionado = False
                        objetos[1].selecionado = True
            if event.key == pygame.K_UP:
                if cena.modo == "PRINCIPAL":                
                    if objetos[1].selecionado:
                        objetos[1].selecionado = False
                        objetos[2].selecionado = True
                    elif objetos[2].selecionado:
                        objetos[2].selecionado = False
                        objetos[1].selecionado = True
            if event.key == pygame.K_RETURN:
                if cena.modo == "PRINCIPAL":                
                    if objetos[1].selecionado:
                        cena.modo = "JOGO"
                    elif objetos[2].selecionado:
                        cena.modo = "SAIR"
            if event.key == pygame.K_ESCAPE:
                cena.modo = "PRINCIPAL"
            
    # myfont = pygame.font.SysFont('Arial', 30)
    # font = myfont.render('- undefined -', False, (0, 0, 0))
    # tela.blit(font,(0,0))
    # font = myfont.render('começar', False, (0, 0, 0))
    # tela.blit(font,(0,50))
    # font = myfont.render('instruções', False, (0, 0, 0))
    # tela.blit(font,(0,100))
    # font = myfont.render('créditos', False, (0, 0, 0))
    # tela.blit(font,(0,150))
    # font = myfont.render('sair', False, (0, 0, 0))
    # tela.blit(font,(0,200))
    


menuPrincipal = {
    "nome": "Menu Principal",
    "modos": ["PRINCIPAL", "JOGO", "SAIR" ],
    "modoInicial": 0,
    "start": menuPrincipalStart,
    "update":menuPrincipalUpdate,
    "objetos": [
        {
            "tipo" : "texto",
            "nome": "botao",
            "pos": [100,100],
            "id": "1",
            "texto": "undefined",
            "camada": "PRINCIPAL"
        },
        {
            "tipo" : "botão",
            "nome": "botao",
            "pos": [100,200],
            "id": "1",
            "texto": "começar",
            "camada": "PRINCIPAL"            
        },

        {
            "tipo" : "botão",
            "nome": "botao",
            "pos": [100,300],
            "id": "1",
            "texto": "sair",
            "camada": "PRINCIPAL"            
        },

        {
            "tipo" : "texto",
            "nome": "botao",
            "pos": [400,300],
            "id": "1",
            "texto": "Iniciando jogo",
            "camada": "JOGO"            
        },

        {
            "tipo" : "texto",
            "nome": "botao",
            "pos": [400,300],
            "id": "1",
            "texto": "Saindo do jogo",
            "camada": "SAIR"            
        }
        
    ]
}

