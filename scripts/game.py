#IMPORTS
import pygame
import sys
from physics import Physics
from gameObject import GameObject
from scenes import Scene
import scenesModel
import random

physics = Physics()
BLACK = (0,0,0)
#INICIAR PYGAME
pygame.init()
pygame.font.init()
tela = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()

MAP = []
i = 0

menu = Scene(scenesModel.menuPrincipal)
menu.start()

def rangeIntersect(min0, max0, min1, max1):
        return max(min0,max0)>= min(min1,max1) and min(min0,max0)<=max(min1,max1);

def drawLine(obj, a,b,x,y):
    while a != x or b != y:
        obj.append((a,b))
        if (a < x and a != x):
            a += 20
        elif (a > x and a != x):
            a -= 20
        if (b < y and b != y):
            b += 20
        elif (b > y and b != y):
            b -= 20
            
# drawLine(MAP, 40, 20, 40, 360)
# drawLine(MAP, 560, 20, 560, 360)
# drawLine(MAP, 40, 20, 580, 20)
# drawLine(MAP, 40, 360, 580, 360)

char = {
    "x":100,
    "y":100,
    "velY":0,
    "velX":0
}
charModel = {
    "nome": "char",
    "pos": [100,100],
    "tipo": "char"
}

char = GameObject(charModel)

#GAME LOOP
while True:
    #detectar eventos
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
    for i in range(len(MAP)):
        collision = physics.detectCollision(char,MAP[i])
        if(collision['type'] == 'top'):
            char.vel[1] = max(0,char.vel[1])
        elif (collision['type'] == 'bottom'):
            char.vel[1] = min(0,char.vel[1])
        elif (collision['type'] == 'right'):
            char.vel[0] = min(0,char.vel[0])   
        elif (collision['type'] == 'left'):
            char.vel[0] = max(0,char.vel[0])   
    char.pos[0] += char.vel[0]
    char.pos[1] += char.vel[1]
    
    
    #renderizar 
    tela.fill((255,255,255))
    # menu.update(tela)
    # for i in range(len(MAP)):
    #     pygame.draw.rect(tela, BLACK, (MAP[i][0],MAP[i][1],20,20))    
    # char.draw(tela)
    menu.update(tela)
    pygame.display.flip()
    clock.tick(60)
