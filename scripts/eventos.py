import pygame

class GerenciadorEventos:
    def __init__(self, model):

    def checarEventos():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    char.interact = True
                else:
                    char.interact = False                     
                if event.key == pygame.K_LEFT:
                    char.vel[0] = -20
                elif event.key == pygame.K_RIGHT:
                    char.vel[0] = 20
                elif event.key == pygame.K_UP:
                    char.vel[1] = -20
                elif event.key == pygame.K_DOWN:
                    char.vel[1] = 20
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    char.vel[0] = 0
                elif event.key == pygame.K_RIGHT:
                    char.vel[0] = 0
                elif event.key == pygame.K_UP:
                    char.vel[1] = 0
                elif event.key == pygame.K_DOWN:
                    char.vel[1] = 0