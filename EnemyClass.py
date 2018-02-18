class EnemyClass:
    speed = null
    speedDirection = null # -1 is negative, 1 is positive
    health = null
    trajectory = null
    angleOfTrajectory = null# range PI/4 and PI/2
    position = null
    radius = null

    # boolean for spawn location
    topOrBottom = null
    rightOrLeft = null

    
    def __init__(self, health, speed, radius):
        self.speed = speed 
        self.health = health
        self.radius = radius
        
        trajectory = [0,0]
        position = [0,0]

        topOrBottom = False
        rightOrLeft = False 
     

        # 0 is right side, 1 is top side, 2 is left side, 3 is bottom side    
        randomSide = Math.rand(0,3)
        
        # x.range = 600 --> screen x range
        # y.range = 400 --> screen y range
        # randomly spawning objects on sides of screen

        # right side
        if(direction == 0):
            topOrBottom = True
            position = [600, Math.random(0,400)]
        # top side
        elif(direction == 1):
            rightOrLeft = True
            position = [Math.random(0,600),0]
        # left side
        elif(direction == 2):
            topOrBottom = True
            position = [0, Math.random(0,400)]
        # bottom side
        elif(direction == 3):
            rightOrLeft = True
            position = [Math.random(0,600),400]

        # angle of movement based on position relative to center of side
        angleOfTrajectory = Math.random(Math.PI/4, Math.PI/2)

        # COORDINATES START AT TOP LEFT CORNER
        
        # negative if above midpoint
        # positive if below midpoint
        if(topOrBottom == True):
            if(position[0] < 600/2):
                speedDirection = -1
            else:
                speedDirection = 1

        # negative if below midpoint
        # positive if above midpoint
        if(rightOrLeft == True):
            if(position[0] < 400/2):
                speedDirection = 1
            else:
                speedDirection = -1
                
            else:
                angleOfTrajectory = Math.random(Math.PI/2, Math.PI/2)
                trajectory = [Math.cos(angleOfTrajectory), Math.sin(angleOfTrajectory)]
            


    def move():
        # updates position with trajectory speed
        position[0]=position[0]+trajectory[0]
        position[1]=position[1]+trajectory[0]
        
        

    def detect():
     
        if(((self.x - Player.x)**2 + (self.y - Player.y)**2)**(1/2) <= radius):
            damage()

        if((self.x < 0 or self.x > 600) or (self.y < 0 or self.y < 400)):
            # this.destroy()
            


    def damage():
        if(lives > 0):
            lives = lives -1
            
        
    def die():
        return (self.lives == 0)

        
        
