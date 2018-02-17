class BossClass:
    speed
    direction
    radius
    position
    def __init__(self):
        speed = 5
        radius = 5
        position = (0,0)
    def incSize():
        size += 1
    def incSpeed():
        speed+= 1
    def move(pos):
        dx = pos[0]-position[0]
        dy = position[1]-pos[1]
        direction = math.atan(dy/dx)
        position[0] += speed*cos(direction)
        position[1] += speed*sin(direction)
