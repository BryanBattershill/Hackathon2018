import random
import math

class EnemyClass:
    
    speed = 0
    speedDirection = 0 # -1 is negative, 1 is positive
    trajectory = [] #[0,1]
    angleOfTrajectory = 0 # range PI/4 and PI/2
    position = [] #[0,1]
    radius = 0
    corners = [] #[0,1,2,3]

    # boolean for spawn location

    destroyed = False
    outOfBounds = False
    absorbed = False

    # constructor    
    def __init__(self, speed, radius):
        
        self.speed = speed 
        self.radius = radius

        # 0 is right side, 1 is top side, 2 is left side, 3 is bottom side    
        randomSide = random.randint(0,3)
        
        # x.range = 600 --> screen x range
        # y.range = 400 --> screen y range
        # randomly spawning objects on sides of screen
        
        # angle of movement based on position relative to center of side
        # self.angleOfTrajectory = random.randint(a,b)

        # corner = [0,1,2,3]
        # 0 = top right corner, 1 = top left corner, 2 = bottom left corner, 3 = bottom right corner
        
        # right side
        if(self.direction == 0):
            self.position = [600, random.randint(0,400))]

            if(self.position[1] <= 400/2):
                corner=[False,False,False,True] # bottom right corner
            else:
                corner=[True, False, False, False] # top right corner           
                
        # top side
        elif(self.direction == 1):
            self.position = [random.randint(0,600),0]

            if(self.position[0] >= 600/2):
                corner=[True,False,False,False] # top right corner
            else:
                corner=[False,True,False,False] # top left corner
                
        # left side
        elif(self.direction == 2):
            self.position = [0, random.randint(0,400)]

            if(self.position[1] >= 400/2):
                corner=[False,True,False,False] # top left corner
            else:
                corner=[False,False,True,False] # bottom left corner
                
        # bottom side
        elif(direction == 3):
            self.position = [random.randint(0,600),400]

            if(self.position[0] <= 600/2):
                corner=[False,False,True,False] # bottom left corner
            else:
                corner=[False,False,False,True] # bottom right corner
                

        

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
            
      

    # run in update
    def stateDetect():
        # if destroyed == true, increment score, if outOfBounds == true then increase speed
        # if absorbed == true, increase the radius of the boss
        return [destroyed, outOfBounds, absorbed] # [0, 1, 2]
            

     # run in update, after stateDetect
     def collision(player, boss):

        self.position[0]=self.position[0]+self.trajectory[0]
        self.position[1]=self.position[1]+self.trajectory[0]
        
        if(((self.x - [player.x)**2 + (self.y - player.y)**2)**(1/2) <= player.getRadius):
            destroyed = True

        if((self.x < 0 or self.x > 600) or (self.y < 0 or self.y < 400)):
            outOfBounds = True
           

        if(((self.x - [boss.x)**2 + (self.y - boss.y)**2)**(1/2) <= boss.getRadius):
            destroyed = True

        if((self.x < 0 or self.x > 600) or (self.y < 0 or self.y < 400)):
            absorbed = True



        


        
        
