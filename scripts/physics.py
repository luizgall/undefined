class Physics:
    def detectCollision(self, obj, MAP):
        if (obj['x']+20,obj['y']) == MAP:
                print("right collision")
                return {
                    "type":"right"
                }
        elif (obj['x']-20,obj['y']) == MAP:
                print("left collision")
                return {
                    "type":"left"
                }
        elif (obj['x'],obj['y']-20) == MAP:
                print("top collision")
                return {
                    "type":"top"
                }
        elif (obj['x'],obj['y']+20) == MAP:
                print("bottom collision")
                return {
                    "type":"bottom"
                }
        return {
                "type": "false"
            }

