# USAGE
# python object_movement.py --video object_tracking_example.mp4
# python object_movement.py

# import the necessary packages
from collections import deque
import numpy as np
import argparse
import imutils
import cv2
import math
import time
import random
import sys

class EnemyClass:
    
    speed = 0
    radius = 0
    trajectory = [] #[0,1]
    positionE = [] #[0,1]
    corners = 0 #[0,1,2,3]
     
    xrange = 0
    yrange = 0

    # boolean for spawn location

    destroyed = False
    outOfBounds = False
    absorbed = False

    # constructor    
    def __init__(self, speed, radius):
        
        self.speed = speed 
        self.radius = radius
         
        self.xrange = 600
        self.yrange = 450
        positionE = [0,0]
        trajectory = [0,0]

        # 0 is right side, 1 is top side, 2 is left side, 3 is bottom side    
        randomSide = random.randint(0,3)
        # angle of movement based on position relative to center of side
        angleOfTrajectory = 0

        # x.range = 600 --> screen x range
        # y.range = 400 --> screen y range
        # randomly spawning objects on sides of screen


        # corner = [0,1,2,3]
        # 0 = top right corner, 1 = top left corner, 2 = bottom left corner, 3 = bottom right corner   
        # COORDINATES START AT TOP LEFT CORNER
        
  # right side
         # right side
        # right side
        if(randomSide == 0):
            self.positionE = [self.xrange, random.randint(0,self.yrange)]

            if(self.positionE[1] >= self.yrange/2):
                corner= 3# bottom right corner
                angleOfTrajectory = random.uniform(4*math.pi/6,5*math.pi/6)
                self.trajectory = [math.cos(angleOfTrajectory)*self.speed,-math.sin(angleOfTrajectory)*self.speed]
                
               
            else:
                corner=0 # top right corner
                angleOfTrajectory = random.uniform(7*math.pi/6,4*math.pi/3)
                self.trajectory = [math.cos(angleOfTrajectory)*self.speed,-math.sin(angleOfTrajectory)*self.speed]
        
                  
        # top side
        elif(randomSide == 1):
            self.positionE = [random.randint(0,self.xrange),0]

            if(self.positionE[0] >= self.xrange/2):
                corner=0 # top right corner
                angleOfTrajectory = random.uniform(7*math.pi/6,4*math.pi/3)
                self.trajectory = [math.cos(angleOfTrajectory)*self.speed,-math.sin(angleOfTrajectory)*self.speed]
            else:
                corner=1# top left corner
                angleOfTrajectory = random.uniform(10*math.pi/6,11*math.pi/6)
                self.trajectory = [math.cos(angleOfTrajectory)*self.speed,-math.sin(angleOfTrajectory)*self.speed]
         
                
        # left side
        elif(randomSide == 2):
            self.positionE = [0, random.randint(0,self.yrange)]

            if(self.positionE[1] <= self.yrange/2):
                corner=1 # top left corner
                angleOfTrajectory = random.uniform(10*math.pi/6,11*math.pi/6)
                self.trajectory = [math.cos(angleOfTrajectory)*self.speed,-math.sin(angleOfTrajectory)*self.speed]
                
            else:
                corner=2# bottom left corner
                angleOfTrajectory = random.uniform(math.pi/6,math.pi/3)
                self.trajectory = [math.cos(angleOfTrajectory)*self.speed,-math.sin(angleOfTrajectory)*self.speed]
                
        # bottom side
        elif(randomSide == 3):
            self.positionE = [random.randint(0,self.xrange),self.yrange]
                       
            if(self.positionE[0] <= self.xrange/2):
                corner =2
                angleOfTrajectory = random.uniform(math.pi/6,math.pi/3) # bottom left corner
                self.trajectory = [math.cos(angleOfTrajectory)*self.speed,-math.sin(angleOfTrajectory)*self.speed]
            else:
                corner=3 # bottom right corner
                angleOfTrajectory = random.uniform(4*math.pi/6,5*math.pi/6)
                self.trajectory = [-math.cos(angleOfTrajectory)*self.speed,math.sin(angleOfTrajectory)*self.speed]
     


            

    # run as update
    def stateDetect(self):
        # if destroyed == true, increment score, if outOfBounds == true then increase speed
        # if absorbed == true, increase the radius of the boss
        return [self.destroyed, self.outOfBounds, self.absorbed] # [0, 1, 2]

    def move(self):
        self.positionE[0]=self.positionE[0]+self.trajectory[0]
        self.positionE[1]=self.positionE[1]+self.trajectory[1]
        pass
    # run as update, after stateDetect
    def collision(self,playerPosition, boss, tempFrame):
        try:
            if((((self.positionE[0]-playerPosition[0])**2 + (self.positionE[1] - playerPosition[1])**2)**(1/2)) <= 30): # player radius is 30
                self.destroyed = True

            if(self.positionE[0] < 0 or self.positionE[0] > self.xrange or self.positionE[1] < 0 or self.positionE[1] > self.yrange):
                self.outOfBounds = True
                
            if(((self.positionE[0] - boss.position[0])**2 + (self.positionE[1] - boss.position[1])**2)**(1/2) <= boss.radius):
                self.absorbed = True
        except:
            pass
        

        



class PlayerClass:
    pBuffer = 0
    lives = 3
    pColor = (29, 120, 6)
    def damage(self):
        if self.invuln()==False:
            self.lives = self.lives - 1
            self.dead()
            self.pBuffer = time.time()
            self.pColor = (255,0,0)
    def invuln(self):
        return self.pBuffer !=0
    def dead(self):
        if self.lives == 0:
            sys.exit()
    def updateBuffer(self):
        if (time.time()-self.pBuffer) > 2:
            self.pBuffer = 0
            self.pColor = (29, 120, 6)
            


