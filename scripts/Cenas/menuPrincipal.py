import pygame
import sys

def menuPrincipalStart(objetos, cena):
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
                            objetos[3].selecionado = True
                        elif objetos[3].selecionado:
                            objetos[3].selecionado = False
                            objetos[4].selecionado = True
                        elif objetos[4].selecionado:
                            objetos[4].selecionado = False
                            objetos[1].selecionado = True
                if event.key == pygame.K_UP:
                    if cena.modo == "PRINCIPAL":
                        if objetos[1].selecionado:
                            objetos[1].selecionado = False
                            objetos[4].selecionado = True
                        elif objetos[2].selecionado:
                            objetos[2].selecionado = False
                            objetos[1].selecionado = True
                        elif objetos[3].selecionado:
                            objetos[3].selecionado = False
                            objetos[2].selecionado = True
                        elif objetos[4].selecionado:
                            objetos[4].selecionado = False
                            objetos[3].selecionado = True
                if event.key == pygame.K_RETURN:
                    if cena.modo == "PRINCIPAL":
                        if objetos[1].selecionado:
                            cena.modo = "JOGO"
                            cena.terminou = True
                            cena.proximaCena = "fase1"
                        elif objetos[2].selecionado:
                            cena.modo = "INSTRUCOES"
                        elif objetos[3].selecionado:
                            cena.modo = "CREDITOS"
                        elif objetos[4].selecionado:
                            pygame.quit()
                            sys.exit()
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
        "modos": ["PRINCIPAL", "JOGO", "SAIR"],
        "modoInicial": 0,
        "start": menuPrincipalStart,
        "update": menuPrincipalUpdate,
        "objetos": [
            {
                "tipo": "texto",
                "nome": "botao",
                "pos": [210, 100],
                "id": "1",
                "texto": "Fora d'água",
                "camada": "PRINCIPAL"
            },
            {
                "tipo": "botão",
                "nome": "botao",
                "pos": [250, 180],
                "id": "1",
                "texto": "começar",
                "camada": "PRINCIPAL"
            },
            {
                "tipo": "botão",
                "nome": "botao",
                "pos": [240, 230],
                "id": "1",
                "texto": "instruções",
                "camada": "PRINCIPAL"
            },
            {
                "tipo": "botão",
                "nome": "botao",
                "pos": [250, 280],
                "id": "1",
                "texto": "créditos",
                "camada": "PRINCIPAL"
            },

            {
                "tipo": "botão",
                "nome": "botao",
                "pos": [270, 330],
                "id": "1",
                "texto": "sair",
                "camada": "PRINCIPAL"
            },

            {
                "tipo": "texto",
                "nome": "botao",
                "pos": [400, 300],
                "id": "1",
                "texto": "Iniciando jogo",
                "camada": "JOGO"
            },
            {
                "tipo": "texto",
                "nome": "botao",
                "pos": [200, 100],
                "id": "1",
                "texto": "INSTRUÇÕES",
                "camada": "INSTRUCOES"
            },
            {
                "tipo": "texto",
                "nome": "botao",
                "pos": [120, 150],
                "id": "1",
                "texto": "Setas direcionais -> movimento",
                "camada": "INSTRUCOES"
            },
            {
                "tipo": "texto",
                "nome": "botao",
                "pos": [180, 200],
                "id": "1",
                "texto": "ENTER -> confirma",
                "camada": "INSTRUCOES"
            },
            {
                "tipo": "texto",
                "nome": "botao",
                "pos": [200, 250],
                "id": "1",
                "texto": "ESC -> cancelar",
                "camada": "INSTRUCOES"
            },
            {
                "tipo": "texto",
                "nome": "botao",
                "pos": [250, 100],
                "id": "1",
                "texto": "Criador por",
                "camada": "CREDITOS"
            },
            {
                "tipo": "texto",
                "nome": "botao",
                "pos": [260, 200],
                "id": "1",
                "texto": "Luiz Gall",
                "camada": "CREDITOS"
            },

            {
                "tipo": "texto",
                "nome": "botao",
                "pos": [400, 300],
                "id": "1",
                "texto": "Saindo do jogo",
                "camada": "SAIR"
            },

            {
                "tipo": "imagem",
                "nome": "botao",
                "pos": [400, 300],
                "id": "1",
                "texto": "background",
                "camada": "PRINCIPAL"
            }

        ]
    }