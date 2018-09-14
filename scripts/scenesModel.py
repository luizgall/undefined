import pygame
import sys
from gameObject import GameObject
from tela import tela
from eventos import GerenciadorEventos

def menuPrincipalStart(objetos):
    objetos[0].selecionado = True

def menuPrincipalUpdate(objetos):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_UP:
            if event.key == pygame.K_DOWN:
                if objetos[0].selecionado:
                    objetos[0].selecionado = False
                    objetos[1].selecionado = True
                elif objetos[1].selecionado:
                    objetos[1].selecionado = False
                    objetos[2].selecionado = True
                elif objetos[2].selecionado:
                    objetos[2].selecionado = False
                    objetos[0].selecionado = True
            if event.key == pygame.K_UP:
                if objetos[0].selecionado:
                    objetos[0].selecionado = False
                    objetos[2].selecionado = True
                elif objetos[1].selecionado:
                    objetos[1].selecionado = False
                    objetos[0].selecionado = True
                elif objetos[2].selecionado:
                    objetos[2].selecionado = False
                    objetos[1].selecionado = True

            if event.key == pygame.K_RETURN:
                print("ENTER")
            
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
    "start": menuPrincipalStart,
    "update":menuPrincipalUpdate,
    "objetos": [
        {
            "tipo" : "botão",
            "nome": "botao",
            "pos": [100,100],
            "id": "1",
            "texto": "undefined"
        },
        {
            "tipo" : "botão",
            "nome": "botao",
            "pos": [100,200],
            "id": "1",
            "texto": "começar"
        },

        {
            "tipo" : "botão",
            "nome": "botao",
            "pos": [100,300],
            "id": "1",
            "texto": "sair"
        }
        
    ]
}

