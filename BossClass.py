class BossClass:
    speed
    direction
    radius
    position
    def __init__(self):
        speed = 5
        radius = 5
        position = (0,0)
    def incSize(self):
        size += 1
    def incSpeed(self):
        speed+= 1
    def move(self,pos,PRadius,player):
        dx = pos[0]-position[0]
        dy = position[1]-pos[1]
        direction = math.atan(dy/dx)
        position[0] += speed*math.cos(direction)
        position[1] += speed*math.sin(direction)
        if math.sqrt(dx**2+dy**2)<=radius+PRadius:
            player.damage()
        
    