class BossClass:
    speed = 2
    Bdirection = 0
    radius = 50
    position = [200, 200]


    def incSize(self):
        self.radius += 1

    def incSpeed(self):
        self.speed += 1

    def move(self, pos, PRadius, playerRef):
        deltx = pos[0] - self.position[0]
        delty = self.position[1] - pos[1]
        if deltx != 0:
            Bdirection = math.atan(delty / deltx)
            if deltx>0:
                self.position[0] += self.speed * math.cos(Bdirection)
                self.position[1] += self.speed * -math.sin(Bdirection)
            else:
                self.position[0] += self.speed * -math.cos(Bdirection)
                self.position[1] += self.speed * math.sin(Bdirection)


        if math.sqrt(deltx ** 2 + delty ** 2) <= self.radius + PRadius:
            playerRef.damage()



# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
    help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=32,
    help="max buffer size")
args = vars(ap.parse_args())

# define the lower and upper boundaries of the "green"
# ball in the HSV color space
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)

# initialize the list of tracked points, the frame counter,
# and the coordinate deltas
pts = deque(maxlen=args["buffer"])
counter = 0
(dX, dY) = (0, 0)
damageBuffer = 0
direction = ""
score = 0
timer = time.time()

boss = BossClass()
player = PlayerClass()
allEnemies = []
enemySpawnTime = time.time()
           
# if a video path was not supplied, grab the reference
# to the webcam
if not args.get("video", False):
    camera = cv2.VideoCapture(0)

# otherwise, grab a reference to the video file
else:
    camera = cv2.VideoCapture(args["video"])

# keep looping
while True:
    # grab the current frame
    (grabbed, frame) = camera.read()
    frame = cv2.flip(frame, 1)
    if(time.time() - enemySpawnTime > 1):           
        allEnemies.append(EnemyClass(2,30))
        enemySpawnTime = time.time()
           
    for i in range(len(allEnemies)):
        cv2.circle(frame, (round(allEnemies[i].positionE[0]),  round(allEnemies[i].positionE[1])), 25, (0, 255, 255), -1)
        allEnemies[i].move()
           
        if(allEnemies[i].stateDetect()[0] == True):
           allEnemies.pop(i)
           score+=1
           break
        
        elif(allEnemies[i].stateDetect()[1] == True):
           allEnemies.pop(i)
           boss.incSpeed()
           break
           
        elif(allEnemies[i].stateDetect()[2] == True):
           allEnemies.pop(i)
           boss.incSize()
           break
           
        allEnemies[i].collision(center, boss, frame)
           


    # if we are viewing a video and we did not grab a frame,
    # then we have reached the end of the video
    if args.get("video") and not grabbed:
        break

    # resize the frame, blur it, and convert it to the HSV
    # color space
    frame = imutils.resize(frame, width=600)
    # blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # construct a mask for the color "green", then perform
    # a series of dilations and erosions to remove any small
    # blobs left in the mask
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # find contours in the mask and initialize the current
    # (x, y) center of the ball
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    # only proceed if at least one contour was found
    if len(cnts) > 0:
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # only proceed if the radius meets a minimum size
        if radius > 10:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            #cv2.circle(frame, (int(x), int(y)), int(radius),
            #	(0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
            pts.appendleft(center)
    try:
        boss.move([center[0], center[1]], 30, player)
        if (player.invuln()):
            player.updateBuffer()
    except:
        pass
    cv2.circle(frame, (round(boss.position[0]), round(boss.position[1])), boss.radius, (0, 255, 255),-1)
    # loop over the set of tracked points
    for i in np.arange(1, len(pts)):
        # if either of the tracked points are None, ignore
        # them
        if pts[i - 1] is None or pts[i] is None:
            continue

        # check to see if enough points have been accumulated in
        # the buffer
        try:
            if counter >= 10 and i == 1 and pts[-10] is not None:
                # compute the difference between the x and y
                # coordinates and re-initialize the direction
                # text variables
                dX = pts[-10][0] - pts[i][0]
                dY = pts[-10][1] - pts[i][1]
                (dirX, dirY) = ("", "")

##                # ensure there is significant movement in the
##                # x-direction
##                if np.abs(dX) > 20:
##                    dirX = "East" if np.sign(dX) == 1 else "West"
##
##                # ensure there is significant movement in the
##                # y-direction
##                if np.abs(dY) > 20:
##                    dirY = "North" if np.sign(dY) == 1 else "South"
##
##                # handle when both directions are non-empty
##                if dirX != "" and dirY != "":
##                    direction = "{}-{}".format(dirY, dirX)
##
##                # otherwise, only one direction is non-empty
##                else:
##                    direction = dirX if dirX != "" else dirY
        except:
            pass
        # otherwise, compute the thickness of the line and
        # draw the connecting lines
        thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
        cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
        try:
            if center == None:
                pass
            elif(center[0] > 10):
                cv2.circle(frame, (center[0], center[1]), 30, player.pColor, -1)
        except:
            pass

    # show the movement deltas and the direction of movement on
    # the frame
##    cv2.putText(frame, direction, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
##        0.65, (0, 0, 255), 3)
    if not (center == (None)):
        cv2.putText(frame, "Score: {}, Time: {}".format(score, round(time.time()-timer,2)),
            (0, 10), cv2.FONT_HERSHEY_SIMPLEX,
            0.35, (0, 0, 255), 1)

    # show the frame to our screen and increment the frame counter
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    counter += 1
    # if the 'q' key is pressed, stop the loop
    if key == ord("q") or player.lives==0:
        break

# cleanup the camera and close any open windows
camera.release()
#cv2.ims
cv2.destroyAllWindows()
