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

