class Physics:
    def detectCollision(self, obj, MAP):
        if (obj.pos[0]+20,obj.pos[1]) == MAP:
                print("right collision")
                return {
                    "type":"right"
                }
        elif (obj.pos[0]-20,obj.pos[1]) == MAP:
                print("left collision")
                return {
                    "type":"left"
                }
        elif (obj.pos[0],obj.pos[1]-20) == MAP:
                print("top collision")
                return {
                    "type":"top"
                }
        elif (obj.pos[0],obj.pos[1]+20) == MAP:
                print("bottom collision")
                return {
                    "type":"bottom"
                }
        return {
                "type": "false"
            }

