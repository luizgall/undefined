import pygame
from gameObject import GameObject
def menuPrincipalStart():
    print("oi")

def menuPrincipalUpdate(tela , objetos):
    objetos[0].selecionado = True
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
