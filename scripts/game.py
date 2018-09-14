#IMPORTS
import pygame
import sys
from physics import Physics
from scenes import GerenciadorCenas


physics = Physics()
BLACK = (0,0,0)
#INICIAR PYGAME
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

MAP = []
i = 0

gerenciadorCenas = GerenciadorCenas()
gerenciadorCenas.iniciar()

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

#GAME LOOP
while True:
    # for i in range(len(MAP)):
    #     collision = physics.detectCollision(char,MAP[i])
    #     if(collision['type'] == 'top'):
    #         char.vel[1] = max(0,char.vel[1])
    #     elif (collision['type'] == 'bottom'):
    #         char.vel[1] = min(0,char.vel[1])
    #     elif (collision['type'] == 'right'):
    #         char.vel[0] = min(0,char.vel[0])   
    #     elif (collision['type'] == 'left'):
    #         char.vel[0] = max(0,char.vel[0])   
    # char.pos[0] += char.vel[0]
    # char.pos[1] += char.vel[1]
    
    #renderizar 
    gerenciadorCenas.atualizar()
    clock.tick(60)
