class Physics:
    def detectCollision(self, obj, MAP):
        if (obj.pos[0]+20,obj.pos[1]) == MAP:
                obj.touch(MAP)
                return {
                    "type":"right"
                }
        elif (obj.pos[0]-20,obj.pos[1]) == MAP:
                obj.touch(MAP)            
                return {
                    "type":"left"
                }
        elif (obj.pos[0],obj.pos[1]-20) == MAP:
                obj.touch(MAP)            
                return {
                    "type":"top"
                }
        elif (obj.pos[0],obj.pos[1]+20) == MAP:
                obj.touch(MAP)            
                return {
                    "type":"bottom"
                }
        return {
                "type": "false"
            }



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
    