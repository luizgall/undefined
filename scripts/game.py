#IMPORTS
import pygame
import sys
BLACK = (0,0,0)
#INICIAR PYGAME
pygame.init()
tela = pygame.display.set_mode((600,400))

MAP = []
i = 0
def detectCollision(obj, MAP):
    for i in range(len(MAP)):
        if obj["x"] >= MAP[i][0] and obj["x"] <= MAP[i][0] + 20 and obj["y"] <= MAP[i][1] + 20:
            print("collision")
            return True
        return False
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
            
drawLine(MAP, 40, 20, 40, 360)
drawLine(MAP, 560, 20, 560, 360)
drawLine(MAP, 40, 20, 580, 20)
drawLine(MAP, 40, 360, 580, 360)

char = {
    "x":100,
    "y":100,
    "velY":0,
    "velX":0
}
#GAME LOOP
while True:
    #detectar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                char["velX"] -= 0.1
            elif event.key == pygame.K_RIGHT:
                char["velX"] += 0.1
            elif event.key == pygame.K_UP:
                char["velY"] -= 0.1
            elif event.key == pygame.K_DOWN:
                char["velY"] += 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                char["velX"] += 0.1
            elif event.key == pygame.K_RIGHT:
                char["velX"] -= 0.1
            elif event.key == pygame.K_UP:
                char["velY"] += 0.1
            elif event.key == pygame.K_DOWN:
                char["velY"] -= 0.1

    if(not detectCollision(char, MAP)):
        char["x"] += char["velX"]
        char["y"] += char["velY"]
    
    #renderizar 
    tela.fill((255,255,255))
    for i in range(len(MAP)):
        pygame.draw.rect(tela, BLACK, (MAP[i][0],MAP[i][1],20,20))    
    pygame.draw.rect(tela, BLACK, (char["x"],char["y"],20,20))
    pygame.display.flip()

