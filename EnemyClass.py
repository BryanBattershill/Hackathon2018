import random
import math

class EnemyClass:
    
    speed = 0
    speedDirection = 0 # -1 is negative, 1 is positive
    trajectory = [0,0]
    angleOfTrajectory = 0 # range PI/4 and PI/2
    position = [0,0]
    radius = 0

    # boolean for spawn location
    topOrBottom = False
    rightOrLeft = False

    
    def __init__(self, speed, radius):
        
        self.speed = speed 
        self.radius = radius

        # 0 is right side, 1 is top side, 2 is left side, 3 is bottom side    
        randomSide = random.randint(0,3)
        
        # x.range = 600 --> screen x range
        # y.range = 400 --> screen y range
        # randomly spawning objects on sides of screen

        # right side
        if(self.direction == 0):
            self.topOrBottom = True
            self.position = [600, random.randint(0,400))]
        # top side
        elif(self.direction == 1):
            self.rightOrLeft = True
            self.position = [random.randint(0,600),0]
        # left side
        elif(self.direction == 2):
            self.topOrBottom = True
            self.position = [0, random.randint(0,400)]
        # bottom side
        elif(direction == 3):
            self.rightOrLeft = True
            self.position = [random.randint(0,600),400]

        # angle of movement based on position relative to center of side
        self.angleOfTrajectory = random.randint(math.pi/4, math.pi/2)

        # COORDINATES START AT TOP LEFT CORNER
        
        # negative if above midpoint
        # positive if below midpoint
        if(self.topOrBottom == True):
            if(self.position[0] < 600/2):
                self.speedDirection = -1
            else:
                self.speedDirection = 1

        # negative if below midpoint
        # positive if above midpoint
        if(self.rightOrLeft == True):
            if(self.position[0] < 400/2):
                self.speedDirection = 1
            else:
                self.speedDirection = -1
                
            else:
                self.angleOfTrajectory = random.randint(math.pi/4, math.pi/2)
                self.trajectory = [self.speedDirection*math.cos(self.angleOfTrajectory),
                                   self.speedDirection*math.sin(self.angleOfTrajectory)]
            

    def move():
        # updates position with trajectory speed
        self.position[0]=self.position[0]+self.trajectory[0]
        self.position[1]=self.position[1]+self.trajectory[0]
        
        

    def detect(player):
     
        if(((self.x - [player.x)**2 + (self.y - player.y)**2)**(1/2) <= radius):
            damage()

        if((self.x < 0 or self.x > 600) or (self.y < 0 or self.y < 400)):
            lives = 0
            die()
            

    def damage():
        if(lives > 0):
            lives = lives -1
            
        
    def die():
        return (self.lives == 0)

        
        
