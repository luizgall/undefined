class Physics:
    def detectarColisao(self, obj, obj2):
        if (obj.pos[1]+ obj.altura > obj2.pos[1]) and (obj.pos[1] + obj.altura < obj2.pos[1] + obj2.altura) and (obj.pos[0] + obj.largura> obj2.pos[0]) and (obj.pos[0] + obj.largura < obj2.pos[0] + obj2.largura):
            return { "colidiu": True, "tipo": "topo"}
        else:
            return {"colidiu": False}
        
    def atualizar(self, objetos):
        for obj in objetos:
            if(obj.tipo == "player"):
                obj.vel[1] += 1  
                obj.pos[0] += obj.vel[0]
                obj.pos[1] += obj.vel[1]
                for obj2 in objetos:
                    if obj2.tipo != "player":
                        colisao = self.detectarColisao(obj, obj2)
                        if colisao["colidiu"]:
                            if(colisao["tipo"] == "topo"):
                                obj.vel[1] = 0
                                obj.pos[1] -= 1
                                obj.caindo = False
                            # if(colisao["tipo"] == "topoDireita"):                            
                            #     obj.pos[0] = obj2.pos[0]



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
    