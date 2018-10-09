import pygame 

class Physics:
    def detectarColisao(self, obj, obj2):
        rect1 = pygame.Rect(obj.pos[0], obj.pos[1], obj.largura, obj.altura)
        rect2 = pygame.Rect(obj2.pos[0], obj2.pos[1], obj2.largura, obj2.altura)
        if rect1.colliderect(rect2):
            return True
        else:
            return False
        
    def atualizar(self, objetos):
        for obj in objetos:
            if(obj.tipo == "player"):
                obj.vel[1] += 1  
                obj.pos[0] += obj.vel[0]
                obj.pos[1] += obj.vel[1]
                
                for obj2 in objetos:
                    if obj2.tipo != "player":
                        if self.detectarColisao(obj, obj2):
                            # obj.vel[0] = obj.vel[0] * -0.1
                            # obj.vel[1] = obj.vel[1] * -0.5
                           
                            if obj.vel[1] > 0:
                                obj.vel[1] = 0
                                obj.pos[1] = obj2.pos[1] - 1 - obj.altura
                                obj.caindo = False
                            # elif obj.vel[0] >= 0 and obj.pos[1] > obj2.pos[1]:
                            #     obj.vel[0] = 0
                            #     obj.pos[0] = obj2.pos[0] - obj.largura - 1
                        # else:
                        #     obj.caindo = True
                            # if(colisao["tipo"] == "topo"):
                            #     obj.vel[1] = 0
                            #     obj.pos[1] = obj2.pos[1] - 1 - obj.altura
                            #     obj.caindo = False
                            # if(colisao["tipo"] == "esquerda"):
                            #     pass
                                # obj.vel[0] = 0
                                # obj.pos[0] = obj.pos[0] - obj2.pos[0] + obj2.largura
                            # if(colisao["tipo"] == "topoDireita"):                            
                            #     obj.pos[0] = obj2.pos[0]


class Forca():
    def __init__(self):
        self.x = 0
        self.y = 0
        pass
    def adicionar(self, forca):
        
        return 
    

# def drawLine(obj, a,b,x,y):
#     while a != x or b != y:
#         obj.append((a,b))
#         if (a < x and a != x):
#             a += 20
#         elif (a > x and a != x):
#             a -= 20
#         if (b < y and b != y):
#             b += 20
#         elif (b > y and b != y):
#             b -= 20
            
# drawLine(MAP, 40, 20, 40, 360)
# drawLine(MAP, 560, 20, 560, 360)
# drawLine(MAP, 40, 20, 580, 20)
# drawLine(MAP, 40, 360, 580, 360)


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
    